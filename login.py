import tkinter
import tkinter.messagebox
from tkinter import *
from window_position import window_pos
# from tkinter.ttk import *
import tkinter.ttk as ttk
import json
import os

# window dimension
width = 300
height = 400
# font
l_style = "Arial 15"
e_style = "Arial 12"

# window
window = Tk()
# title
window.title("Login")

# check_box box var
checked = IntVar()
temp_username = ''

# check_box if json is empty or not
if os.stat("config.json").st_size == 0:
    temp_username = ''
    checked = 0
else:
    with open("config.json""r") as file:
        data = json.load(file)
        temp_username = data['USERNAME']
        checked = data['REMEMBER']

# logo
logo = Canvas(window, width=105, height=105)
logo.pack(pady=(10, 0))

# place logo
logo_img = PhotoImage(file="user.png")
logo.create_image(5, 5, anchor=NW, image=logo_img, )

# size
window.geometry(window_pos(width, height))
window.resizable(False, False)

# username
# label
username_label = Label(window, font=l_style, text="Username").pack(pady=(20, 0))
# check_box if username is saved
username_var = ''

# entry
username_entry = Entry(window, width=25, font=e_style)
username_entry.pack()

# password
# label
password_label = Label(window, font=l_style, text="Password").pack(pady=(10, 0))
# entry
password_entry = Entry(window, font=e_style, width=25, show="*")
password_entry.pack()


# button function
def clicked():
    # save username if checkbox is ticked
    if  username_entry.get() and checked==1:
        with open("config.json", "w") as config:
            user_config = {"USERNAME": username_entry.get(), "REMEMBER": checked.get()}
            json.dump(user_config, config)

    # clear file if checkbox is not ticked
    else:
        with open("config.json", "w") as config:
            config.truncate(0)
    # test
    var = username_entry.get(), password_entry.get(), checked.get()
    tkinter.messagebox.showinfo(message=var)


# check_box box
check_box = Checkbutton(window, text="Remember username?", variable=checked)

check_box.selection_clear()
check_box.pack(pady=(20, 0))

# button
login_button = Button(window, text="Login", command=clicked, width=25)
login_button.pack(pady=(20, 0))

# run
window.mainloop()
