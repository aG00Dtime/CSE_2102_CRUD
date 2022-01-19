import json
import os
import tkinter as tk
import tkinter.messagebox as mb
from tkinter import *
from tkinter.ttk import *

import funcs.connector
import ui.set_host_window
from funcs.window_position import window_pos
from ui.main_menu import MainMenu

root = os.path.abspath(os.curdir)


class LoginWindow(tk.Tk):

    def __init__(self):
        super(LoginWindow, self).__init__()

        # title
        self.title("Login")

        # size and window pos
        self.geometry(window_pos(300, 400))

        # resize
        self.resizable(False, False)

        # font
        self.l_style = "Arial 15"
        self.e_style = "Arial 12"

        # json path
        self.json_path = os.path.join(root, 'last_user.json')
        # vars
        self.temp_username = ''
        self.check_box_var = tk.IntVar()

        # img path
        self.logo_img_path = os.path.join(root, 'assets', 'user.png')

        self.logo_img = tk.PhotoImage(file=self.logo_img_path)

        # check if file exists
        if os.path.exists(self.json_path) and not os.stat(self.json_path).st_size == 0:
            # open file if it exists and isn't empty
            with open(self.json_path, "r") as file:
                # load file
                data = json.load(file)
                self.temp_username = data['USERNAME']
                self.check_box_var.set(1)

        # logo using canvas
        self.logo = tk.Canvas(self, width=105, height=105)
        self.logo.pack()
        self.logo.create_image(5, 5, anchor=tk.NW, image=self.logo_img, )

        # username
        # label
        self.username_label = Label(self, font=self.l_style, text="Username").pack(pady=(20, 0))

        # entry
        self.username_entry = Entry(self, width=25, font=self.e_style)
        self.username_entry.pack()

        # password
        # label
        self.password_label = Label(self, font=self.l_style, text="Password").pack(pady=(10, 0))
        # entry
        self.password_entry = Entry(self, font=self.e_style, width=25, show="*")
        self.password_entry.pack()

        # if remember username is selected the username is filled in
        if self.check_box_var.get():
            self.username_entry.insert(0, self.temp_username)
            self.password_entry.focus_force()
        else:
            self.username_entry.focus_force()

            # print(check_box_var.get())

        # check_box box
        self.check_box = Checkbutton(self, text="Remember username?", variable=self.check_box_var)

        # check box is un selected if remember username was not selected
        if not self.check_box_var:
            self.check_box.selection_clear()

        self.check_box.pack(pady=(20, 0))

        # button
        self.login_button = Button(self, text="Login", command=self.clicked, width=20)
        self.login_button.pack(pady=(20, 0))

        # icon
        self.iconbitmap(os.path.join(root, 'assets', 'icon.ico'))

        # button function
        self.host_label = Button(self, text="configure host", command=ui.set_host_window.HostWindow).pack(pady=(20, 0))

    def clicked(self):

        # vars to pass

        user_name, pass_word = self.username_entry.get(), self.password_entry.get()
        db = funcs.connector.db_conn()
        cur = db.cursor()
        # testing -------------------add encryption
        cur.execute(f'''SELECT access_level FROM USER WHERE username = '{user_name}' and password = '{pass_word}' ''')
        found = cur.fetchone()

        if found:
            #
            # print(f"Logged in as {user_name}")

            access_level = found

            # save username if checkbox is ticked
            if self.username_entry.get() and self.check_box_var.get():
                # save username into file
                with open(self.json_path, "w") as config:
                    user_config = {"USERNAME": self.username_entry.get()}
                    json.dump(user_config, config)

            self.destroy()
            # open next window
            main_menu = MainMenu(access_level,user_name)

        # if login fails
        else:
            mb.showerror(title="Error", message="Username or Password Error")

        # ---------------------------------------
