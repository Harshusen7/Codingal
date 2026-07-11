# import necessary libraries
from tkinter import *
from datetime import date 

# create window
root = Tk()
root.title('getting started with widgets')
root.geometry('400x300')

#add widgets
# add label

lbl = Label(text="Hey There!", fg="white", bg=  "#072F5F", height=1, width=300)
# addlabel for getting name as input from user
# use entry widget to create a text box for user to enter details
name_lbl = Label(text="Full Name", bg= "#3895D3")
name_entry = Entry()

# Function to display a message
              