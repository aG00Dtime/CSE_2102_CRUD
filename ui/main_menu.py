from tkinter import *
from tkinter.ttk import *

from funcs.window_position import window_pos
from ui.customer_manager import CustomerManager
from ui.employee_manager import EmployeeManager
import os

root = os.path.abspath(os.curdir)


class MainMenu(Tk):
    def __init__(self, access_level, username):
        super(MainMenu, self, ).__init__()
        # pass access level
        self.access = access_level
        # pass user
        self.user = username

        self.title("Menu")
        self.resizable(False, False)
        self.geometry(window_pos(400, 400))

        # icon
        self.iconbitmap(os.path.join(root, 'assets', 'icon.ico'))

        # buttons
        self.customer_button = Button(self, text="Manage Customers", command=self.customer, width=40).pack(pady=(40, 0))
        self.employee_button = Button(self, text="Manage Employees", command=self.employee, width=40).pack(pady=(20, 0))
        self.employee_button = Button(self, text="Manage Employees", command=self.employee, width=40).pack(pady=(20, 0))
        self.employee_button = Button(self, text="Manage Employees", command=self.employee, width=40).pack(pady=(20, 0))

    def customer(self):
        open_customer_manager = CustomerManager(self.access, self.user)

    def employee(self):
        open_employee_manager = EmployeeManager(self.access, self.user)