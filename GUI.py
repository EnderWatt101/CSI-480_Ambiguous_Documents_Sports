import tkinter
from tkinter import *

root = tkinter.Tk()
root.title('Sports App')
#root.geometry("2000x1125")


def button_click(number):
    return

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))

button_1.grid(row=0, column=0)

tkinter.mainloop()