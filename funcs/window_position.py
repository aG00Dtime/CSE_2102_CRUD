from tkinter import *


def window_pos(w, h):
    """Takes width and height of a window as arguments and returns a tkinter geometry string that centers the window
    on the screen , usage eg. geometry(window_pos(500,500))"""
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
