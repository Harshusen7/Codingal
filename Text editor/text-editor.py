# import neccessary packages
from tkinter import *
from tkinter.filedialog import askopenfilenname, asksaveasfilename

# setup root window
window = Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Function to Open a file
def open_file():
    """Open a file for editing."""
    filepath = askopenfilenname(
        filetypes=[("Text Files", "*.txt"), ("All files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    #if a file is opened then displaythe contents of the file
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    window.title(f"Codingal's Text Editor - {filepath}")

def save_file():

    filepath = asksaveasfilename( defaultextension = "txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], )
    if not filepath:
        return
    with open(filepath)
    

