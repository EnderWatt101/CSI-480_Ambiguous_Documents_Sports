from tkinter import *
from tkinter import ttk
# ------------------------------
# Ambiguous Documents
# Software Engineering
# Coding Project: Recreating IM Leagues
# Evan McCarthy, Jakob Watt, Tegan McBride, Jack Maher, Christian Gruyon
# ------------------------------



def forgetWig(wig):
    for widget in wig.winfo_children():
        widget.destroy()

def changeFrame(frame):
    forgetWig(currentFrame)
    lbl_Players = Label(currentFrame, text="Players:")
    if frame == "button_1":    
        button_a1 = Button(currentFrame, text="Sam")
        button_a2 = Button(currentFrame, text="Jack")
    elif frame == "button_2":
        button_a1 = Button(currentFrame, text="Megan")
        button_a2 = Button(currentFrame, text="Lobo")
    elif frame == "button_3":
        button_a1 = Button(currentFrame, text="Jack")
        button_a2 = Button(currentFrame, text="Jill")
    elif frame == "button_4":
        button_a1 = Button(currentFrame, text="Aaron")
        button_a2 = Button(currentFrame, text="Jim")
    
    lbl_Players.pack() #Pack this first to be on top
    #-------Expand this list?
    button_a1.pack()
    button_a2.pack()
    #--------Do these after
    lbl_bottom = Label(currentFrame, text="^Look its player buttons")
    lbl_bottom.pack()
    notebook.add(currentFrame, text='Current Frame')
    notebook.select(1)#DONT LIKE

top = Tk() #needs to be on top of other code, similar to main()
top.title("Lazie Sports")

notebook = ttk.Notebook(top)
notebook.pack(pady=10, expand=True)
topFrame = Frame(notebook)


currentFrame = Frame(notebook, borderwidth = 2, bg="Black")
#teamlist = []
teamlist = ["WMT", "IML", "IMT", "Testing the length?"]

list_Team1 = ["Sam", "Jack", "John"]
list_Team2 = ["Megan", "Austin", "Allie"]

button_1 = Button(topFrame, text=teamlist[0], padx=40, pady=20, command=lambda: changeFrame("button_1"))
button_2 = Button(topFrame, text=teamlist[1], padx=40, pady=20, command=lambda: changeFrame("button_2"))
button_3 = Button(topFrame, text=teamlist[2], padx=40, pady=20, command=lambda: changeFrame("button_3"))
button_4 = Button(topFrame, text=teamlist[3], padx=40, pady=20, command=lambda: changeFrame("button_4"))


button_1.grid(row=1, column=0)
button_2.grid(row=2, column=0)
button_3.grid(row=3, column=0)
button_4.grid(row=4, column=0)

welcome_label = Label(topFrame, text="Teams") #"Changed Washing Machine Team" to "Teams"
welcome_label.grid(row=0, column=0)

notebook.add(topFrame, text='Home')
#notebook.add(frame2, text='Profile')

top.mainloop()
