# imports
from tkinter import *
from funcs.window_position import window_pos
from tkinter.ttk import *
import json
import os

# root
root_folder = os.path.dirname(os.getcwd())
# main
window = Tk()

# window dimensions
width = 300
height = 400
window.geometry(window_pos(width, height))
window.resizable(False, False)

# title
window.title("Login")


# class
class Logon:

    def __init__(self, master):

        # dummy frame
        frame = Frame()
        frame.pack()

        # font
        self.l_style = "Arial 15"
        self.e_style = "Arial 12"

        # json path
        self.json_path = root_folder + "\\ui\\config.json"
        # vars
        self.temp_username = ''
        self.check_box_var = IntVar()

        # img path

        self.logo_img = PhotoImage(file=root_folder + "\\assets\\user.png")

        # check if file exists
        if os.path.exists(self.json_path) and not os.stat(self.json_path).st_size == 0:
            # open file if it exists and isn't empty
            with open(self.json_path, "r") as file:
                # load file
                data = json.load(file)
                self.temp_username = data['USERNAME']
                self.check_box_var.set(1)

        # button function
        def clicked():
            # save username if checkbox is ticked
            if self.username_entry.get() and self.check_box_var.get():
                # save username into file

                with open(self.json_path, "w") as config:
                    user_config = {"USERNAME": self.username_entry.get(), "REMEMBER": str(self.check_box_var.get())}
                    json.dump(user_config, config)

            # clear file if checkbox is not ticked
            else:
                with open(self.json_path, "w") as config:
                    config.truncate(0)

        # logo
        self.logo = Canvas(width=105, height=105)
        self.logo.pack()
        self.logo.create_image(5, 5, anchor=NW, image=self.logo_img, )

        # username
        # label
        self.username_label = Label(master, font=self.l_style, text="Username").pack(pady=(20, 0))

        # entry
        self.username_entry = Entry(master, width=25, font=self.e_style)
        self.username_entry.pack()

        # password
        # label
        self.password_label = Label(master, font=self.l_style, text="Password").pack(pady=(10, 0))
        # entry
        self.password_entry = Entry(master, font=self.e_style, width=25, show="*")
        self.password_entry.pack()

        # if remember username is selected the username is filled in
        if self.check_box_var.get():
            self.username_entry.insert(0, self.temp_username)
            self.password_entry.focus_force()
        else:
            self.username_entry.focus_force()

            # print(check_box_var.get())

        # check_box box
        self.check_box = Checkbutton(master, text="Remember username?", variable=self.check_box_var)

        # check box is un selected if remember username was not selected
        if not self.check_box_var:
            self.check_box.selection_clear()

        self.check_box.pack(pady=(20, 0))

        # button
        self.login_button = Button(master, text="Login", command=clicked, width=20)
        self.login_button.pack(pady=(20, 0))


run = Logon(window)
# icon
window.iconbitmap(root_folder + "\\assets\\ico.ico")
window.mainloop()
