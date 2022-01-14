from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from funcs.connector import db_conn
from funcs.window_position import window_pos


class CustomerManager(Tk):
    def __init__(self, access_level):
        super(CustomerManager, self).__init__()

        self.title("Customers Manager")
        self.geometry(window_pos(1050, 600))
        self.resizable(False, False)

        # create notebook to hold tabs
        self.tabs = Notebook(self)

        # create tabs
        self.tab1 = Frame(self.tabs)
        self.tab2 = Frame(self.tabs)
        self.tab3 = Frame(self.tabs)
        self.tab4 = Frame(self.tabs)

        # add tabs to notebook with tab names
        self.tabs.add(self.tab1, text="Query Customer Database")
        self.tabs.add(self.tab2, text="Add Customer record")
        self.tabs.add(self.tab3, text="Update Customer record")
        self.tabs.add(self.tab4, text="Delete Customer record")

        self.tabs.grid()

        # query tree view
        self.font_style_large = "arial 20 bold"
        self.font_style_medium = "arial 18 bold"
        self.font_style_small = "arial 14"

        # name labels
        self.f_name_label = Label(self.tab1, text='First Name', font=self.font_style_small).grid(row=0, column=0,
                                                                                                 sticky="W",
                                                                                                 padx=(18, 0),
                                                                                                 pady=(50, 10))
        # entry boxes
        self.f_name_entry = Entry(self.tab1, width=50)
        self.f_name_entry.grid(row=0, column=1, columnspan=2, sticky="W", pady=(50, 10), padx=0)
        # name labels
        self.l_name_label = Label(self.tab1, text='Last Name', font=self.font_style_small).grid(row=1, column=0,
                                                                                                sticky="W",
                                                                                                padx=(18, 0))
        # entry boxes
        self.l_name_entry = Entry(self.tab1, width=50)
        self.l_name_entry.grid(row=1, column=1, sticky="NW")

        # button
        self.query_button = Button(self.tab1, width=50, text="Search", command=self.db_query).grid(row=2, column=1,
                                                                                                   columnspan=4,
                                                                                                   sticky="NW",
                                                                                                   pady=(10, 50))
        #
        self.tree = Treeview(self.tab1, height=15, show='headings')

        # tree position
        self.tree.grid(row=3, column=0, columnspan=4, padx=(18, 0))

        self.scrollbar = Scrollbar(self.tab1, orient="vertical", command=self.tree.yview)

        self.scrollbar.grid(row=3, column=4, sticky="NS")

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # column headings
        self.tree['columns'] = ("1", "2", "3", "4", '5', '6', '7')

        self.tree.heading("1", text="ID")

        self.tree.heading("2", text="First Name")

        self.tree.heading("3", text="Last Name")

        self.tree.heading("4", text="Phone")

        self.tree.heading("5", text="Email")

        self.tree.heading("6", text="Address")

        self.tree.heading("7", text="Plan")

        # align column data
        for i in range(8):
            self.tree.column(str(i), anchor="center")

        # column width
        self.tree.column('1', width=40)
        self.tree.column('2', width=80)
        self.tree.column('3', width=80)

        # TAB 2 #######################################################################################################
        # width of entry boxes
        self.entry_width = 50
        # name entry
        self.first_name_label = Label(self.tab2, text="First Name").grid(row=0, column=0, pady=(50, 10), padx=(300, 20),
                                                                         sticky=NW)
        self.first_name_entry = Entry(self.tab2, width=self.entry_width)
        self.first_name_entry.grid(row=0, column=1, pady=(50, 10))

        self.last_name_label = Label(self.tab2, text="Last Name").grid(row=1, column=0, pady=10, padx=(300, 20),
                                                                       sticky=NW)
        self.last_name_entry = Entry(self.tab2, width=self.entry_width)
        self.last_name_entry.grid(row=1, column=1, pady=10)

        # phone
        self.phone_label = Label(self.tab2, text="Phone").grid(row=2, column=0, pady=10, padx=(300, 20), sticky=NW)
        self.phone_entry = Entry(self.tab2, width=self.entry_width)
        self.phone_entry.grid(row=2, column=1, pady=10)

        # email
        self.email_label = Label(self.tab2, text="Email").grid(row=3, column=0, pady=10, padx=(300, 20), sticky=NW)
        self.email_entry = Entry(self.tab2, width=self.entry_width)
        self.email_entry.grid(row=3, column=1, pady=10)

        # address1
        self.address1_label = Label(self.tab2, text="Address").grid(row=4, column=0, pady=10, padx=(300, 20), sticky=NW)
        self.address1_entry = Entry(self.tab2, width=self.entry_width)
        self.address1_entry.grid(row=4, column=1, pady=10)

        # drop down selection box
        self.customer_plan_label = Label(self.tab2, text="Select Plan").grid(row=7, column=0, pady=10, padx=(300, 20),
                                                                             sticky=NW)

        self.customer_plan = Combobox(self.tab2, width=36, state='readonly')

        # query from db instead to values
        self.customer_plan['values'] = self.db_get_plans()

        self.customer_plan.grid(row=7, column=1, pady=10)

        # submit button
        self.submit = Button(self.tab2, width=20, text="Submit", command=self.submit_details).grid(row=8, column=1)

        # TAB 3 #######################################################################################################

        self.enter_id_label = Label(self.tab3, text="CUSTOMER ID").grid(row=0, column=0,
                                                                        pady=(50, 0), padx=(300, 20),
                                                                        sticky=NW)
        # customer id
        self.id_entry = Entry(self.tab3, width=50)
        self.id_entry.grid(row=0, column=1, pady=(50, 0))

        # button
        self.query_button_customer = Button(self.tab3, width=20, text="Search", command=self.update_query).grid(row=1,
                                                                                                                column=1)

        # entry boxes to insert values
        self.first_name_label_2 = Label(self.tab3, text="First Name").grid(row=2, column=0, pady=(50, 10),
                                                                           padx=(300, 20),
                                                                           sticky=NW)
        # name entry
        self.first_name_entry_2 = Entry(self.tab3, width=self.entry_width)
        self.first_name_entry_2.grid(row=2, column=1, pady=(50, 10))

        self.last_name_label_2 = Label(self.tab3, text="Last Name").grid(row=3, column=0, pady=10, padx=(300, 20),
                                                                         sticky=NW)
        self.last_name_entry_2 = Entry(self.tab3, width=self.entry_width)
        self.last_name_entry_2.grid(row=3, column=1, pady=10)

        # phone
        self.phone_label_2 = Label(self.tab3, text="Phone").grid(row=4, column=0, pady=10, padx=(300, 20), sticky=NW)
        self.phone_entry_2 = Entry(self.tab3, width=self.entry_width)
        self.phone_entry_2.grid(row=4, column=1, pady=10)

        # email
        self.email_label_2 = Label(self.tab3, text="Email").grid(row=5, column=0, pady=10, padx=(300, 20), sticky=NW)
        self.email_entry_2 = Entry(self.tab3, width=self.entry_width)
        self.email_entry_2.grid(row=5, column=1, pady=10)

        # address1
        self.address1_label_2 = Label(self.tab3, text="Address").grid(row=6, column=0, pady=10, padx=(300, 20),
                                                                      sticky=NW)
        self.address1_entry_2 = Entry(self.tab3, width=self.entry_width)
        self.address1_entry_2.grid(row=6, column=1, pady=10)

        # drop down selection box
        self.customer_plan_label_2 = Label(self.tab3, text="Select Plan").grid(row=7, column=0, pady=10, padx=(300, 20),
                                                                               sticky=NW)

        self.customer_plan_2 = Combobox(self.tab3, width=36, state='readonly')

        # query from db instead to values
        self.customer_plan_2['values'] = self.db_get_plans()

        self.customer_plan_2.grid(row=7, column=1, pady=10)

        # submit button
        self.submit_2 = Button(self.tab3, width=20, text="Update", command=self.update_record).grid(row=8, column=1)

        # TAB 4 #######################################################################################################
        self.enter_id_label_2 = Label(self.tab4, text="CUSTOMER ID").grid(row=0, column=0,
                                                                          pady=(50, 0), padx=(300, 20),
                                                                          sticky=NW)
        # customer id
        self.id_entry_2 = Entry(self.tab4, width=50)
        self.id_entry_2.grid(row=0, column=1, pady=(50, 0))

        # button
        self.delete_button = Button(self.tab4, width=20, text="Search", command=self.delete_record).grid(row=1,
                                                                                                         column=1)

    # delete a record
    def delete_record(self):

        customer_id = self.id_entry_2.get()

        db = db_conn()
        cur = db.cursor()
        # check if record exists in the database

        cur.execute(f'''select first_name,last_name from customers where customer_id = '{customer_id}' ''')
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
        customer_id = self.id_entry.get()

        db = db_conn()
        cur = db.cursor()
        # fetch the record
        cur.execute(
            f'''select first_name,last_name,telephone,email,address,plan_id from customers where customer_id= 
            '{customer_id}' ''')

        record = cur.fetchone()

        if not record:
            messagebox.showerror(message="Record not found", parent=self.tab3)
            return

        # get the details
        first_name = record[0]
        last_name = record[1]
        tele = record[2]
        email = record[3]
        address = record[4]
        # -1 to set the right id
        plan_id = int(record[5]) - 1

        # clear entry boxes before inserting new data
        self.first_name_entry_2.delete(0, END)
        self.last_name_entry_2.delete(0, END)
        self.email_entry_2.delete(0, END)
        self.address1_entry_2.delete(0, END)
        self.phone_entry_2.delete(0, END)
        self.customer_plan_2.set(' ')

        # insert
        self.first_name_entry_2.insert(0, first_name)
        self.last_name_entry_2.insert(0, last_name)
        self.phone_entry_2.insert(0, tele)
        self.email_entry_2.insert(0, email)
        self.address1_entry_2.insert(0, address)
        self.customer_plan_2.current(plan_id)

    def update_record(self):
        customer_id = self.id_entry.get()
        error_list = []

        # name checking
        first = self.first_name_entry_2.get().lower().capitalize()
        last = self.last_name_entry_2.get().lower().capitalize()

        if " " in first or " " in last or not first or not last:
            error_list.append("Names cannot be empty or contain spaces")

        # check plan
        plan = self.customer_plan_2.get()
        if not plan:
            error_list.append("Plan must be selected")

        # check email
        email = self.email_entry_2.get()
        if not email:
            error_list.append("Email Address missing")

        # check phone
        phone = self.phone_entry_2.get()
        number_list = '1234567890'
        number_check = [False for number in phone]

        # if phone is too short or invalid
        if len(phone) == 7:
            for index, number in enumerate(phone):
                if number in number_list:
                    number_check[index] = True

            if not all(number_check):
                error_list.append("Invalid Phone Number")
        else:
            error_list.append("Invalid Phone Number")

        # get list of errors to display

        address1 = self.address1_entry_2.get().lower().capitalize()

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

            cur.execute(f''' 
            
            update customers set first_name = '{first}',last_name='{last}',telephone='{phone}',address='{address1}',
            plan_id='{plan_id}',email='{email}' where customer_id='{customer_id}'



            ''')
            # commit and close db
            db.commit()
            db.close()

            ##################################################################

            # clear entry boxes after record inserted
            self.first_name_entry_2.delete(0, END)
            self.last_name_entry_2.delete(0, END)
            self.email_entry_2.delete(0, END)
            self.address1_entry_2.delete(0, END)
            self.phone_entry_2.delete(0, END)
            self.customer_plan_2.set(' ')

            # show success message
            messagebox.showinfo(title="Success", message="Done.", parent=self.tab3)

    @staticmethod
    def db_get_plans():
        # connect to db and fetch plans available
        db = db_conn()
        cur = db.cursor()
        cur.execute(''' SELECT id,plan_name,plan_speed FROM plan ''')

        plans = cur.fetchall()

        db.close()

        # return plans pulled from db
        return plans

    # query func
    def db_query(self):

        # connect to db
        db = db_conn()
        cur = db.cursor()

        # clear out tree view
        self.tree.delete(*self.tree.get_children())

        f_name = self.f_name_entry.get().lower().capitalize()
        l_name = self.l_name_entry.get().lower().capitalize()

        # sql
        #######################################################################################################

        cur.execute(f'''  select * from customer_details where first_name ='{f_name}' and last_name ='{l_name}' ''')

        #######################################################################################################

        rows = cur.fetchall()

        # add data the tree
        for column in rows:
            self.tree.insert("", END,
                             values=(column[0], column[1], column[2], column[3], column[4], column[5], column[6]))

        db.close()

    # submit
    def submit_details(self):

        error_list = []

        # name checking
        first = self.first_name_entry.get().lower().capitalize()
        last = self.last_name_entry.get().lower().capitalize()

        if " " in first or " " in last or not first or not last:
            error_list.append("Names cannot be empty or contain spaces")

        # check plan
        plan = self.customer_plan.get()
        if not plan:
            error_list.append("Plan must be selected")

        # check email
        email = self.email_entry.get()
        if not email:
            error_list.append("Email Address missing")

        # check phone
        phone = self.phone_entry.get()
        number_list = '1234567890'
        number_check = [False for number in phone]

        # if phone is too short or invalid
        if len(phone) == 7:
            for index, number in enumerate(phone):
                if number in number_list:
                    number_check[index] = True

            if not all(number_check):
                error_list.append("Invalid Phone Number")
        else:
            error_list.append("Invalid Phone Number")

        # get list of errors to display

        address1 = self.address1_entry.get().lower().capitalize()

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

            cur.execute(f'''
            insert into customers (first_name,last_name,telephone,email,address,plan_id) 
                           values ('{first}','{last}','{phone}','{email}','{address1}','{plan_id}')
                ''')
            # commit and close db
            db.commit()
            db.close()

            ##################################################################

            # clear entry boxes after record inserted
            self.first_name_entry.delete(0, END)
            self.last_name_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.address1_entry.delete(0, END)
            self.phone_entry.delete(0, END)
            self.customer_plan.set(' ')

            # show success message
            messagebox.showinfo(title="Success", message="Done.", parent=self.tab2)
