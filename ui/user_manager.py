import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from funcs.connector import db_conn
from funcs.window_position import window_pos

root = os.path.abspath(os.curdir)


# customer window
class UserManager(Tk):
    def __init__(self, access_level, username):
        super(UserManager, self).__init__()

        self.title("User Manager")
        # self.geometry(window_pos(800, 600))
        self.resizable(False, False)

        self.user = username

        # icon
        # self.iconbitmap(os.path.join(root, 'assets', 'icon.ico'))

        # create notebook to hold tabs
        self.tabs = Notebook(self)

        # create tabs
        self.tab1 = Frame(self.tabs)
        self.tab2 = Frame(self.tabs)
        self.tab3 = Frame(self.tabs)
        self.tab4 = Frame(self.tabs)

        # add tabs to notebook with tab names
        self.tabs.add(self.tab1, text="View User List")

        self.tabs.add(self.tab2, text="Add User")

        self.tabs.add(self.tab3, text="Update User details")

        if 'admin' in access_level:
            self.tabs.add(self.tab4, text="Delete User")

        tkinter.Grid.rowconfigure(self,0,weight=1)
        tkinter.Grid.columnconfigure(self,0,weight=0)
        self.tabs.grid(column=0,row=0,sticky=E+W+N+S)
        # tab 1

        self.view_label=Label(self.tab1,text='Load User List').grid()


user = UserManager('admin', 'admin')
user.mainloop()
