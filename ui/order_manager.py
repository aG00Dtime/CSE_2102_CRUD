import os
from fpdf import FPDF

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from funcs.connector import db_conn
from funcs.window_position import window_pos
from tkinter.filedialog import askdirectory

root = os.path.abspath(os.curdir)


class OrderManager(Tk):
    def __init__(self, access_level, username):
        super(OrderManager, self).__init__()

        self.title("Order Manager")

        self.geometry(window_pos(750, 600))
        self.resizable(False, False)

        self.user = username
        self.access_level = access_level

        # icon
        self.iconbitmap(os.path.join(root, 'assets', 'icon.ico'))

        self.window_title = Label(self, text="Order Manager", font="ARIAL 16 bold").grid(pady=(20, 20))

        # tabs

        self.tabs = Notebook(self)

        self.tab1 = Frame(self.tabs)
        self.tab2 = Frame(self.tabs)
        self.tab3 = Frame(self.tabs)
        self.tab4 = Frame(self.tabs)

        self.tabs.add(self.tab1, text="Customer Order List")
        self.tabs.add(self.tab2, text="Add New Orders")
        self.tabs.add(self.tab3, text="Delete Orders")
        self.tabs.add(self.tab4, text="Create Invoice")

        self.tabs.grid()
        self.view_orders_button = Button(self.tab1, text="View Customer Order List", width=40, command=self.get_orders)
        self.view_orders_button.grid(pady=(30, 20), padx=(200, 0))

        self.tree = Treeview(self.tab1, height=15, show='headings')

        # tree
        self.tree.grid(row=3, column=0, columnspan=4, padx=(10, 0))

        self.scrollbar = Scrollbar(self.tab1, orient="vertical", command=self.tree.yview)

        self.scrollbar.grid(row=3, column=4, sticky="NS")

        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.tree['columns'] = ("1", "2", "3", "4", "5", "6")
        self.tree.heading("1", text="ID")
        self.tree.heading("2", text="Customer")
        self.tree.heading("3", text="Plan")
        self.tree.heading("4", text="Plan Speed")
        self.tree.heading("5", text="Plan Cost")
        self.tree.heading("6", text="Quotation")

        self.tree.column("1", anchor=E, width=50)

        for i in range(2, 7):
            self.tree.column(str(i), width=132, anchor=CENTER)

        # tab 2 ####################################################################################################
        # add orders
        self.customer_id_label_tab_2 = Label(self.tab2, text="Customer ID").grid(row=0, column=0, pady=20,
                                                                                 padx=(200, 0))
        self.customer_id_tab_2 = Entry(self.tab2, width=40)
        self.customer_id_tab_2.grid(row=0, column=1)
        # quot
        self.customer_quotation_tab_2 = Label(self.tab2, text="Quotation").grid(row=1, column=0, padx=(200, 0))
        self.customer_quotation_tab_2_entry = Entry(self.tab2, width=40)
        self.customer_quotation_tab_2_entry.grid(row=1, column=1)

        # button
        self.submit_button_tab_2 = Button(self.tab2, text="Submit", width=40, command=self.add_orders)
        self.submit_button_tab_2.grid(row=2, column=1, pady=20)

        # tab 3 ######################################################################################################

        # delete orders
        self.order_id = Label(self.tab3, text="Order ID").grid(row=0, column=0, pady=20,
                                                               padx=(200, 0))
        self.order_id_entry_tab3 = Entry(self.tab3, width=40)
        self.order_id_entry_tab3.grid(row=0, column=1)

        # button
        self.submit_button_tab_3 = Button(self.tab3, text="Delete", width=40, command=self.delete_orders)
        self.submit_button_tab_3.grid(row=2, column=1)

        # tab 4 create invoice
        self.order_id = Label(self.tab4, text="Order ID").grid(row=0, column=0, pady=20,
                                                               padx=(200, 0))
        self.order_id_entry_tab4 = Entry(self.tab4, width=40)
        self.order_id_entry_tab4.grid(row=0, column=1)

        # button
        self.submit_button_tab_4 = Button(self.tab4, text="Create Invoice", width=40, command=self.create_invoice)
        self.submit_button_tab_4.grid(row=2, column=1)

    def create_invoice(self):

        order_id = self.order_id_entry_tab4.get()

        db = db_conn()
        cur = db.cursor()
        cur.execute(F'''
        SELECT * FROM CUSTOMER_ORDERS WHERE ORDER_ID = '{order_id}'

        ''')

        order = cur.fetchone()

        db.close()

        print(order)

        if not order:
            messagebox.showerror(message="Order not found", title="Error", parent=self.tab4)
            return

        customer_name = f'''{order[1]} {order[2]}'''
        plan = order[3]




        # create invoice
        pdf = FPDF('P', 'mm', 'Letter')
        pdf.add_page()
        pdf.set_font('helvetica', '', 18)

        pdf.cell(200, 20, "SMJ", ln=1, align="C")
        pdf.cell(200, 20, customer_name, ln=1, align="l")
        pdf.cell(200, 20, plan, ln=1, align="l")

        save_dir = askdirectory()

        save_path = os.path.join(save_dir, "test.pdf")

        if save_path:
            pdf.output(save_path)

        messagebox.showinfo(title="Done", message="Invoice Created", parent=self.tab4)

    def delete_orders(self):

        order_id = self.order_id_entry_tab3.get()

        db = db_conn()
        cur = db.cursor()

        # CHECK IF ORDER ID EXISTS
        cur.execute(F""" SELECT * FROM CUSTOMER_ORDERS WHERE ORDER_ID ='{order_id}' """)

        order = cur.fetchone()

        if not order:
            messagebox.showerror(title="Error", message="Invalid Order ID", parent=self.tab3)
            db.close()
            return

        # DELETE ORDER
        cur.execute(f"""DELETE FROM ORDERS WHERE ORDER_ID ='{order_id}' """)
        db.commit()
        db.close()

        messagebox.showinfo(title="Success", message="Removed Order", parent=self.tab3)

    def get_orders(self):

        # clear out tree view
        self.tree.delete(*self.tree.get_children())

        # connect
        db = db_conn()

        cur = db.cursor()

        sql = "SELECT * FROM CUSTOMER_ORDERS ORDER BY ORDER_ID "

        cur.execute(sql)

        orders = cur.fetchall()

        db.close()

        if not orders:
            messagebox.showerror(title="Error", message="No results", parent=self.tab1)
            return

        for order in orders:
            customer_name = f'''{order[1]} {order[2]}'''

            self.tree.insert("", END,
                             values=(
                                 order[0], customer_name, order[3], order[4], order[5], order[6])
                             )

    def add_orders(self):

        customer_id = self.customer_id_tab_2.get()
        quotation_estimate = self.customer_quotation_tab_2_entry.get()
        new_quotation_estimate = ''

        db = db_conn()
        cur = db.cursor()

        cur.execute(F"""SELECT * FROM CUSTOMERS WHERE CUSTOMER_ID ='{customer_id}' """)

        customer = cur.fetchone()

        if not customer:
            messagebox.showerror(title="Error", message="Invalid Customer ID", parent=self.tab2)
            return

        if not customer_id or not quotation_estimate:
            messagebox.showerror(title="Error", message="Ensure All fields are correct", parent=self.tab2)
            return

        for char in quotation_estimate:
            if char.isalnum():
                new_quotation_estimate += char

        new_quotation_estimate = "${:,.2f}".format(int(new_quotation_estimate))

        cur.execute(f''' 
        INSERT INTO ORDERS (ORDER_CUSTOMER_ID,ORDER_QUOTATION)
        VALUES ('{customer_id}','{new_quotation_estimate}')
        ''')

        self.customer_quotation_tab_2_entry.delete(0, END)
        self.customer_id_tab_2.delete(0, END)

        messagebox.showinfo(title="Order Created", message="Done", parent=self.tab2)

        db.commit()
        db.close()
