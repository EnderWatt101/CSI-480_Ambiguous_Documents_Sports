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

currentFrame = Frame(top, borderwidth = 2, bg="Black")
currentFrame.grid(row=1, column=1)

def button_click(number):
    return

def forgetWig(wig):
    wig.forget() # removes from window

def changeFrame(frame):
    forgetWig(currentFrame)
    frameTemp = Frame(top)
    if frame == "button_1":
        label_temp = Label(frameTemp, text="option 1")
        label_temp.pack()
    if frame == "button_2":
        label_temp = Label(frameTemp, text="option 2")
        label_temp.pack()  
    frameTemp.grid(row=1, column=1)

## Evan Add
button_1 = Button(top, text="1", padx=40, pady=20, command=lambda: changeFrame("button_1"))
button_2 = Button(top, text="2", padx=40, pady=20, command=lambda: changeFrame("button_2"))


player_label = Label(currentFrame, text="Player 1")
player_label.pack()
player_stat_button = Button(currentFrame, text="Stats", command=lambda: button_click(1))
player_stat_button.pack()
currentFrame.grid(row=1, column=1)

button_1.grid(row=1, column=0)
button_2.grid(row=2, column=0)

welcome_label = Label(text="Washing Machine Team")
welcome_label.grid(row=0, column=0)

## Evan Add End

top.mainloop()
