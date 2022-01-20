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
        for i in range(5):
            self.tree.column(str(i), anchor="center")

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

    def insert_users(self):

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

        # SQL
        # INSERT INTO USERS TABLE
        cur.execute(f'''INSERT INTO USERS (USERNAME,PASSWORD,ACCESS_LEVEL)
        VALUES("{username}","{password}","{access_level}")''')

        # GET LAST GENERATED USER_ID FROM USERS TABLE
        cur.execute('''SET @LAST_ID = LAST_INSERT_ID()''')

        # INSERT USER_ID AND EMPLOYEE_ID INTO EMPLOYEE_LOGINS TABLE
        cur.execute(f'''INSERT INTO EMPLOYEE_LOGINS (LOGIN_USER_ID,LOGIN_EMPLOYEE_ID)
        VALUES(@LAST_ID,"{employee_id}")''')

        db.commit()
        db.close()

        # clear fields
        self.user_username_tab_2_entry.delete(0, END)
        self.user_password_tab_2_entry.delete(0, END)
        self.user_employee_id_tab_2_entry.delete(0, END)
        self.user_access_level.set(' ')

        # done message
        messagebox.showinfo(title="Done", message="Success", parent=self.tab2)

    def query_users(self):

        """QUERY USERS TABLE"""

        # connect to db
        db = db_conn()
        cur = db.cursor()

        # SQL
        cur.execute(''' SELECT * FROM employee_login ''')

        # fetch data
        data = cur.fetchall()

        if not data:
            messagebox.showerror(message="Table empty", title="ERROR", parent=self.tab1)

        # close connection
        else:
            # clear out tree view
            self.tree.delete(*self.tree.get_children())

            # insert data
            for column in data:
                self.tree.insert("", END,
                                 values=(
                                     column[0], column[1], column[2], column[3], column[4]))
        db.close()
