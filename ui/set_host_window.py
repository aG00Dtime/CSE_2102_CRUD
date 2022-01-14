import tkinter
from tkinter import *
import tkinter.messagebox

import mysql.connector as mysql
import funcs.connector
from funcs.window_position import window_pos
from tkinter.ttk import *
import os
import json
from cryptography.fernet import Fernet

root = os.path.abspath(os.curdir)


class HostWindow(tkinter.Tk):

    def __init__(self):
        super(HostWindow, self).__init__()

        # title
        self.title("Host Configuration")
        # json
        self.json_path = os.path.join(root, 'host_config.json')

        # decrypt key
        with open(os.path.join(root, 'k.key'), 'rb') as key:
            self.key = key.read()

        self.f = Fernet(self.key)

        # size and window pos
        self.geometry(window_pos(300, 400))

        # font
        self.l_style = "Arial 15"
        self.e_style = "Arial 12"

        # resize
        self.resizable(False, False)

        # label
        self.host_address = Label(self, font=self.l_style, text="Host Address").pack(pady=(20, 0))
        self.host_address_entry = Entry(self, width=25, font=self.e_style)
        self.host_address_entry.pack()

        # username
        self.username_label = Label(self, font=self.l_style, text="Username").pack(pady=(20, 0))
        self.username_entry = Entry(self, width=25, font=self.e_style)
        self.username_entry.pack()

        # password
        self.password_label = Label(self, font=self.l_style, text="Password").pack(pady=(20, 0))
        self.password_entry = Entry(self, width=25, font=self.e_style, show="*")
        self.password_entry.pack()

        # database
        self.database_label = Label(self, font=self.l_style, text="Database").pack(pady=(20, 0))
        self.database_entry = Entry(self, width=25, font=self.e_style)
        self.database_entry.pack()

        # read file
        if os.path.exists(self.json_path) and not os.stat(self.json_path).st_size == 0:
            # open file if it exists and isn't empty
            with open(self.json_path, "r") as file:
                # load file
                data = json.load(file)

                f = Fernet(self.key)
                pwe = (data['PASSWORD'].encode())

                self.pwd = (str(f.decrypt(pwe)).strip("b").strip("'").strip("'"))

                mask = ''

                pl = len(self.pwd)

                for i in range(pl):
                    mask += "*"

                # insert details
                self.host_address_entry.insert(0, data['HOST'])
                self.username_entry.insert(0, data['USERNAME'])
                self.password_entry.insert(0, mask)
                self.database_entry.insert(0, data['DATABASE'])

        # save
        self.save_button = Button(self, text="Test and save connection details", command=self.save).pack(pady=(20, 0))
        self.mainloop()

    def save(self):

        password = self.password_entry.get()

        # if pw wasn't changed
        if "*" in password:

            password = self.pwd.encode()
        else:
            password = password.encode()

        encrypted_pw = self.f.encrypt(password)

        with open(self.json_path, "w") as host_config:
            data = {"HOST": self.host_address_entry.get(),
                    "USERNAME": self.username_entry.get(),
                    "PASSWORD": str(encrypted_pw).strip("b").strip("'").strip("'"),
                    "DATABASE": self.database_entry.get()
                    }

            json.dump(data, host_config, indent=2)

        # check if details are valid
        db_check = funcs.connector.db_conn()

        if type(db_check) == mysql.connection.MySQLConnection:

            tkinter.messagebox.showinfo(message="Host configuration saved!", title="Success",parent=self)
            self.destroy()

        else:
            tkinter.messagebox.showerror(title='Error', message=db_check,parent=self)

