import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

from funcs.connector import db_conn
from funcs.window_position import window_pos

root = os.path.abspath(os.curdir)


# customer window
class SupplierManager(Tk):
    def __init__(self, access_level, username):
        super(SupplierManager, self).__init__()

        self.title("Supplier Manager")
        self.geometry(window_pos(1024, 600))
        self.resizable(False, False)

        self.user = username



        # icon
        self.iconbitmap(os.path.join(root, 'assets', 'icon.ico'))

        # window_title
        self.window_title = Label(self, text="Supplier Manager", font="ARIAL 16 bold").grid()

        # create notebook to hold tabs
        self.tabs = Notebook(self)


