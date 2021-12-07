from tkinter import *
from tkinter import ttk
from typing import List

#from PIL.Image import new
#from tkinter import tkfont
# ------------------------------
# Ambiguous Documents
# Software Engineering
# Coding Project: Recreating IM Leagues
# Evan McCarthy, Jakob Watt, Tegan McBride, Jack Maher, Christian Gruyon 
# ------------------------------
# Combining the code from multiple files to help integrate the main

class sport():
    def __init__(self, sportNameIn):
        self.sportName = sportNameIn
        self.teamList = [team("Washing Machine Team"), team("Drying Machine Team"), team("IM Team")]
    def addTeam(self, team):
        self.teamList.append(team)
    def removeTeam(self, teamName):
        for i in range(len(self.teamList)):
            if self.teamList[i].getTeamName() == teamName:
                del self.teamList[i]
        else:
            print("ERROR: class \"Sport\"")
    def getSportName(self):
        return self.sportName
    def getTeamList(self):
        return self.teamList

class team():
    def __init__(self, teamNameIn):
        self.teamName = teamNameIn
        self.playerList = [player("Default"), player("Player")]
    def addPlayer(self,player):
        self.playerList.append(player)
    def removePlayer(self, playerName):
        for i in range(len(self.playerList)):
            if self.playerList[i].getPlayerName() == playerName:
                del self.playerList[i]
        else:
            print("ERROR: class \"team\"")
    def getTeamName(self):
        return self.teamName
    def getPlayerList(self):
        return self.playerList

class player():
    def __init__(self, playerNameIn):
        self.playerName = playerNameIn
    def getPlayerName(self):
        return self.playerName

def forgetWig(wig):
    for widget in wig.winfo_children():
        widget.destroy()

def sportTabPress(sportNameIn): ###TODO: Need to add another change frame inside to show players when each team is selected
    thisSportName = str(sportNameIn)
    sportNotebook = ttk.Notebook(notebook)
    notebook.add(sportNotebook, text=thisSportName)
    notebook.select(sportNotebook)
    tempFrame = Frame(sportNotebook, width= 800, height=200)
    title = Label(tempFrame, text="Teams:", font=("Arial",25))
    title.pack()
    for i in range(len(sportData)):# Creates buttons for each sport
        if thisSportName == sportData[i].getSportName():
            for j in range(len(sportData[i].getTeamList())): #Each Team
                tempButton = Button(tempFrame, text=sportData[i].getTeamList()[j].getTeamName(), command=lambda i=i, j=j:teamButtonPress(sportData[i].getSportName(),sportData[i].getTeamList()[j].getTeamName()), font=("Arial",15)) #Add command
                tempButton.pack()
    for i in range(len(tabFrameList)):
        if thisSportName == tabFrameList[i][0]:
            notebook.select(tabFrameList[i][1])
            return
    tabFrameList.append([thisSportName, sportNotebook])
    sportNotebook.add(tempFrame, text=thisSportName + " Home")
    sportNotebook.select(sportNotebook)

def teamButtonPress(sportNameIn, teamNameIn):#TODO FIX ALL THIS
    internalNotebook = None
    for i in range(len(tabFrameList)):
        if sportNameIn == tabFrameList[i][0]:
            internalNotebook = tabFrameList[i][1]
            break
    tempFrame = Frame(internalNotebook, width= 800, height=400)
    title = Label(tempFrame, text="Players:", font=("Arial",25))
    title.pack()
    for i in range(len(sportData)):#Each sport
        if sportNameIn == sportData[i].getSportName():
            for j in range(len(sportData[i].getTeamList())):
                if teamNameIn == sportData[i].getTeamList()[j].getTeamName():
                    for k in range(len(sportData[i].getTeamList()[j].getPlayerList())):
                        tempButton = Button(tempFrame, text=sportData[i].getTeamList()[j].getPlayerList()[k].getPlayerName(), font=("Arial",15))
                        tempButton.pack()


    internalNotebook.add(tempFrame, text=sportNameIn + ": " + teamNameIn)


    #forgetWig(internamTempFrame)
    
def submit():
    name=name_var.get()
    password=passw_var.get()
    global bool_signedIn
    name_var.set("")
    passw_var.set("")
    for i in range(len(Users)):
        if name and password in Users[i]:
            bool_signedIn = True
            login_window.destroy()
        else:
            bool_signedIn = False

def newuser1():
    name=name_var.get()
    password=passw_var.get()
    Users.append((name, password))

def create(w):
    new_name=name_var_new.get()
    new_password=passw_var_new.get()
    Users.append((new_name, new_password))
    print("The name is : " + new_name)
    print("The password is : " + new_password)
    name_var_new.set("")
    w.withdraw()
    passw_var_new.set("")
    
