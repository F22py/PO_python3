from tkinter import *
from Swiat import *
from GUI.Game_GUI import *

def makeentry(parent, caption, width=None):
    Label(parent, text=caption).pack(side=LEFT)
    entry = Entry(parent)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry


def get_data():
    try:
        w_s = int(width_entry.get())
        h_s = int(height_entry.get())

        if w_s > 0 and h_s > 0:
            game = Swiat(w_s, h_s)
    except ValueError:
        print("It is not an integer")


root = Tk()

width_entry = makeentry(root, "Width:", 10)

height_entry = makeentry(root, "Height:", 10)

start_button = Button(root, text="Start Game!", width=10, command=get_data)
start_button.pack(side=LEFT)


root.mainloop()
