from tkinter import *
from tkinter.ttk import *

from funcs.window_position import window_pos
from ui.customer_manager import CustomerManager
from ui.employee_manager import EmployeeManager


class MainMenu(Tk):
    def __init__(self, access_level):
        super(MainMenu, self, ).__init__()
        # pass access level
        self.access = access_level

        self.title("Menu")
        self.resizable(False, False)
        self.geometry(window_pos(400, 400))

        # buttons
        self.customer_button = Button(self, text="Manage Customers", command=self.customer).pack(pady=(40, 0))
        self.employee_button = Button(self, text="Manage Employees", command=self.employee).pack(pady=(20, 0))
        self.customer_button = Button(self, text="Manage Inventory", command=self.inventory).pack(pady=(20, 0))

    def customer(self):
        customer_manager = CustomerManager(self.access)

    def employee(self):
        employee_manager = EmployeeManager(self.access)

    def inventory(self):
        print("working")
