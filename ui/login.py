# imports
import tkinter.messagebox
from tkinter import *
from funcs.window_position import window_pos
from tkinter.ttk import *
import json
import os
from funcs.connector import db_conn
import mysql.connector as mysql


# window class
class Window(tkinter.Tk):

    def __init__(self):
        super().__init__()

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
        self.json_path = os.path.join(os.getcwd(), 'ui', 'config.json')
        # vars
        self.temp_username = ''
        self.check_box_var = IntVar()

        # img path
        self.logo_img_path = os.path.join(os.getcwd(), 'assets', 'user.png')

        self.logo_img = PhotoImage(file=self.logo_img_path)

        # check if file exists
        if os.path.exists(self.json_path) and not os.stat(self.json_path).st_size == 0:
            # open file if it exists and isn't empty
            with open(self.json_path, "r") as file:
                # load file
                data = json.load(file)
                self.temp_username = data['USERNAME']
                self.check_box_var.set(1)

        # logo using canvas
        self.logo = Canvas(self, width=105, height=105)
        self.logo.pack()
        self.logo.create_image(5, 5, anchor=NW, image=self.logo_img, )

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
        self.iconbitmap(os.path.join(os.getcwd(), 'assets', 'ico.ico'))
        # button function

    def clicked(self):

        # vars to pass
        user_name = self.username_entry.get()
        pass_word = self.password_entry.get()

        # db object
        db = db_conn(user_name, pass_word)
        # login
        # check to see if db object is a mysql object and not an error string
        if type(db) == mysql.connection.MySQLConnection:
            # show success info box
            tkinter.messagebox.showinfo(title="Success", message="Logged in user @" + user_name)

            # save username if checkbox is ticked
            if self.username_entry.get() and self.check_box_var.get():
                # save username into file

                with open(self.json_path, "w") as config:
                    user_config = {"USERNAME": self.username_entry.get()}
                    json.dump(user_config, config)

            # clear file if checkbox is not ticked
            else:
                with open(self.json_path, "w") as config:
                    config.truncate(0)

            # close the window
            self.destroy()

            # else
        else:
            tkinter.messagebox.showerror(title="Error", message=db)


# run
def log():
    win = Window()
    win.mainloop()
