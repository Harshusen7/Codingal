# Import necessary libraries
from tkinter import *

# setting up main window
root = Tk()
root.geometry("400x300")
root.title("main")

# function to open new (top level) window
def topwin():
    # setting up top window
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")

    # adding a label wigdet to top window
    l2 = Label(top, text="This is top level window")
    l2.pack()

    top.mainloop()

# adding a label and button widget to root (main) window
l = Label(root, text="This is root window")
btn = Button(root,text="click here to open another window", command=topwin)

# arranging widgets
l.pack()
btn.pack()

root.mainloop()