from tkinter import *
from tkinter import ttk
# ------------------------------
# Ambiguous Documents
# Software Engineering
# Coding Project: Recreating IM Leagues
# Evan McCarthy, Jakob Watt, Tegan McBride, Jack Maher, Christian Gruyon
# ------------------------------


#Functions-----------------

def button_click(number):
    return

def forgetWig(wig):
    wig.forget() # removes from window

def changeFrame(frame, str):
    forgetWig(currentFrame)
    frameTemp = Frame(top)
    if frame == "button_1":
        label_temp = Label(frameTemp, text=str)
        label_temp.pack()
    if frame == "button_2":
        label_temp = Label(frameTemp, text=str)
        label_temp.pack()  
    frameTemp.grid(row=1, column=1)


top = Tk() #needs to be on top of other code, similar to main()
top.title("Lazie Sports")

currentFrame = Frame(top, borderwidth = 2, bg="Black")
currentFrame.grid(row=1, column=1)
#teamlist = []
teamlist = ["WMT", "IML", "IMT", "Testing the length?"]

## Evan Add
button_1 = Button(top, text=teamlist[0], padx=40, pady=20, command=lambda: changeFrame("button_1", teamlist[0]))
button_2 = Button(top, text=teamlist[1], padx=40, pady=20, command=lambda: changeFrame("button_2", teamlist[1]))

currentFrame.grid(row=1, column=1)

button_1.grid(row=1, column=0)
button_2.grid(row=2, column=0)

welcome_label = Label(text="Washing Machine Team")
welcome_label.grid(row=0, column=0)

## Evan Add End

top.mainloop()
