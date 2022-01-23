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
    def __init__(self):
        super(PlanManager, self).__init__()


