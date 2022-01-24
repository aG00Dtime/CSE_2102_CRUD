import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from tkinter.ttk import *

from fpdf import FPDF

from funcs.connector import db_conn
from funcs.window_position import window_pos

root = os.path.abspath(os.curdir)


class PlanManager(Tk):
    def __init__(self, access_level, user):
        super(PlanManager, self).__init__()

        self.title("Subscriptions Manager")

        self.geometry(window_pos(940, 600))

        self.resizable(False, False)

        # window_title
        self.window_title = Label(self, text="Subscriptions Manager", font="ARIAL 16 bold").grid(pady=(20, 20))

        self.tabs = Notebook(self)

        self.tab1 = Frame(self.tabs)
        self.tab2 = Frame(self.tabs)
        self.tab3 = Frame(self.tabs)

        self.tabs.add(self.tab1, text="View Plans")
        self.tabs.add(self.tab2, text="Add New Plans")
        self.tabs.add(self.tab3, text="Update New Plans")

        self.tabs.grid()

        self.get_plans_button = Button(self.tab1, text="View Plans", command=self.get_plans, width=50).grid(row=0,
                                                                                                            pady=20,
                                                                                                            padx=(
                                                                                                                260, 0)
                                                                                                            )

        self.tree = Treeview(self.tab1, height=20, show='headings')

        # tree position
        self.tree.grid(row=3, column=0, columnspan=4, padx=(10, 0))
        # scroll bar
        self.scrollbar = Scrollbar(self.tab1, orient="vertical", command=self.tree.yview)

        self.scrollbar.grid(row=3, column=4, sticky="NS")

        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # columns and headings
        self.tree['columns'] = ("1", "2", "3", "4", '5', '6')
        self.tree.heading("1", text="ID")
        self.tree.heading("2", text="Plan Name")
        self.tree.heading("3", text="Burst Speed")
        self.tree.heading("4", text="Upload Speed")
        self.tree.heading("5", text="Download Speed")
        self.tree.heading("6", text="Cost")

        self.tree.column("1", width=50, anchor=W)

        for i in range(2, 7):
            self.tree.column(str(i), width=170, anchor=W)

        # TAB 2 #######################################################################################################

        self.plan_name_label = Label(self.tab2, text="Plan Name").grid(row=0, column=0, padx=(200, 5), pady=(30, 5))
        self.plan_name_entry_tab_2 = Entry(self.tab2, width=40)
        self.plan_name_entry_tab_2.grid(row=0, column=1, pady=(30, 5))

        self.plan_cost_label = Label(self.tab2, text="Price").grid(row=1, column=0, padx=(200, 5), pady=(5, 5))
        self.plan_cost_label_entry_tab_2 = Entry(self.tab2, width=40)
        self.plan_cost_label_entry_tab_2.grid(row=1, column=1, pady=(5, 5))

        self.plan_burst_speed_label = Label(self.tab2, text="Burst Speed").grid(row=2, column=0, padx=(200, 5),
                                                                                pady=(5, 5))
        self.plan_burst_speed_entry_tab_2 = Entry(self.tab2, width=40)
        self.plan_burst_speed_entry_tab_2.grid(row=2, column=1, pady=(5, 5))

        self.plan_upload_speed_label = Label(self.tab2, text="Upload Speed").grid(row=3, column=0, padx=(200, 5),
                                                                                  pady=(5, 5))
        self.plan_upload_speed_entry_tab_2 = Entry(self.tab2, width=40)
        self.plan_upload_speed_entry_tab_2.grid(row=3, column=1, pady=(5, 5))

        self.plan_download_speed_label = Label(self.tab2, text="Download Speed").grid(row=4, column=0, padx=(200, 5),
                                                                                  pady=(5, 5))
        self.plan_download_speed_entry_tab_2 = Entry(self.tab2, width=40)
        self.plan_download_speed_entry_tab_2.grid(row=4, column=1, pady=(5, 5))

    def get_plans(self):

        """GET SUB PLANS AVAILABLE"""

        db = db_conn()
        cur = db.cursor()

        cur.execute("SELECT * FROM PLANS")

        plans = cur.fetchall()

        db.close()

        # clear out tree view

        self.tree.delete(*self.tree.get_children())

        if not plans:
            messagebox.showerror(title="Error", message="No results to display", parent=self.tab1)
            return

        for plan in plans:
            self.tree.insert("", END,
                             values=(
                                 plan[0], plan[1], plan[2], plan[3], plan[4], plan[5]))
