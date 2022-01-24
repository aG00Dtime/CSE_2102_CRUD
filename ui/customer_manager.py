import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from funcs.connector import db_conn
from funcs.window_position import window_pos

root = os.path.abspath(os.curdir)


# customer window
class CustomerManager(Tk):
    def __init__(self, access_level, username):
        super(CustomerManager, self).__init__()

        self.title("Customers Manager")

        self.geometry(window_pos(1024, 630))

        self.resizable(False, False)

        # window_title
        self.window_title = Label(self, text="Customer Manager", font="ARIAL 16 bold").grid(pady=(20, 20))

        self.user = username
        self.access_level = access_level

        # icon
        self.iconbitmap(os.path.join(root, 'assets', 'icon.ico'))

        # create notebook to hold tabs
        self.tabs = Notebook(self)

        # create tabs
        self.tab1 = Frame(self.tabs)
        self.tab2 = Frame(self.tabs)
        self.tab3 = Frame(self.tabs)
        self.tab4 = Frame(self.tabs)

        # add tabs to notebook with tab names
        self.tabs.add(self.tab1, text="Search Customer Database")
        self.tabs.add(self.tab2, text="Add Customer record")
        self.tabs.add(self.tab3, text="Update Customer record")

        # only admins can delete
        if 'admin' in access_level:
            self.tabs.add(self.tab4, text="Delete Customer record")

        # pack tabs
        self.tabs.grid()

        # query tree view
        self.font_style_large = "arial 18 bold"
        self.font_style_medium = "arial 14 "
        self.font_style_small = "arial 11"

        # TAB 1 ######################################################################################################

        # first name label
        self.f_name_label_tab_1 = Label(self.tab1, text='First Name', font=self.font_style_small).grid(row=0, column=0,
                                                                                                       padx=(180, 2),
                                                                                                       pady=(40, 0),
                                                                                                       sticky=E)

        # first name entry boxes
        self.f_name_entry_tab_1 = Entry(self.tab1, width=50)
        self.f_name_entry_tab_1.grid(row=0, column=1, sticky=W, pady=(40, 0))

        # last name label
        self.l_name_label_tab_1 = Label(self.tab1, text='Last Name', font=self.font_style_small).grid(row=1, column=0,
                                                                                                      padx=2, pady=5,
                                                                                                      sticky=E)

        # first name entry boxes
        self.l_name_entry_tab_1 = Entry(self.tab1, width=50)
        self.l_name_entry_tab_1.grid(row=1, column=1, sticky=W)

        # button
        self.query_button_tab_1 = Button(self.tab1, width=50, text="Search", command=self.db_query).grid(row=2,
                                                                                                         column=1,
                                                                                                         pady=20,
                                                                                                         sticky=W)

        # # enter key
        # self.bind('<Return>', self.db_query)

        #
        self.tree = Treeview(self.tab1, height=15, show='headings')

        # tree position
        self.tree.grid(row=3, column=0, columnspan=4, padx=(10, 0))

        self.scrollbar = Scrollbar(self.tab1, orient="vertical", command=self.tree.yview)

        self.scrollbar.grid(row=3, column=4, sticky="NS")

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        #

        # column headings
        if "admin" in access_level:
            self.tree['columns'] = ("1", "2", "3", "4", '5', '6', '7', '8')
        else:
            self.tree['columns'] = ("1", "2", "3", "4", '5', '6', '7')

        self.tree.heading("1", text="ID")

        self.tree.heading("2", text="First Name")

        self.tree.heading("3", text="Last Name")

        self.tree.heading("4", text="Phone")

        self.tree.heading("5", text="Email")

        self.tree.heading("6", text="Address")

        self.tree.heading("7", text="Plan")

        if "admin" in access_level:
            self.tree.heading("8", text="Modified By")

        # align column data
        if "admin" not in access_level:
            # column width
            self.tree.column('1', width=30)
            self.tree.column('2', width=80)
            self.tree.column('3', width=80)
            self.tree.column('4', width=80)

            for i in range(8):
                self.tree.column(str(i), anchor=W)

            for i in range(5, 8):
                self.tree.column(str(i), width=240)
        else:
            # column width
            self.tree.column('1', width=30)
            self.tree.column('2', width=80)
            self.tree.column('3', width=80)
            self.tree.column('4', width=80)
            self.tree.column('5', width=250)
            self.tree.column('6', width=250)
            self.tree.column('7', width=110)
            self.tree.column('8', width=100)

            for i in range(9):
                self.tree.column(str(i), anchor=W)

        # TAB 2 #######################################################################################################
        # width of entry boxes
        self.entry_width = 50
        # name entry
        self.first_name_label_tab_2 = Label(self.tab2, text="First Name").grid(row=0, column=0, pady=(50, 10),
                                                                               padx=(250, 20),
                                                                               sticky=NW)
        self.first_name_entry_tab_2 = Entry(self.tab2, width=self.entry_width)
        self.first_name_entry_tab_2.grid(row=0, column=1, pady=(50, 10))

        self.last_name_label_tab_2 = Label(self.tab2, text="Last Name").grid(row=1, column=0, pady=10, padx=(250, 20),
                                                                             sticky=NW)
        self.last_name_entry_tab_2 = Entry(self.tab2, width=self.entry_width)
        self.last_name_entry_tab_2.grid(row=1, column=1, pady=10)

        # phone
        self.phone_label_tab_2 = Label(self.tab2, text="Phone").grid(row=2, column=0, pady=10, padx=(250, 20),
                                                                     sticky=NW)
        self.phone_entry_tab_2 = Entry(self.tab2, width=self.entry_width)
        self.phone_entry_tab_2.grid(row=2, column=1, pady=10)

        # email
        self.email_label_tab_2 = Label(self.tab2, text="Email").grid(row=3, column=0, pady=10, padx=(250, 20),
                                                                     sticky=NW)
        self.email_entry_tab_2 = Entry(self.tab2, width=self.entry_width)
        self.email_entry_tab_2.grid(row=3, column=1, pady=10)

        # address1
        self.address1_label_tab_2 = Label(self.tab2, text="Address").grid(row=4, column=0, pady=10, padx=(250, 20),
                                                                          sticky=NW)
        self.address1_entry_tab_2 = Entry(self.tab2, width=self.entry_width)
        self.address1_entry_tab_2.grid(row=4, column=1, pady=10)

        # drop down selection box
        self.customer_plan_label_tab_2 = Label(self.tab2, text="Select Plan").grid(row=7, column=0, pady=10,
                                                                                   padx=(250, 20),
                                                                                   sticky=NW)

        self.customer_plan_tab_2 = Combobox(self.tab2, width=36, state='readonly')

        # query from db instead to values
        self.customer_plan_tab_2['values'] = self.get_plans()

        ##################
        self.customer_plan_tab_2.grid(row=7, column=1, pady=10)

        # submit button
        self.submit_button_tab_2 = Button(self.tab2, width=20, text="Submit", command=self.insert_customer).grid(row=10,
                                                                                                                 column=1)

        # TAB 3 #######################################################################################################

        self.enter_id_label_tab_3 = Label(self.tab3, text="CUSTOMER ID").grid(row=0, column=0,
                                                                              pady=(50, 0), padx=(250, 20),
                                                                              sticky=NW)
        # customer id
        self.id_entry_tab_3 = Entry(self.tab3, width=50)
        self.id_entry_tab_3.grid(row=0, column=1, pady=(50, 0))

        # button
        self.query_button_customer_tab_3 = Button(self.tab3, width=20, text="Search", command=self.update_query).grid(
            row=1,
            column=1, pady=10)

        # entry boxes to insert values
        self.first_name_label_tab_3 = Label(self.tab3, text="First Name").grid(row=2, column=0, pady=(50, 10),
                                                                               padx=(250, 20),
                                                                               sticky=NW)
        # name entry
        self.first_name_entry_tab_3 = Entry(self.tab3, width=self.entry_width)
        self.first_name_entry_tab_3.grid(row=2, column=1, pady=(50, 10))

        self.last_name_label_tab_3 = Label(self.tab3, text="Last Name").grid(row=3, column=0, pady=10, padx=(250, 20),
                                                                             sticky=NW)
        self.last_name_entry_tab_3 = Entry(self.tab3, width=self.entry_width)
        self.last_name_entry_tab_3.grid(row=3, column=1, pady=10)

        # phone
        self.phone_label_tab_3 = Label(self.tab3, text="Phone").grid(row=4, column=0, pady=10, padx=(250, 20),
                                                                     sticky=NW)
        self.phone_entry_tab_3 = Entry(self.tab3, width=self.entry_width)
        self.phone_entry_tab_3.grid(row=4, column=1, pady=10)

        # email
        self.email_label_tab_3 = Label(self.tab3, text="Email").grid(row=5, column=0, pady=10, padx=(250, 20),
                                                                     sticky=NW)
        self.email_entry_tab_3 = Entry(self.tab3, width=self.entry_width)
        self.email_entry_tab_3.grid(row=5, column=1, pady=10)

        # address1
        self.address1_label_tab_3 = Label(self.tab3, text="Address").grid(row=6, column=0, pady=10, padx=(250, 20),
                                                                          sticky=NW)
        self.address1_entry_tab_3 = Entry(self.tab3, width=self.entry_width)
        self.address1_entry_tab_3.grid(row=6, column=1, pady=10)

        # drop down selection box
        self.customer_plan_label_tab_3 = Label(self.tab3, text="Select Plan").grid(row=7, column=0, pady=10,
                                                                                   padx=(250, 20),
                                                                                   sticky=NW)

        self.customer_plan_tab_3 = Combobox(self.tab3, width=36, state='readonly')

        # query from db instead to values
        self.customer_plan_tab_3['values'] = self.get_plans()

        self.customer_plan_tab_3.grid(row=7, column=1, pady=10)

        # submit button
        self.submit_button_tab_3 = Button(self.tab3, width=20, text="Update", command=self.update_record).grid(row=9,
                                                                                                               column=1)

        # TAB 4 #######################################################################################################
        self.enter_id_label_tab_4 = Label(self.tab4, text="CUSTOMER ID").grid(row=0, column=0,
                                                                              pady=(50, 0), padx=(250, 20),
                                                                              sticky=NW)
        # customer id
        self.id_entry_tab_4 = Entry(self.tab4, width=50)
        self.id_entry_tab_4.grid(row=0, column=1, pady=(50, 0))

        # button
        self.delete_button_tab_4 = Button(self.tab4, width=20, text="Search", command=self.delete_record).grid(row=1,
                                                                                                               column=1,
                                                                                                               pady=10)

    # delete a record
    def delete_record(self):

        customer_id = self.id_entry_tab_4.get()

        db = db_conn()
        cur = db.cursor()
        # check if record exists in the database

        cur.execute(
            f'''select customer_first_name,customer_last_name from customers where customer_id = '{customer_id}' ''')
        record_exist = cur.fetchone()

        if record_exist:
            confirm = messagebox.askokcancel(title="DELETE RECORD?", message=record_exist, parent=self.tab4)

            if confirm:
                cur.execute(f'''delete from customers where customer_id='{customer_id}' ''')
                db.commit()

                messagebox.showinfo(message="Record Deleted", parent=self.tab4)
            else:
                messagebox.showinfo(message="Cancelled", parent=self.tab4)

        else:

            messagebox.showerror(message="Record Not Found", parent=self.tab4)
            db.close()

        db.close()

    def update_query(self):
        # get customer id to update
        customer_id = self.id_entry_tab_3.get()

        db = db_conn()
        cur = db.cursor()
        # fetch the record
        cur.execute(
            f'''select * from customer_update where customer_id = '{customer_id}' ''')

        record = cur.fetchone()

        # clear entry boxes before inserting new data
        self.first_name_entry_tab_3.delete(0, END)
        self.last_name_entry_tab_3.delete(0, END)
        self.email_entry_tab_3.delete(0, END)
        self.address1_entry_tab_3.delete(0, END)
        self.phone_entry_tab_3.delete(0, END)
        self.customer_plan_tab_3.set(' ')

        if not record:
            messagebox.showerror(message="Record not found", parent=self.tab3)
            return

        # get the details
        first_name = record[1]
        last_name = record[2]
        tele = record[3]
        email = record[4]
        address = record[5]

        # insert
        self.first_name_entry_tab_3.insert(0, first_name)
        self.last_name_entry_tab_3.insert(0, last_name)
        self.phone_entry_tab_3.insert(0, tele)
        self.email_entry_tab_3.insert(0, email)
        self.address1_entry_tab_3.insert(0, address)
        self.customer_plan_tab_3.set("SELECT PLAN")

    def update_record(self):
        # customer id
        customer_id = self.id_entry_tab_3.get()

        # create error list
        error_list = []

        # name checking
        first = self.first_name_entry_tab_3.get().lower().capitalize()
        last = self.last_name_entry_tab_3.get().lower().capitalize()

        if " " in first or " " in last or not first or not last:
            error_list.append("Names cannot be empty or contain spaces")

        # check plan
        plan = self.customer_plan_tab_3.get()

        if plan == "SELECT PLAN":
            error_list.append("Plan must be selected")

        # grab email
        email = self.email_entry_tab_3.get()

        # crude email validity check
        if not email or "@" not in email or "." not in email:
            error_list.append("Email Address invalid")

        # check phone
        phone = self.phone_entry_tab_3.get()
        number_list = '1234567890'
        number_check = [False for number in phone]

        # if phone is too short or invalid
        if len(phone) <= 10:
            for index, number in enumerate(phone):
                if number in number_list:
                    number_check[index] = True

            if not all(number_check):
                error_list.append("Invalid Phone Number,Number must be 7 digits")
        else:
            error_list.append("Invalid Phone Number,Number must be 7 digits")

        # get list of errors to display

        address1 = self.address1_entry_tab_3.get().lower().capitalize()

        if not address1:
            error_list.append("Ensure Address is filled in")

        if error_list:
            # make list into string
            error_str = '\n'.join(error_list)
            messagebox.showerror(message=error_str, title="ERROR!", parent=self.tab2)

        else:

            plan_str = plan.split(" ")
            plan_id = plan_str[0]

            # SQL HERE ###############################################################################################

            db = db_conn()
            cur = db.cursor()

            cur.execute(f''' 
            update customers set customer_first_name = '{first}',customer_last_name='{last}',customer_telephone='{phone}'
            ,customer_address='{address1}',
            customer_plan='{plan_id}',customer_email='{email}', modified_by = '{self.user}' 
            where customer_id='{customer_id}'
            ''')

            # commit and close db
            db.commit()
            db.close()

            ##########################################################################################################

            # clear entry boxes after record inserted
            self.first_name_entry_tab_3.delete(0, END)
            self.last_name_entry_tab_3.delete(0, END)
            self.email_entry_tab_3.delete(0, END)
            self.address1_entry_tab_3.delete(0, END)
            self.phone_entry_tab_3.delete(0, END)
            self.customer_plan_tab_3.set(' ')

            # show success message
            messagebox.showinfo(title="Success", message="Done.", parent=self.tab3)

    @staticmethod
    def get_plans():
        """GET LIST OF AVAILABLE PLANS"""

        # connect to db and fetch plans available
        db = db_conn()
        cur = db.cursor()

        cur.execute(''' SELECT plan_id , plan_name ,plan_burst_speed FROM plans ''')

        plans = cur.fetchall()

        db.close()

        # return plans pulled from db
        return plans

    # query func
    def db_query(self):
        """SEARCH DATABASE"""

        # connect to db
        db = db_conn()
        cur = db.cursor()

        # clear out tree view
        self.tree.delete(*self.tree.get_children())

        f_name = self.f_name_entry_tab_1.get().lower().capitalize()
        l_name = self.l_name_entry_tab_1.get().lower().capitalize()

        # sql
        #######################################################################################################

        cur.execute(
            f'''
            select * from customer_details 
            where customer_first_name ='{f_name}' 
            and 
            customer_last_name ='{l_name}' 
            
                ''')

        #######################################################################################################
        # get
        rows = cur.fetchall()

        # check if any results were returned
        if not rows:
            messagebox.showerror(message="No results", title="Error", parent=self.tab1)
            return

        # add data the tree
        for column in rows:
            if "admin" not in self.access_level:
                self.tree.insert("", END,
                                 values=(
                                     column[0], column[1], column[2], column[3], column[4], column[5], column[6]))
            else:
                self.tree.insert("", END,
                                 values=(
                                     column[0], column[1], column[2], column[3], column[4], column[5], column[6],
                                     column[7]))

        db.close()

    # submit
    def insert_customer(self):

        """INSERT CUSTOMER DETAILS"""

        # error list
        error_list = []

        # name checking
        first = self.first_name_entry_tab_2.get().lower().capitalize()
        last = self.last_name_entry_tab_2.get().lower().capitalize()

        if " " in first or " " in last or not first or not last:
            error_list.append("Names cannot be empty or contain spaces")

        # check
        plan = self.customer_plan_tab_2.get()

        # check plan
        if not plan:
            error_list.append("Plan must be selected")

        # check email
        email = self.email_entry_tab_2.get()

        # crude email validity check
        if not email or "@" not in email or "." not in email:
            error_list.append("Email Address invalid")

        # check phone
        phone = self.phone_entry_tab_2.get()
        number_list = '1234567890'
        number_check = [False for number in phone]

        # if phone is too short or invalid
        if len(phone) <= 10:
            for index, number in enumerate(phone):
                if number in number_list:
                    number_check[index] = True

            if not all(number_check):
                error_list.append("Invalid Phone Number")
        else:
            error_list.append("Invalid Phone Number")

        # get list of errors to display

        address1 = self.address1_entry_tab_2.get().lower().capitalize()

        if not address1:
            error_list.append("Ensure Address is filled in")

        if error_list:
            # make list into string
            error_str = '\n'.join(error_list)

            messagebox.showerror(message=error_str, title="ERROR!", parent=self.tab2)

        else:

            plan_str = plan.split(" ")

            plan_id = plan_str[0]

            # sql here #####################################################
            db = db_conn()
            cur = db.cursor()

            cur.execute(f''' insert into customers (customer_first_name,customer_last_name,customer_telephone,
            customer_email,customer_address ,customer_plan,modified_by) values ('{first}','{last}','{phone}',
            '{email}','{address1}','{plan_id}','{self.user}') 
                ''')

            # commit and close db
            db.commit()
            db.close()

            ##################################################################

            # clear entry boxes after record inserted
            self.first_name_entry_tab_2.delete(0, END)
            self.last_name_entry_tab_2.delete(0, END)
            self.email_entry_tab_2.delete(0, END)
            self.address1_entry_tab_2.delete(0, END)
            self.phone_entry_tab_2.delete(0, END)
            self.customer_plan_tab_2.set(' ')

            # show success message
            messagebox.showinfo(title="Success", message="Done.", parent=self.tab2)
