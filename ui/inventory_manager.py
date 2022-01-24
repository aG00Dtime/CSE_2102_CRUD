import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from funcs.connector import db_conn
from funcs.window_position import window_pos

root = os.path.abspath(os.curdir)


class InventoryManager(Tk):
    def __init__(self, access_level, username):
        super(InventoryManager, self).__init__()

        self.title("Inventory Manager")

        self.geometry(window_pos(890, 630))

        self.resizable(False, False)

        self.access_level = access_level
        self.username = username

        # icon
        self.iconbitmap(os.path.join(root, 'assets', 'icon.ico'))

        self.window_title = Label(self, text="Inventory Manager", font="ARIAL 16 bold").grid(pady=(20, 20))

        self.tabs = Notebook(self)

        self.tab1 = Frame(self.tabs)
        self.tab2 = Frame(self.tabs)

        self.tabs.add(self.tab1, text="View Inventory")

        self.tabs.add(self.tab2, text='Add Device')

        self.tabs.grid()

        self.tree = Treeview(self.tab1, height=20, show='headings')

        # tree position
        self.tree.grid(row=3, column=0, columnspan=4, padx=(10, 0))

        self.scrollbar = Scrollbar(self.tab1, orient="vertical", command=self.tree.yview)

        self.scrollbar.grid(row=3, column=4, sticky="NS")

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        self.tree['columns'] = ("1", "2", "3", "4", "5")

        self.tree.heading("1", text="ID")
        self.tree.heading("2", text="Device")
        self.tree.heading("3", text="Description")
        self.tree.heading("4", text="Serial Number")
        self.tree.heading("5", text="Supplier")

        self.tree.column("1", anchor=CENTER, width=50)

        for i in range(2, 6):
            self.tree.column(str(i), anchor=W)

        self.device_list = Button(self.tab1, text="View Available Devices List", width=40, command=self.get_devices)
        self.device_list.grid(row=0, padx=(270, 0), pady=30)

        # tab 2 ###################################################################################################

        self.device_name = Label(self.tab2, text="Device Name").grid(row=0, column=0, pady=(20, 5), padx=(220, 0))
        self.device_name_combobox = Combobox(self.tab2, state='readonly', width=40)

        self.device_name_combobox['values'] = ['Switch', 'Router', 'Modem', 'Repeater', 'Access Point', 'Antenna']
        self.device_name_combobox.grid(row=0, column=1, pady=(20, 5))

        self.supplier_name = Label(self.tab2, text="Supplier").grid(row=1, column=0, pady=(20, 5), padx=(220, 0))
        self.supplier_combobox = Combobox(self.tab2, state='readonly', width=40)
        self.supplier_combobox['values'] = self.get_suppliers()
        self.supplier_combobox.grid(row=1, column=1, pady=(20, 5))

        self.device_description = Label(self.tab2, text="Description").grid(row=2, column=0, pady=(20, 5),
                                                                            padx=(220, 0))
        self.device_description_entry = Entry(self.tab2, width=42)
        self.device_description_entry.grid(row=2, column=1, pady=(20, 5))

        self.device_serial = Label(self.tab2, text="Serial Number").grid(row=3, column=0, pady=(20, 5),
                                                                         padx=(220, 0))
        self.device_serial_number_entry = Entry(self.tab2, width=42)
        self.device_serial_number_entry.grid(row=3, column=1, pady=(20, 5))

        self.add_device_button = Button(self.tab2, width=38, text="Add Device", command=self.add_device).grid(row=4,
                                                                                                              column=1,
                                                                                                              pady=(
                                                                                                                  20, 5
                                                                                                              ))

        ############################################################################################################

    def add_device(self):

        device_name = self.device_name_combobox.get()
        device_serial_number = self.device_serial_number_entry.get()
        device_supplier = self.supplier_combobox.get()
        device_description = self.device_description_entry.get()

        if not device_name or not device_supplier or not device_description or not device_serial_number.isnumeric():
            messagebox.showerror(title="Error", message="Ensure All fields are filled in and correct", parent=self.tab2)
            return

        supplier_id, supplier = device_supplier.split()

        self.device_description_entry.delete(0, END)
        self.device_serial_number_entry.delete(0, END)
        self.supplier_combobox.set(" ")
        self.device_name_combobox.set(" ")

        db = db_conn()
        cur = db.cursor()

        cur.execute(f"""   
            INSERT INTO INVENTORY
            (DEVICE_NAME,DEVICE_SERIAL_NUMBER,DEVICE_DESCRIPTION,SUPPLIER_ID)
            VALUES('{device_name}','{device_serial_number}','{device_description.lower()}','{supplier_id}')
            """)

        db.commit()
        db.close()

        messagebox.showinfo(title="Success", message="Added New Device", parent=self.tab2)

    def get_suppliers(self):
        db = db_conn()
        cur = db.cursor()

        cur.execute("SELECT SUPPLIER_ID,SUPPLIER_NAME FROM SUPPLIERS")

        suppliers = cur.fetchall()
        if not suppliers:
            messagebox.showerror(title="Error", message="No results to display", parent=self.tab2)
            return
        return suppliers

    def get_devices(self):

        self.tree.delete(*self.tree.get_children())
        db = db_conn()
        cur = db.cursor()

        cur.execute(""" 
                SELECT DEVICE_ID,DEVICE_NAME,DEVICE_DESCRIPTION,DEVICE_SERIAL_NUMBER,SUPPLIER_NAME
                FROM INVENTORY
                join suppliers on inventory.supplier_id = suppliers.supplier_id
                WHERE DEVICE_ID NOT IN 
                (SELECT INVENTORY_DEVICE_ID FROM CUSTOMER_INVENTORY)
                ORDER BY DEVICE_NAME
                """)

        devices = cur.fetchall()
        db.close()

        if devices:
            for device in devices:
                self.tree.insert("", END,
                                 values=(
                                     device[0], device[1], device[2], device[3], device[4]))

        else:
            messagebox.showerror(title="Error", message="No Results to display", parent=self.tab1)
