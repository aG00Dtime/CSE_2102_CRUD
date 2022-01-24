import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from funcs.connector import db_conn
from funcs.window_position import window_pos

root = os.path.abspath(os.curdir)


class PlanManager(Tk):
    def __init__(self, access_level, user):
        super(PlanManager, self).__init__()

        self.title("Subscriptions Manager")

        self.geometry(window_pos(940, 600))

        self.resizable(False, False)

        # icon
        self.iconbitmap(os.path.join(root, 'assets', 'icon.ico'))

        # window_title
        self.window_title = Label(self, text="Subscriptions Manager", font="ARIAL 16 bold").grid(pady=(20, 20))

        # tabs
        self.tabs = Notebook(self)

        self.tab1 = Frame(self.tabs)
        self.tab2 = Frame(self.tabs)
        self.tab3 = Frame(self.tabs)
        self.tab4 = Frame(self.tabs)

        self.tabs.add(self.tab1, text="View Plans")
        self.tabs.add(self.tab2, text="Add New Plans")
        self.tabs.add(self.tab3, text="Update New Plans")
        self.tabs.add(self.tab4, text="Delete Plans")

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

        self.plan_name_label = Label(self.tab2, text="Plan Name").grid(row=0, column=0, padx=(230, 5), pady=(30, 5))
        self.plan_name_entry_tab_2 = Entry(self.tab2, width=40)
        self.plan_name_entry_tab_2.grid(row=0, column=1, pady=(30, 5))

        self.plan_cost_label = Label(self.tab2, text="Price").grid(row=1, column=0, padx=(230, 5), pady=(5, 5))
        self.plan_cost_label_entry_tab_2 = Entry(self.tab2, width=40)
        self.plan_cost_label_entry_tab_2.grid(row=1, column=1, pady=(5, 5))

        self.plan_burst_speed_label = Label(self.tab2, text="Burst Speed").grid(row=2, column=0, padx=(230, 5),
                                                                                pady=(5, 5))
        self.plan_burst_speed_entry_tab_2 = Entry(self.tab2, width=40)
        self.plan_burst_speed_entry_tab_2.grid(row=2, column=1, pady=(5, 5))

        self.plan_upload_speed_label = Label(self.tab2, text="Upload Speed").grid(row=3, column=0, padx=(230, 5),
                                                                                  pady=(5, 5))
        self.plan_upload_speed_entry_tab_2 = Entry(self.tab2, width=40)
        self.plan_upload_speed_entry_tab_2.grid(row=3, column=1, pady=(5, 5))

        self.plan_download_speed_label = Label(self.tab2, text="Download Speed").grid(row=4, column=0, padx=(230, 5),
                                                                                      pady=(5, 5))
        self.plan_download_speed_entry_tab_2 = Entry(self.tab2, width=40)
        self.plan_download_speed_entry_tab_2.grid(row=4, column=1, pady=(5, 5))

        self.plan_submit_button = Button(self.tab2, width=40, text="Submit", command=self.add_plan).grid(row=5,
                                                                                                         column=1,
                                                                                                         pady=(5, 5))
        # tab 3 ####################################################################################################
        self.plan_id_label = Label(self.tab3, text="Plan ID").grid(row=0, column=0, pady=(50, 5),
                                                                   padx=(240, 20))
        self.plan_id_entry_tab_3 = Entry(self.tab3, width=40)
        self.plan_id_entry_tab_3.grid(row=0, column=1, pady=(50, 5))
        self.search_plan_button = Button(self.tab3, text="Search", command=self.load_plan)
        self.search_plan_button.grid(row=1, column=1)

        self.plan_name_label_tab_3 = Label(self.tab3, text="Plan Name").grid(row=2, column=0, padx=(230, 5),
                                                                             pady=(50, 5))
        self.plan_name_entry_tab_3 = Entry(self.tab3, width=40)
        self.plan_name_entry_tab_3.grid(row=2, column=1, pady=(50, 5))

        self.plan_cost_label = Label(self.tab3, text="Price").grid(row=3, column=0, padx=(230, 5), pady=(5, 5))
        self.plan_cost_label_entry_tab_3 = Entry(self.tab3, width=40)
        self.plan_cost_label_entry_tab_3.grid(row=3, column=1, pady=(5, 5))

        self.plan_burst_speed_label_tab_3 = Label(self.tab3, text="Burst Speed").grid(row=4, column=0, padx=(230, 5),
                                                                                      pady=(5, 5))
        self.plan_burst_speed_entry_tab_3 = Entry(self.tab3, width=40)
        self.plan_burst_speed_entry_tab_3.grid(row=4, column=1, pady=(5, 5))

        self.plan_upload_speed_label_tab_3 = Label(self.tab3, text="Upload Speed").grid(row=5, column=0, padx=(230, 5),
                                                                                        pady=(5, 5))
        self.plan_upload_speed_entry_tab_3 = Entry(self.tab3, width=40)
        self.plan_upload_speed_entry_tab_3.grid(row=5, column=1, pady=(5, 5))

        self.plan_download_speed_label_tab_3 = Label(self.tab3, text="Download Speed").grid(row=6, column=0,
                                                                                            padx=(230, 5),
                                                                                            pady=(5, 5))
        self.plan_download_speed_entry_tab_3 = Entry(self.tab3, width=40)
        self.plan_download_speed_entry_tab_3.grid(row=6, column=1, pady=(5, 5))

        self.plan_submit_button_tab_3 = Button(self.tab3, width=40, text="Submit", command=self.update_plan).grid(row=7,
                                                                                                                  column=1,
                                                                                                                  pady=(
                                                                                                                      5,
                                                                                                                      5))
        # tab 4 #######################################################################################################
        self.plan_id_label_tab_4 = Label(self.tab4, text="Plan ID").grid(row=0, column=0, pady=(50, 5),
                                                                         padx=(270, 20))
        self.plan_id_entry_tab_4 = Entry(self.tab4, width=40)
        self.plan_id_entry_tab_4.grid(row=0, column=1, pady=(50, 5))
        self.search_plan_button_tab_4 = Button(self.tab4, text="Delete", command=self.delete_plan)
        self.search_plan_button_tab_4.grid(row=1, column=1)
        ###############################################################################################################

    def delete_plan(self):
        plan_id = self.plan_id_entry_tab_4.get()

        db = db_conn()
        cur = db.cursor()
        cur.execute(f'''SELECT * FROM PLANS WHERE PLAN_ID= '{plan_id}' ''')

        plan = cur.fetchone()

        if not plan:
            messagebox.showerror(title="Done", message="Invalid Plan ID", parent=self.tab4)
            db.close()
            return

        cur.execute(f'''DELETE FROM PLANS WHERE PLAN_ID='{plan_id}' ''')

        db.commit()
        db.close()

        messagebox.showinfo(title="Done", message="Removed Plan", parent=self.tab4)

    def load_plan(self):
        plan_id = self.plan_id_entry_tab_3.get()

        # clear
        self.plan_name_entry_tab_3.delete(0, END)
        self.plan_burst_speed_entry_tab_3.delete(0, END)
        self.plan_upload_speed_entry_tab_3.delete(0, END)
        self.plan_download_speed_entry_tab_3.delete(0, END)
        self.plan_cost_label_entry_tab_3.delete(0, END)

        db = db_conn()
        cur = db.cursor()
        cur.execute(f'''SELECT * FROM PLANS WHERE PLAN_ID= '{plan_id}' ''')

        plan = cur.fetchone()
        db.close()

        if not plan:
            messagebox.showinfo(title="Done", message="Invalid Plan ID", parent=self.tab3)
            return

        self.plan_name_entry_tab_3.insert(0, plan[1])
        self.plan_burst_speed_entry_tab_3.insert(0, plan[2])
        self.plan_upload_speed_entry_tab_3.insert(0, plan[3])
        self.plan_download_speed_entry_tab_3.insert(0, plan[4])
        self.plan_cost_label_entry_tab_3.insert(0, plan[5])

    def update_plan(self):

        plan_id = self.plan_id_entry_tab_3.get()
        plan_name = self.plan_name_entry_tab_3.get().lower().capitalize()
        plan_burst = self.plan_burst_speed_entry_tab_3.get()
        plan_upload = self.plan_upload_speed_entry_tab_3.get()
        plan_download = self.plan_download_speed_entry_tab_3.get()
        plan_price = self.plan_cost_label_entry_tab_3.get()
        f_plan_price = ''

        if not plan_name or not plan_burst or not plan_upload or not plan_download:
            messagebox.showerror(title="Error", message="Ensure All fields are filled and correct", parent=self.tab3)
            return

        for char in plan_price:
            if char.isalnum():
                f_plan_price += char

        f_plan_price = "${:,.2f}".format(int(f_plan_price))

        db = db_conn()
        cur = db.cursor()
        cur.execute(f'''SELECT PLAN_ID FROM PLANS WHERE PLAN_ID= '{plan_id}' ''')

        plan = cur.fetchone()

        if not plan:
            messagebox.showinfo(title="Done", message="Invalid Plan ID", parent=self.tab3)
            db.close()

        cur.execute(f'''  
        UPDATE PLANS
        SET PLAN_NAME = '{plan_name}'  ,
        PLAN_BURST_SPEED = '{plan_burst}',
        PLAN_UPLOAD_SPEED ='{plan_upload}',
        PLAN_DOWNLOAD_SPEED = '{plan_download}',
        PLAN_COST = '{f_plan_price}'
        WHERE PLAN_ID = '{plan_id}'
        ''')

        db.commit()
        db.close()

        self.plan_name_entry_tab_3.delete(0, END)
        self.plan_burst_speed_entry_tab_3.delete(0, END)
        self.plan_upload_speed_entry_tab_3.delete(0, END)
        self.plan_download_speed_entry_tab_3.delete(0, END)
        self.plan_cost_label_entry_tab_3.delete(0, END)

        messagebox.showinfo(title="Done", message="Plan Updated", parent=self.tab3)

    def add_plan(self):
        plan_name = self.plan_name_entry_tab_2.get().lower().capitalize()
        plan_burst = self.plan_burst_speed_entry_tab_2.get()
        plan_upload = self.plan_upload_speed_entry_tab_2.get()
        plan_download = self.plan_download_speed_entry_tab_2.get()
        plan_price = self.plan_cost_label_entry_tab_2.get()
        f_plan_price = ''

        if not plan_name or not plan_burst or not plan_upload or not plan_download:
            messagebox.showerror(title="Error", message="Ensure All fields are filled and correct", parent=self.tab2)
            return

        for char in plan_price:
            if char.isalnum():
                f_plan_price += char

        f_plan_price = "${:,.2f}".format(int(f_plan_price))

        db = db_conn()
        cur = db.cursor()

        cur.execute(f""" 
        INSERT INTO PLANS (PLAN_NAME,PLAN_BURST_SPEED,PLAN_UPLOAD_SPEED,PLAN_DOWNLOAD_SPEED,PLAN_COST)
        VALUES (
        '{plan_name}',
        '{plan_burst}',
        '{plan_upload}',
        '{plan_download}',
        '{f_plan_price}'

        ) """)

        db.commit()
        db.close()

        self.plan_name_entry_tab_2.delete(0, END)
        self.plan_burst_speed_entry_tab_2.delete(0, END)
        self.plan_upload_speed_entry_tab_2.delete(0, END)
        self.plan_download_speed_entry_tab_2.delete(0, END)
        self.plan_cost_label_entry_tab_2.delete(0, END)

        messagebox.showinfo(title="Done", message="Plan Added", parent=self.tab2)

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
