from tkinter import *



def window_pos(w, h):
    # dummy window to get screen size
    dummy = Tk()

    # hide window
    dummy.withdraw()
    # get the screen width and height
    x = (dummy.winfo_screenwidth() / 2) - (w / 2)
    y = (dummy.winfo_screenheight() / 2) - (h / 2)

    # destroy window
    dummy.destroy()

    # return str
    return "%dx%d+%d+%d" % (w, h, x, y)