def newuser():
    newWindow = Tk()
    newWindow.title("New User")
    newWindow.geometry("750x250")
    sub_btn=Button(newWindow,text = 'Create New User', command = create())
    label = Label(newWindow, text='Log in',  padx=20, pady=20)
    label.config(width=50)
    username_label = Label(newWindow, text='Username:')
    password_label = Label(newWindow, text='Password:')
    name_entry = Entry(newWindow,textvariable = name_var_new, font=('calibre',10,'normal'))
    passw_entry=Entry(newWindow, textvariable = passw_var_new, font = ('calibre',10,'normal'), show = '*')
    name_entry.grid(row=1, column =1)
    passw_entry.grid(row=2, column=1)
    label.grid(row=0, column=0)
    username_label.grid(row=1, column=0, padx=10)
    password_label.grid(row=2, column=0, padx=10)
    sub_btn.grid(row=3, column=0)
    newWindow.mainloop()

#Sports
tennis = sport("Tennis")
basketball = sport("Basketball")
frisbee = sport("Frisbee")
sportData = [tennis,basketball]

# NEEDED!!!
tabFrameList = []
buttonList = []

bool_signedIn = False
login_window = Tk()
name_var=StringVar()
passw_var=StringVar()
name_var_new=StringVar()
passw_var_new=StringVar()

Users = ["jakob, password", "evan, password", "christian, password", "tegan, password", "jack, password"]

#Init Frames
loginFrame = Frame(login_window, borderwidth = 2)
#-----------Sub Items
lbl_init= Label(loginFrame, text='Log in',  padx=20, pady=20)
lbl_init.config(width=50)
username_label = Label(loginFrame, text='Username:')
password_label = Label(loginFrame, text='Password:')
sub_btn = Button(loginFrame,text = 'Submit', command = lambda:submit())
new_user =Button(loginFrame, text="New User?", padx=40, pady=20, command = newuser)
name_entry = Entry(loginFrame,textvariable = name_var, font=('calibre',10,'normal'))
passw_entry= Entry(loginFrame, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

lbl_init.grid(row=0, column=0)
loginFrame.grid(row=1, column=1)
username_label.grid(row=1, column =0, padx=10)
password_label.grid(row=2, column=0, padx=10)
name_entry.grid(row=1, column =1)
passw_entry.grid(row=2, column=1)
sub_btn.grid(row=3, column=0)
new_user.grid(row=4, column=0)

login_window.mainloop()

#print("HHH" + str(bool_signedIn))
if(bool_signedIn == True):

    #-----Evans Code:
    top = Tk()
    top.title("Lazie Sports")

    notebook = ttk.Notebook(top)
    notebook.pack(pady=10, expand=True)
    topFrame = Frame(notebook, width= 800, height=400)
    currentFrame = Frame(notebook, borderwidth = 2, bg="Black", width= 800, height=400)
    for i in range(len(sportData)):
        print("each sport button: " + sportData[i].getSportName())
        buttonList.append(Button(topFrame, text=sportData[i].getSportName(), command=lambda i=i: sportTabPress(sportData[i].getSportName()), font=("Arial",15)).grid(row=i+1, column=0))
    welcome_label = Label(topFrame, text="Sports", font=("Arial",25))
    welcome_label.grid(row=0, column=0)
    notebook.add(topFrame, text='Home')
    top.mainloop()

    #-----
'''
    top = Tk()
    top.title("Lazie Sports")
    mainFrame = Frame(top, borderwidth = 2, bg="Black")
    #-----------Sub items
    button_1 = Button(top, text=teamlist[0], padx=40, pady=20, command=lambda: changeFrame("button_1"))
    button_2 = Button(top, text=teamlist[1], padx=40, pady=20, command=lambda: changeFrame("button_2"))
    button_3 = Button(top, text=teamlist[2], padx=40, pady=20, command=lambda: changeFrame("button_3"))
    button_4 = Button(top, text=teamlist[3], padx=40, pady=20, command=lambda: changeFrame("button_4"))
    welcome_label = Label(text="Teams")
    name_label = Label(text="The Ambiguous Documents")

    mainFrame.grid(row=1, column=1)
    button_1.grid(row=1, column=0)
    button_2.grid(row=2, column=0)
    button_3.grid(row=3, column=0)
    button_4.grid(row=4, column=0)
    welcome_label.grid(row=0, column=0)
    name_label.grid(row=5, column=0)

    #button_lobo.grid(row=6, column=0)
    top.mainloop()
'''

