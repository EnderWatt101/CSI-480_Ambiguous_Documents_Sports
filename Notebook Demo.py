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

def changeFrame(frame): ###TODO: Need to add another change frame inside to show players when each team is selected
    #forgetWig(currentFrame)
    tempFrame = Frame(notebook)
    lbl_Players = Label(tempFrame, text="Teams:")
    if frame == "Tennis":    
        button_a1 = Button(tempFrame, text="Team 1")
        button_a2 = Button(tempFrame, text="Team 2")
    elif frame == "Kickball":
        button_a1 = Button(tempFrame, text="Team 1")
        button_a2 = Button(tempFrame, text="Team 2")
    elif frame == "Basketball":
        button_a1 = Button(tempFrame, text="Team 1")
        button_a2 = Button(tempFrame, text="Team 2")
    elif frame == "Soccer":
        button_a1 = Button(tempFrame, text="Team 1")
        button_a2 = Button(tempFrame, text="Team 2")
    
    lbl_Players.grid(row=0, column=0) #Pack this first to be on top
    #-------Expand this list?
    button_a1.grid(row=1, column=0)
    button_a2.grid(row=2, column=0)
    #--------Do these after
    lbl_bottom = Label(tempFrame, text="^Look its Team buttons")
    lbl_bottom.grid(row=3, column=0)
    for i in range(len(tabFrameList)):
        print(tabFrameList[i])
        if frame == tabFrameList[i][0]:
            notebook.select(tabFrameList[i][1])
            return
    tabFrameList.append([frame, tempFrame])
    notebook.add(tempFrame, text=frame)
    notebook.select(tempFrame)

top = Tk() #needs to be on top of other code, similar to main()
top.title("Lazie Sports")

notebook = ttk.Notebook(top)
notebook.pack(pady=10, expand=True)
topFrame = Frame(notebook)


currentFrame = Frame(notebook, borderwidth = 2, bg="Black")
#teamlist = []
sportList = ["Tennis", "Kickball", "Basketball", "Soccer"]

list_Tennis = ["WMT", "IML", "TMP"]
list_Kickball = ["WMT", "IML", "TMP"]

tabFrameList = []#list for holding tabs to refrence later

button_1 = Button(topFrame, text=sportList[0], padx=40, pady=20, command=lambda: changeFrame(sportList[0]))
button_2 = Button(topFrame, text=sportList[1], padx=40, pady=20, command=lambda: changeFrame(sportList[1]))
button_3 = Button(topFrame, text=sportList[2], padx=40, pady=20, command=lambda: changeFrame(sportList[2]))
button_4 = Button(topFrame, text=sportList[3], padx=40, pady=20, command=lambda: changeFrame(sportList[3]))


button_1.grid(row=1, column=0)
button_2.grid(row=2, column=0)
button_3.grid(row=3, column=0)
button_4.grid(row=4, column=0)

welcome_label = Label(topFrame, text="Sports") #"Changed Washing Machine Team" to "Teams"
welcome_label.grid(row=0, column=0)

notebook.add(topFrame, text='Home')
#notebook.add(frame2, text='Profile')

top.mainloop()
