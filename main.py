from tkinter import *
from tkinter import ttk
# ------------------------------
# Ambiguous Documents
# Software Engineering
# Coding Project: Recreating IM Leagues
# Evan McCarthy, Jakob Watt, Tegan McBride, Jack Maher, Christian Gruyon
# ------------------------------

top = Tk()
top.title("Sports for the less sporty")
#setup fancy windows


def button_click(number):
    return number

## Evan Add
button_1 = Button(top, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(top, text="2", padx=40, pady=20, command=lambda: button_click(2))

player_frame = Frame(top, borderwidth = 2, bg="Black")
player_label = Label(player_frame, text="WMT")
player_label.pack()
player_stat_button = Button(player_frame, text="Players: ", command=lambda: button_click(1))
player_stat_button.pack()
player_frame.grid(row=1, column=1)

button_1.grid(row=1, column=0)
button_2.grid(row=2, column=0)

welcome_label = Label(text="Teams: ")
welcome_label.grid(row=0, column=0)

## Evan Add End

top.mainloop()
