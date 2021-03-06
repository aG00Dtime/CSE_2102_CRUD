import os
from tkinter import *
from tkinter.ttk import *

from funcs.reports_generator import report
from funcs.window_position import window_pos
from ui.customer_manager import CustomerManager
from ui.employee_manager import EmployeeManager
from ui.inventory_manager import InventoryManager
from ui.order_manager import OrderManager
from ui.plan_manager import PlanManager
from ui.supplier_manager import SupplierManager
from ui.user_manager import UserManager

root = os.path.abspath(os.curdir)


class MainMenu(Tk):
    def __init__(self, access_level, username):
        super(MainMenu, self, ).__init__()

        # pass access level
        self.access = access_level

        # pass user
        self.user = username

        self.title("SMJ Database Manager")
        self.resizable(False, False)
        self.geometry(window_pos(500, 600))

        self.window_title = Label(self, text="SMJ Manager", font="ARIAL 16 bold").pack(pady=10)

        # icon
        self.iconbitmap(os.path.join(root, 'assets', 'icon.ico'))

        # buttons
        # customer
        self.customer_label = Label(self, text="Customers", font="ARIAL 10 bold").pack()
        self.customer_button = Button(self, text="Manage Customers", command=self.customer, width=40).pack(pady=(5, 10))

        # employee
        self.employee_label = Label(self, text="Employees", font="ARIAL 10 bold").pack()
        self.employee_button = Button(self, text="Manage Employees", command=self.employee, width=40).pack(pady=(5, 10))

        # orders
        self.order_label = Label(self, text="Orders", font="ARIAL 10 bold").pack()
        self.order_button = Button(self, text="Manage Orders", width=40, command=self.orders).pack(
            pady=(5, 10))

        # inventory
        self.inventory_label = Label(self, text="Inventory", font="ARIAL 10 bold").pack()
        self.inventory_button = Button(self, text="Manage Inventory", width=40, command=self.inventory).pack(
            pady=(5, 10))

        # suppliers
        self.supplier_label = Label(self, text="Suppliers", font="ARIAL 10 bold").pack()
        self.supplier_button = Button(self, text="Manage Suppliers", command=self.supplier, width=40).pack(
            pady=(5, 10))

        if 'admin' in access_level:
            # plans
            self.plans_label = Label(self, text="Subscription Plans", font="ARIAL 10 bold").pack()
            self.plans_label_button = Button(self, text="Manage Subscriptions Plans", command=self.plans,
                                             width=40).pack(pady=(5, 10))

            # users
            self.users_label = Label(self, text="Database Users", font="ARIAL 10 bold").pack()
            self.users_button = Button(self, text="Manage Users", command=self.users, width=40).pack(
                pady=(5, 10))

            # reports
            self.report = Label(self, text="Reports", font="ARIAL 10 bold").pack()
            self.report_button = Button(self, text="Produce database reports", command=report, width=40).pack(
                pady=(5, 10))

    def customer(self):
        open_customer_manager = CustomerManager(self.access, self.user)

    def employee(self):
        open_employee_manager = EmployeeManager(self.access, self.user)

    def supplier(self):
        open_supplier_manager = SupplierManager(self.access, self.user)

    def users(self):
        open_user_manager = UserManager(self.access, self.user)

    def orders(self):
        open_order_manager = OrderManager(self.access, self.user)

    def inventory(self):
        open_inventory_manager = InventoryManager(self.access, self.user)

    def plans(self):
        open_plans = PlanManager(self.access, self.user)
