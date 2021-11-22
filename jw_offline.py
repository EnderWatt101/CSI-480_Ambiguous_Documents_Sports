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
    forgetWig(f_cur)
    #frameTemp = Frame(top)
    lbl_Players = Label(f_cur, text="Players:")
    if frame == "button_1":    
        button_a1 = Button(f_cur, text="Sam")
        button_a2 = Button(f_cur, text="Jack")
    elif frame == "button_2":
        button_a1 = Button(f_cur, text="Megan")
        button_a2 = Button(f_cur, text="Lobo")
    elif frame == "button_3":
        button_a1 = Button(f_cur, text="Jack")
        button_a2 = Button(f_cur, text="Jill")
    elif frame == "button_4":
        button_a1 = Button(f_cur, text="Aaron")
        button_a2 = Button(f_cur, text="Jim")
    
    lbl_Players.pack() #Pack this first to be on top
    #-------Expand this list?
    button_a1.pack()
    button_a2.pack()
    #--------Do these after
    lbl_bottom = Label(f_cur, text="^Look its player buttons")
    lbl_bottom.pack()
    #frameTemp.grid(row=1, column=1)
    f_cur.grid(row=1, column=1)

def buttonLoop(list, frame): #Does not work, but we should try something similar
    for i in list.count()-1:
            Button(frame, text=list[i]).pack()
            
top = Tk() #needs to be on top of other code, similar to main()
top.title("Lazie Sports")
top.geometry("1280x720") #Locks the window to the specific resolution
#------------------------------------
f_cur = Frame(top, borderwidth = 2, bg="Black")
f_cur.grid(row=1, column=1)

teamlist = ["WMT", "IML", "IMT", "Testing the length?"]
list_Team1 = ["Sam", "Jack", "John"]
list_Team2 = ["Megan", "Austin", "Allie"]
      
button_1 = Button(top, text=teamlist[0], padx=40, pady=20, command=lambda: changeFrame("button_1"))
button_2 = Button(top, text=teamlist[1], padx=40, pady=20, command=lambda: changeFrame("button_2"))
button_3 = Button(top, text=teamlist[2], padx=40, pady=20, command=lambda: changeFrame("button_3"))
button_4 = Button(top, text=teamlist[3], padx=40, pady=20, command=lambda: changeFrame("button_4"))
#button_5 = Button(top, text=teamlist[3], padx=40, pady=20, command=lambda: buttonLoop(list_Team1, f_cur))
        
#------------------------------
button_1.grid(row=1, column=0)
button_2.grid(row=2, column=0)
button_3.grid(row=3, column=0)
button_4.grid(row=4, column=0)
#button_5.grid(row=5, column=0)

welcome_label = Label(text="Teams")
welcome_label.grid(row=0, column=0)

top.mainloop()

###
'''
# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *


class NewWindow(Toplevel):
	
	def __init__(self, master = None):
		
		super().__init__(master = master)
		self.title("New Window")
		self.geometry("200x200")
		label = Label(self, text ="This is a new Window")
		label.pack()


# creates a Tk() object
master = Tk()

# sets the geometry of
# main root window
master.geometry("200x200")

label = Label(master, text ="This is the main window")
label.pack(side = TOP, pady = 10)

# a button widget which will
# open a new window on button click
btn = Button(master,text ="Click to open a new window")
btn.bind("<Button>",
		lambda e: NewWindow(master))

btn.pack(pady = 10)

# mainloop, runs infinitely
mainloop()

'''
###