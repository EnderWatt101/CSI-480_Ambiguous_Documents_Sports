from tkinter import *
from tkinter import ttk
from typing import List
#from PIL import Image, ImageTk

#------------------
bool_signedIn = False
def submit():
    name=name_var.get()
    password=passw_var.get()
    global bool_signedIn
    #-------------
    name_var.set("")
    passw_var.set("")
    #print(len(Users))
    for i in range(len(Users)):
        #print("apple")
        if name and password in Users[i]:
            #print("banana")
            bool_signedIn = True
            #print(bool_signedIn)
        else:
            #print("orange")
            bool_signedIn = False
            #print(bool_signedIn)

def newuser():

    name=name_var.get()
    password=passw_var.get()
    Users.append((name, password))
    #print(Users)

def forgetWig(wig):
    for widget in wig.winfo_children():
        widget.destroy()

def changeFrame(frame):
    forgetWig(mainFrame)
    frameTemp = Frame(top)
    lbl_Players = Label(mainFrame, text="Players:")
    if frame == "button_1":    
        button_a1 = Button(mainFrame, text="Sam")
        button_a2 = Button(mainFrame, text="Jack")
    elif frame == "button_2":
        button_a1 = Button(mainFrame, text="Megan")
        button_a2 = Button(mainFrame, text="Lobo")
    elif frame == "button_3":
        button_a1 = Button(mainFrame, text="Jack")
        button_a2 = Button(mainFrame, text="Jill")
    elif frame == "button_4":
        button_a1 = Button(mainFrame, text="Aaron")
        button_a2 = Button(mainFrame, text="Jim")
    elif frame == "button_lobo":
        button_a1 = Button(mainFrame, text="Lobo")
        button_a2 = Button(mainFrame, text="Lobo!")
        #image_label2 = Label(mainFrame, image=test2)
        #image_label2.pack()
    lbl_Players.pack() #Pack this first to be on top
    #-------Expand this list?
    button_a1.pack()
    button_a2.pack()
    #--------Do these after
    lbl_bottom = Label(mainFrame, text="^Look its player buttons")
    lbl_bottom.pack()
    frameTemp.grid(row=1, column=1)
    mainFrame.grid(row=1, column=1)



login = Tk()
#Variables
teamlist = ["WMT", "IML", "IMT", "Geese"]
list_Team1 = ["Sam", "Jack", "John"]
list_Team2 = ["Megan", "Austin", "Allie"]
#bool_signedIn = FALSE
#image1 = Image.open("jack.jpg")
#image2 = Image.open("lobo.jpg")
#image1 = image1.resize((50, 25), Image.ANTIALIAS)
#test = ImageTk.PhotoImage(image1)
#test2 = ImageTk.PhotoImage(image2)
name_var=StringVar()
passw_var=StringVar()
Users = []

#Init Frames
loginFrame = Frame(login, borderwidth = 2, bg="Black")
#-----------Sub Items
label = Label(loginFrame, text='Log in',  padx=20, pady=20)
label.config(width=50)
username_label = Label(loginFrame, text='Username:')
password_label = Label(loginFrame, text='Password:')
sub_btn=Button(loginFrame,text = 'Submit', command = lambda:submit())
new_user = Button(loginFrame, text="New User?", padx=40, pady=20, command = newuser)
name_entry = Entry(loginFrame,textvariable = name_var, font=('calibre',10,'normal'))
passw_entry=Entry(loginFrame, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')


loginFrame.grid(row=1, column=1)
label.grid(row=0, column=0)
username_label.grid(row=1, column =0, padx=10)
password_label.grid(row=2, column=0, padx=10)
name_entry.grid(row=1, column =1)
passw_entry.grid(row=2, column=1)
sub_btn.grid(row=3, column=0)
new_user.grid(row=4, column=0)


login.mainloop()

#print("HHH" + str(bool_signedIn))
if(bool_signedIn == True):

    top = Tk()
    top.title("Lazie Sports")
    mainFrame = Frame(top, borderwidth = 2, bg="Black")
    #-----------Sub itenms
    button_1 = Button(top, text=teamlist[0], padx=40, pady=20, command=lambda: changeFrame("button_1"))
    button_2 = Button(top, text=teamlist[1], padx=40, pady=20, command=lambda: changeFrame("button_2"))
    button_3 = Button(top, text=teamlist[2], padx=40, pady=20, command=lambda: changeFrame("button_3"))
    button_4 = Button(top, text=teamlist[3], padx=40, pady=20, command=lambda: changeFrame("button_4"))
    welcome_label = Label(text="Teams")
    name_label = Label(text="The Ambiguous Documents")
    #button_lobo = Button(top, image=test, padx=40, pady=20, command=lambda: changeFrame("button_lobo"))
    #image_label = Label(image=test); image_label.image = test

    #Build Grids
    mainFrame.grid(row=1, column=1)

    button_1.grid(row=1, column=0)
    button_2.grid(row=2, column=0)
    button_3.grid(row=3, column=0)
    button_4.grid(row=4, column=0)
    welcome_label.grid(row=0, column=0)
    name_label.grid(row=5, column=0)

    #button_lobo.grid(row=6, column=0)
    top.mainloop()

