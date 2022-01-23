import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from funcs.connector import db_conn
from funcs.window_position import window_pos

root = os.path.abspath(os.curdir)


class SupplierManager(Tk):
    def __init__(self, access_level, username):
        super(SupplierManager, self).__init__()

        self.title("Supplier Manager")
        self.geometry(window_pos(850, 500))
        self.resizable(False, False)

        # current user
        self.user = username
        self.access_level = access_level

        # icon
        self.iconbitmap(os.path.join(root, 'assets', 'icon.ico'))

        # window_title
        self.window_title = Label(self, text="Supplier Manager", font="ARIAL 16 bold").grid(pady=(20, 20))

        # create notebook to hold tabs
        self.tabs = Notebook(self)

        self.tab1 = Frame(self.tabs)
        self.tab2 = Frame(self.tabs)
        self.tab3 = Frame(self.tabs)
        self.tab4 = Frame(self.tabs)

        self.tabs.add(self.tab1, text="Supplier List")
        self.tabs.add(self.tab2, text="Add Supplier")
        self.tabs.add(self.tab3, text="Update Supplier")

        # self.tabs.add(self.tab4, text="Delete Supplier")

        self.tabs.grid()

        # TAB 1 ####################################################################################

        self.view_supplier_button = Button(self.tab1, text="View Supplier List", width=40,
                                           command=self.query_suppliers).grid(padx=(130, 0), pady=20,
                                                                              row=0,
                                                                              column=1)

        # tree position
        self.tree = Treeview(self.tab1, height=15, show='headings')

        # scrollbar
        self.scrollbar = Scrollbar(self.tab1, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=3, column=4, sticky="NS")

        # conf columns
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.tree['columns'] = ("1", "2", "3", "4", "5")
        self.tree.heading("1", text="ID")
        self.tree.heading("2", text="Name")
        self.tree.heading("3", text="Address")
        self.tree.heading("4", text="Email")
        self.tree.heading("5", text="Telephone")

        # width
        self.tree.column('1', width=30)
        self.tree.column('2', width=180)
        self.tree.column('3', width=200)
        self.tree.column('4', width=200)
        self.tree.column('5', width=200)

        # center tree data
        for i in range(6):
            self.tree.column(str(i), anchor=E)

        self.tree.grid(row=3, column=0, columnspan=4, padx=(10, 0))

        # tab 2 ##################################################################################

        # name
        self.entry_box_width = 40
        self.supplier_name_tab_2 = Label(self.tab2, text="Name").grid(row=0, column=0, pady=(50, 5), padx=(240, 20))
        self.supplier_name_entry_tab_2 = Entry(self.tab2, width=self.entry_box_width)
        self.supplier_name_entry_tab_2.grid(row=0, column=1, pady=(50, 5))

        # address
        self.supplier_address_tab_2 = Label(self.tab2, text="Address").grid(row=1, column=0, pady=(5, 5),
                                                                            padx=(240, 20))
        self.supplier_address_entry_tab_2 = Entry(self.tab2, width=self.entry_box_width)
        self.supplier_address_entry_tab_2.grid(row=1, column=1, pady=5)

        # email
        self.supplier_email_tab_2 = Label(self.tab2, text="Email").grid(row=2, column=0, pady=(5, 5), padx=(240, 20))
        self.supplier_email_entry_tab_2 = Entry(self.tab2, width=self.entry_box_width)
        self.supplier_email_entry_tab_2.grid(row=2, column=1, pady=5)

        # telephone
        self.supplier_telephone_tab_2 = Label(self.tab2, text="Telephone").grid(row=3, column=0, pady=(5, 5),
                                                                                padx=(240, 20))
        self.supplier_telephone_entry_tab_2 = Entry(self.tab2, width=self.entry_box_width)
        self.supplier_telephone_entry_tab_2.grid(row=3, column=1, pady=5)

        # button
        self.submit_button_tab_2 = Button(self.tab2, text="Submit", width=self.entry_box_width,
                                          command=self.insert_supplier)
        self.submit_button_tab_2.grid(row=4, column=1, pady=20)

        # tab 3 ##################################################################################
        self.supplier_id_label = Label(self.tab3, text="Supplier ID").grid(row=0, column=0, pady=(50, 5),
                                                                           padx=(240, 20))
        self.supplier_id_entry_tab_3 = Entry(self.tab3, width=self.entry_box_width)
        self.supplier_id_entry_tab_3.grid(row=0, column=1, pady=(50, 5))
        self.search_supplier_button = Button(self.tab3, text="Search", command=self.update_query)
        self.search_supplier_button.grid(row=1, column=1)

        # name
        self.supplier_name_tab_3 = Label(self.tab3, text="Name").grid(row=2, column=0, pady=(30, 5), padx=(240, 20))
        self.supplier_name_entry_tab_3 = Entry(self.tab3, width=self.entry_box_width)
        self.supplier_name_entry_tab_3.grid(row=2, column=1, pady=(30, 5))

        # address
        self.supplier_address_tab_3 = Label(self.tab3, text="Address").grid(row=3, column=0, pady=(5, 5),
                                                                            padx=(240, 20))
        self.supplier_address_entry_tab_3 = Entry(self.tab3, width=self.entry_box_width)
        self.supplier_address_entry_tab_3.grid(row=3, column=1, pady=5)

        # email
        self.supplier_email_tab_3 = Label(self.tab3, text="Email").grid(row=4, column=0, pady=(5, 5), padx=(240, 20))
        self.supplier_email_entry_tab_3 = Entry(self.tab3, width=self.entry_box_width)
        self.supplier_email_entry_tab_3.grid(row=4, column=1, pady=5)

        # telephone
        self.supplier_telephone_tab_3 = Label(self.tab3, text="Telephone").grid(row=5, column=0, pady=(5, 5),
                                                                                padx=(240, 20))
        self.supplier_telephone_entry_tab_3 = Entry(self.tab3, width=self.entry_box_width)
        self.supplier_telephone_entry_tab_3.grid(row=5, column=1, pady=5)

        # button
        self.submit_button_tab_3 = Button(self.tab3, text="Submit", width=self.entry_box_width,
                                          command=self.update_supplier)
        self.submit_button_tab_3.grid(row=6, column=1, pady=20)

        # # tab 4 ####################################################################################
        #
        # self.supplier_id_label = Label(self.tab4, text="Supplier ID").grid(row=0, column=0, pady=(50, 5),
        #                                                                    padx=(240, 20))
        # self.supplier_id_entry_tab_4 = Entry(self.tab4, width=self.entry_box_width)
        # self.supplier_id_entry_tab_4.grid(row=0, column=1, pady=(50, 5))
        # self.search_supplier_button_tab_4 = Button(self.tab4, text="Remove", command=self.delete_supplier)
        # self.search_supplier_button_tab_4.grid(row=1, column=1)

    # # delete record
    # def delete_supplier(self):
    #     supplier_id = self.supplier_id_entry_tab_4.get()
    #
    #     if not supplier_id:
    #         messagebox.showerror(title="Error", message="Enter ID", parent=self.tab4)
    #         return
    #
    #     db = db_conn()
    #     cur = db.cursor()
    #
    #     # SQL
    #     cur.execute(F""" SELECT SUPPLIER_NAME FROM SUPPLIERS WHERE SUPPLIER_ID = '{supplier_id}' """)
    #
    #     results = cur.fetchone()
    #
    #     if not results:
    #         messagebox.showerror(title="!", message="Supplier not found", parent=self.tab4)
    #         return
    #
    #     confirm_delete = messagebox.askyesno(message=f"Delete record for {results[0]} ?", parent=self.tab4)
    #
    #     if confirm_delete:
    #         # SQL
    #         cur.execute(f""" DELETE FROM SUPPLIERS WHERE SUPPLIER_ID = '{supplier_id}' """)
    #         db.commit()
    #         messagebox.showinfo(message="Deleted record.", title="Done", parent=self.tab4)
    #
    #     else:
    #         messagebox.showinfo(message="Cancelled", title="Cancelled", parent=self.tab4)
    #
    #     # close
    #     db.close()

    # update record
    def update_supplier(self):
        name = self.supplier_name_entry_tab_3.get().lower().capitalize()
        address = self.supplier_address_entry_tab_3.get().lower().capitalize()
        email = self.supplier_email_entry_tab_3.get().lower()
        telephone = self.supplier_telephone_entry_tab_3.get()
        supplier_id = self.supplier_id_entry_tab_3.get()

        error_list = []

        if not name:
            error_list.append("Check Supplier Name Field")

        if not address:
            error_list.append("Check Supplier Address Field")

        if not email:
            error_list.append("Check Supplier Email Field")

        number_list = '1234567890'
        number_check = [False for number in telephone]

        # if phone is too short or invalid
        if len(telephone) <= 10:
            for index, number in enumerate(telephone):
                if number in number_list:
                    number_check[index] = True

            if not all(number_check):
                error_list.append("Check Telephone Number")
        else:
            error_list.append("Check Telephone Number")
        # check errors
        if error_list:
            # make list into string
            error_str = '\n'.join(error_list)

            messagebox.showerror(message=error_str, title="ERROR!", parent=self.tab2)

        else:
            # db conn
            db = db_conn()
            cur = db.cursor()

            cur.execute(f'''
                    UPDATE SUPPLIERS
                    SET SUPPLIER_NAME = '{name}',
                    SUPPLIER_ADDRESS = '{address}',
                    SUPPLIER_EMAIL = '{email}',
                    SUPPLIER_TELEPHONE = '{telephone}'
                    WHERE SUPPLIER_ID = '{supplier_id}'
                    
                    
                    ''')
            # commit and close db connection
            db.commit()
            db.close()

            self.supplier_address_entry_tab_3.delete(0, END)
            self.supplier_name_entry_tab_3.delete(0, END)
            self.supplier_email_entry_tab_3.delete(0, END)
            self.supplier_telephone_entry_tab_3.delete(0, END)

            # success message
            messagebox.showinfo(title="Success", message="Added Supplier Information", parent=self.tab2)

    # get supplier info to update
    def update_query(self):
        supplier_id = self.supplier_id_entry_tab_3.get()

        if not supplier_id:
            messagebox.showerror(title="!", message="Enter ID", parent=self.tab3)
            return

        db = db_conn()
        cur = db.cursor()

        cur.execute(f'''
        SELECT 
        SUPPLIER_NAME,
        SUPPLIER_ADDRESS,
        SUPPLIER_EMAIL,
        SUPPLIER_TELEPHONE
        FROM SUPPLIERS WHERE SUPPLIER_ID = "{supplier_id}"
        ''')

        data = cur.fetchone()

        # clear boxes
        self.supplier_address_entry_tab_3.delete(0, END)
        self.supplier_name_entry_tab_3.delete(0, END)
        self.supplier_email_entry_tab_3.delete(0, END)
        self.supplier_telephone_entry_tab_3.delete(0, END)

        if not data:
            messagebox.showerror(title="!", message="No Results", parent=self.tab3)
            return

        # insert
        self.supplier_name_entry_tab_3.insert(0, data[0])
        self.supplier_address_entry_tab_3.insert(0, data[1])
        self.supplier_email_entry_tab_3.insert(0, data[2])
        self.supplier_telephone_entry_tab_3.insert(0, data[3])

        db.close()

    # insert supplier info
    def insert_supplier(self):
        """INSERT SUPPLIER INFORMATION"""

        name = self.supplier_name_entry_tab_2.get().lower().capitalize()
        address = self.supplier_address_entry_tab_2.get().lower().capitalize()
        email = self.supplier_email_entry_tab_2.get().lower()
        telephone = self.supplier_telephone_entry_tab_2.get()

        error_list = []

        if not name:
            error_list.append("Check Supplier Name Field")

        if not address:
            error_list.append("Check Supplier Address Field")

        if not email:
            error_list.append("Check Supplier Email Field")

        number_list = '1234567890'
        number_check = [False for number in telephone]

        # if phone is too short or invalid
        if len(telephone) <= 10:
            for index, number in enumerate(telephone):
                if number in number_list:
                    number_check[index] = True

            if not all(number_check):
                error_list.append("Check Telephone Number")
        else:
            error_list.append("Check Telephone Number")
        # check errors
        if error_list:
            # make list into string
            error_str = '\n'.join(error_list)

            messagebox.showerror(message=error_str, title="ERROR!", parent=self.tab2)

        else:
            # db conn
            db = db_conn()
            cur = db.cursor()

            cur.execute(f'''
            INSERT INTO SUPPLIERS(
            SUPPLIER_NAME,
            SUPPLIER_ADDRESS,
            SUPPLIER_EMAIL,
            SUPPLIER_TELEPHONE
            )
            VALUES(
            '{name}',
            '{address}',
            '{email}',
            '{telephone}')
            ''')
            # commit and close db connection
            db.commit()
            db.close()

            # clear
            self.supplier_address_entry_tab_2.delete(0, END)
            self.supplier_name_entry_tab_2.delete(0, END)
            self.supplier_email_entry_tab_2.delete(0, END)
            self.supplier_telephone_entry_tab_2.delete(0, END)

            # success message
            messagebox.showinfo(title="Success", message="Added Supplier Information", parent=self.tab2)

    # query supplier table
    def query_suppliers(self):
        """QUERY SUPPLIERS TABLE"""

        # connect to db
        db = db_conn()
        cur = db.cursor()

        # SQL
        cur.execute('''SELECT * FROM SUPPLIERS''')

        # fetch data
        data = cur.fetchall()
        db.close()

        # check
        if not data:
            messagebox.showerror(message="Table empty", title="ERROR")

        # close connection
        else:
            # clear out tree view
            self.tree.delete(*self.tree.get_children())

            # insert data
            for column in data:
                self.tree.insert("", END,
                                 values=(
                                     column[0], column[1], column[2], column[3], column[4]))
