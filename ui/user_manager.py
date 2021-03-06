import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from funcs.connector import db_conn
from funcs.window_position import window_pos

root = os.path.abspath(os.curdir)


class UserManager(Tk):
    def __init__(self, access_level, username):
        super(UserManager, self).__init__()

        self.title("User Manager")
        self.geometry(window_pos(700, 500))
        self.resizable(False, False)
        # var
        self.user_user_id_temp = None

        # ready key from file
        with open(os.path.join(root, 'k.key'), 'rb') as key:
            key = key.read()

        # encryption key
        self.key = str(key).strip("b").strip("'").strip("'")

        # current user
        self.user = username
        self.access_level = access_level

        # icon
        self.iconbitmap(os.path.join(root, 'assets', 'icon.ico'))

        # window_title
        self.window_title = Label(self, text="User Manager", font="ARIAL 16 bold").grid(pady=(20, 20))

        # create notebook to hold tabs
        self.tabs = Notebook(self)

        self.tab1 = Frame(self.tabs)
        self.tab2 = Frame(self.tabs)
        self.tab3 = Frame(self.tabs)
        self.tab4 = Frame(self.tabs)

        self.tabs.add(self.tab1, text="User List")
        self.tabs.add(self.tab2, text="Add User")
        self.tabs.add(self.tab3, text="Update User")
        self.tabs.add(self.tab4, text="Delete User")

        self.tabs.grid()

        # TAB 1 ####################################################################################

        self.view_user_button = Button(self.tab1, text="View User List", width=40,
                                       command=self.query_users).grid(padx=(130, 0), pady=20,
                                                                      row=0,
                                                                      column=1)

        # tree position
        self.tree = Treeview(self.tab1, height=15, show='headings')

        # scrollbar
        self.scrollbar = Scrollbar(self.tab1, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=3, column=4, sticky="NS")
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # conf columns
        self.tree['columns'] = ("1", "2", "3", "4", "5")
        self.tree.heading("1", text="ID")
        self.tree.heading("2", text="Username")
        self.tree.heading("3", text="Access Level")
        self.tree.heading("4", text="Employee First Name")
        self.tree.heading("5", text="Employee Last Name")

        # width
        self.tree.column('1', width=50)
        self.tree.column('2', width=100)
        self.tree.column('3', width=150)
        self.tree.column('4', width=180)
        self.tree.column('5', width=180)

        # center tree data
        for i in range(6):
            self.tree.column(str(i), anchor=W)

        self.tree.grid(row=3, column=0, columnspan=4, padx=(10, 0))

        # tab 2 ##################################################################################

        # name
        self.entry_box_width = 40
        self.user_username_tab_2_label = Label(self.tab2, text="Username").grid(row=0, column=0, pady=(50, 5),
                                                                                padx=(140, 20))
        self.user_username_tab_2_entry = Entry(self.tab2, width=self.entry_box_width)
        self.user_username_tab_2_entry.grid(row=0, column=1, pady=(50, 5))

        # password
        self.user_password_tab_2_label = Label(self.tab2, text="Password").grid(row=1, column=0, pady=5,
                                                                                padx=(140, 20))
        self.user_password_tab_2_entry = Entry(self.tab2, width=self.entry_box_width)
        self.user_password_tab_2_entry.grid(row=1, column=1, pady=5)

        # employee_id
        self.user_employee_id_tab_2_label = Label(self.tab2, text="Employee ID").grid(row=2, column=0, pady=5,
                                                                                      padx=(140, 20))
        self.user_employee_id_tab_2_entry = Entry(self.tab2, width=self.entry_box_width)
        self.user_employee_id_tab_2_entry.grid(row=2, column=1, pady=5)

        # access_level
        self.user_access_label = Label(self.tab2, text="Access Level ").grid(row=3, column=0, pady=5,
                                                                             padx=(140, 20))
        self.user_access_level = Combobox(self.tab2, width=36, state='readonly')
        self.user_access_level['values'] = ["ADMIN", "USER"]
        self.user_access_level.grid(row=3, column=1, pady=5)
        # submit
        self.insert_user_button = Button(self.tab2, text="Submit", width=self.entry_box_width,
                                         command=self.insert_users)
        self.insert_user_button.grid(row=4, column=1, pady=5)

        # tab 3 #############################################################################################
        # search by id
        self.search_user_id_tab_3 = Label(self.tab3, text="User ID").grid(row=0, column=0, pady=(50, 5), padx=(140, 20))

        self.search_user_id_entry_tab_3 = Entry(self.tab3, width=self.entry_box_width)
        self.search_user_id_entry_tab_3.grid(row=0, column=1, pady=(50, 5))

        self.search_id_button = Button(self.tab3, width=self.entry_box_width, text="Search",
                                       command=self.query_update_user).grid(row=1, column=1)

        # name
        self.user_username_tab_3_label = Label(self.tab3, text="Username").grid(row=2, column=0, pady=(30, 5),
                                                                                padx=(140, 20))
        self.user_username_tab_3_entry = Entry(self.tab3, width=self.entry_box_width)
        self.user_username_tab_3_entry.grid(row=2, column=1, pady=(30, 5))

        # password
        self.user_password_tab_3_label = Label(self.tab3, text="Password").grid(row=3, column=0, pady=5,
                                                                                padx=(140, 20))
        self.user_password_tab_3_entry = Entry(self.tab3, width=self.entry_box_width)
        self.user_password_tab_3_entry.grid(row=3, column=1, pady=5)

        # access_level
        self.user_access_label_tab_3 = Label(self.tab3, text="Access Level ").grid(row=5, column=0, pady=5,
                                                                                   padx=(140, 20))

        self.user_access_level_tab_3 = Combobox(self.tab3, width=36, state='readonly')
        self.user_access_level_tab_3['values'] = ["ADMIN", "USER"]
        self.user_access_level_tab_3.grid(row=5, column=1, pady=5)

        # submit
        self.insert_user_button_tab_3 = Button(self.tab3, text="Submit", command=self.update_user,
                                               width=self.entry_box_width)
        self.insert_user_button_tab_3.grid(row=6, column=1, pady=5)

        # tab 4 #############################################################################################
        self.user_id_entry_tab_4_label = Label(self.tab4, text="User ID").grid(row=0, column=0,
                                                                               pady=(50, 0), padx=(160, 20),
                                                                               sticky=NW)
        # employee id
        self.user_id_entry_tab_4 = Entry(self.tab4, width=40)
        self.user_id_entry_tab_4.grid(row=0, column=1, pady=(50, 0))

        # button
        self.delete_button_tab_4 = Button(self.tab4, width=40, text="Delete", command=self.delete_user).grid(row=1,
                                                                                                             column=1,
                                                                                                             pady=10)

        ####################################################################################################

    def insert_users(self):

        """INSERT NEW USER LOGIN"""

        username = self.user_username_tab_2_entry.get().lower()
        password = self.user_password_tab_2_entry.get().lower()
        employee_id = self.user_employee_id_tab_2_entry.get()
        access_level = self.user_access_level.get().lower()

        # check fields - simple check
        if not username or not password or not employee_id or not access_level:
            messagebox.showerror(title="Error", message="Ensure all fields are correct", parent=self.tab2)
            return

        db = db_conn()
        cur = db.cursor()

        cur.execute(F"""SELECT EMPLOYEE_ID FROM EMPLOYEES WHERE EMPLOYEE_ID ={employee_id} """)

        exists = cur.fetchone()

        if not exists:
            messagebox.showerror(title="Error", message="Employee Does not exist", parent=self.tab2)
            db.close()
            return
        # SQL
        # INSERT INTO USERS TABLE AND ENCRYPT PASSWORDS USING AES ENCRYPTION
        cur.execute(f'''
        INSERT INTO USERS (USERNAME,PASSWORD,ACCESS_LEVEL,USER_EMPLOYEE_ID)
        VALUES(
        "{username}",
        AES_ENCRYPT("{password}",'{self.key}'),
        "{access_level}",
        "{employee_id}"
        
        )
        ''')

        db.commit()
        db.close()

        # clear fields
        self.user_username_tab_2_entry.delete(0, END)
        self.user_password_tab_2_entry.delete(0, END)
        self.user_employee_id_tab_2_entry.delete(0, END)
        self.user_access_level.set(' ')

        # done message
        messagebox.showinfo(title="Done", message="Success", parent=self.tab2)
        ###########################################################################################################

    def delete_user(self):
        user_id = self.user_id_entry_tab_4.get()

        if not user_id:
            messagebox.showerror(message="Enter User ID", parent=self.tab4, title="Error")
            return

        db = db_conn()
        cur = db.cursor()

        cur.execute(F"""SELECT USER_ID FROM USERS WHERE USER_ID ='{user_id}' """)

        user = cur.fetchone()

        if not user:
            messagebox.showerror(message="User not found", parent=self.tab4, title="Error")
            db.close()
            return

        cur.execute(F""" DELETE FROM USERS WHERE USER_ID = '{user_id}' """)

        db.commit()
        db.close()
        messagebox.showinfo(title="Done", message="User deleted", parent=self.tab4)

    def query_update_user(self):
        """UPDATE USER DETAILS"""

        user_id = self.search_user_id_entry_tab_3.get()

        if not user_id:
            messagebox.showerror(title="Error", message="Enter ID", parent=self.tab3)
            return

        db = db_conn()
        cur = db.cursor()

        sql = f'''
        
        SELECT USERNAME,ACCESS_LEVEL
        
        FROM user_details
        
        WHERE USER_ID = '{user_id}'
        
        '''
        # SQL QUERY
        cur.execute(sql)

        # clear boxes
        self.user_access_level_tab_3.set(' ')
        self.user_username_tab_3_entry.delete(0, END)
        self.user_password_tab_3_entry.delete(0, END)

        data = cur.fetchone()

        if not data:
            messagebox.showerror(message="No results", title="Error", parent=self.tab3)
            db.close()
            return

        username = data[0]
        access_level = data[1]

        # insert user details
        self.user_access_level_tab_3.set(f'''{access_level.upper()}''')
        self.user_username_tab_3_entry.insert(0, username)

        # close
        db.close()

    def update_user(self):

        """UPDATE USER INFO"""

        user_id = self.search_user_id_entry_tab_3.get()
        username = self.user_username_tab_3_entry.get()
        password = self.user_password_tab_3_entry.get()
        access_level = self.user_access_level_tab_3.get().lower()

        if not username or not password or not user_id or not access_level:
            messagebox.showerror(title="Error", message="Ensure All Fields Are Correct", parent=self.tab3)
            return

        db = db_conn()
        cur = db.cursor()

        cur.execute(f"""
        
        UPDATE USERS
        SET USERNAME = '{username}',
        PASSWORD = AES_ENCRYPT("{password}",'{self.key}'),
        ACCESS_LEVEL = '{access_level}'
        WHERE USER_ID = '{user_id}'
        
        """)

        db.commit()
        db.close()

        self.search_user_id_entry_tab_3.delete(0, END)
        self.user_username_tab_3_entry.delete(0, END)
        self.user_password_tab_3_entry.delete(0, END)
        self.user_access_level_tab_3.set(' ')

        messagebox.showinfo(title="Done", message="User Updated.", parent=self.tab3)

    def query_users(self):
        """QUERY USERS TABLE"""

        # connect to db
        db = db_conn()
        cur = db.cursor()

        # SQL
        cur.execute(''' SELECT  * from user_details ''')

        # fetch data
        data = cur.fetchall()

        # clear out tree view
        self.tree.delete(*self.tree.get_children())

        # check if user found
        if not data:
            messagebox.showerror(message="No results", title="ERROR", parent=self.tab3)

        # close connection
        else:
            # clear out tree view
            self.tree.delete(*self.tree.get_children())

            # insert data
            for column in data:
                self.tree.insert("", END,
                                 values=(
                                     column[0], column[1], column[2], column[3], column[4]))

        # close
        db.close()
