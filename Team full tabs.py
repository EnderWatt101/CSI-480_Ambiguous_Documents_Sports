from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar
# ------------------------------
# Ambiguous Documents
# Software Engineering
# Coding Project: Recreating IM Leagues
# Evan McCarthy, Jakob Watt, Tegan McBride, Jack Maher, Christian Gruyon
# ------------------------------


class sport():
    def __init__(self, sportNameIn):
        self.sportName = sportNameIn
        self.teamList = []
    def addTeam(self, team):
        self.teamList.append(team)
    def removeTeam(self, teamName):
        for i in range(len(self.teamList)):
            if self.teamList[i].getTeamName() == teamName:
                del self.teamList[i]
        else:
            print("error")
    def getSportName(self):
        return self.sportName
    def getTeamList(self):
        return self.teamList
    
class team():
    def __init__(self, teamNameIn):
        self.teamName = teamNameIn
        self.playerList = []
    def addPlayer(self,player):
        self.playerList.append(player)
    def removePlayer(self, playerName):
        for i in range(len(self.playerList)):
            if self.playerList[i].getPlayerName() == playerName:
                del self.playerList[i]
        else:
            print("error")
    def getTeamName(self):
        return self.teamName
    def getPlayerList(self):
        return self.playerList

class player():
    def __init__(self, playerNameIn):
        self.playerName = playerNameIn
    def getPlayerName(self):
        return self.playerName



##SPORTDATA

tennis = sport("Tennis")
tennis_t1 = team("Racket Masters")
tennis_t1.addPlayer(player("Wilson"))
tennis_t1.addPlayer(player("Megan"))
tennis_t2 = team("Ping + Pong")
tennis_t2.addPlayer(player("Teddy"))
tennis_t2.addPlayer(player("Koby"))
tennis.addTeam(tennis_t1)
tennis.addTeam(tennis_t2)

basketball = sport("Basketball")
basketball_t1 = team("Ballerz")
basketball_t1.addPlayer(player("Charles"))
basketball_t1.addPlayer(player("Joey"))
basketball_t2 = team("Gus's Globetrotters")
basketball_t2.addPlayer(player("Olivia"))
basketball_t2.addPlayer(player("Allison"))
basketball_t3 = team("Toon Squad")
basketball_t3.addPlayer(player("Buggs Bunny"))
basketball_t3.addPlayer(player("That one duck bastard"))
basketball_t3.addPlayer(player("Literally an alien"))
basketball.addTeam(basketball_t1)
basketball.addTeam(basketball_t2)
basketball.addTeam(basketball_t3)

frisbee = sport("Frisbee")
frisbee_t1 = team("Compact Disks")
frisbee_t1.addPlayer(player("Wonderwall"))
frisbee_t1.addPlayer(player("Shrek 2: The Musical"))
frisbee_t2 = team("Digital Video Disks")
frisbee_t2.addPlayer(player("Godzilla"))
frisbee_t2.addPlayer(player("Monty Python and the Holy Grail"))
frisbee.addTeam(frisbee_t1)
frisbee.addTeam(frisbee_t2)

sportData = [tennis,basketball, frisbee]

def forgetWig(wig):
    for widget in wig.winfo_children():
        widget.destroy()

def sportTabPress(sportNameIn): ###TODO: Need to add another change frame inside to show players when each team is selected
    thisSportName = str(sportNameIn)
    sportNotebook = ttk.Notebook(notebook)
    for i in range(len(tabFrameList)):
        print("WATCHEHEE")
        print(tabFrameList[i][0])
        if thisSportName == tabFrameList[i][0]:
            notebook.select(tabFrameList[i][1])
            print("areadyhere")
            return
    print("werwwww")
    print(thisSportName)
    notebook.add(sportNotebook, text=thisSportName)
    notebook.select(sportNotebook)
    tempFrame = Frame(sportNotebook, width= 800, height=200)
    title = Label(tempFrame, text="Teams:", font=("Arial",25))
    title.pack(padx=10, pady=10)
    for i in range(len(sportData)):#Each sport
        print(sportData[i].getSportName())
        print("1aswds" + thisSportName + sportNameIn)
        if thisSportName == sportData[i].getSportName():
            print("gether")
            for j in range(len(sportData[i].getTeamList())): #Each Team
                tempButton = Button(tempFrame, text=sportData[i].getTeamList()[j].getTeamName(), command=lambda i=i, j=j:teamButtonPress(sportData[i].getSportName(),sportData[i].getTeamList()[j].getTeamName()), font=("Arial",15)) #Add command
                tempButton.pack(padx=10, pady=10)
            #this should only exit for loop and go through rest of func
            print("Image " + str(i))
            calendarLabel = Label(tempFrame, image=imageList[i])
            calendarLabel.pack(padx=10, pady=10)
            calwidget = Calendar(tempFrame, selectmode = 'day',
               year = 2021, month = 12,
               day = 9, firstweekday = "sunday", showweeknumbers = False)
            calwidget.pack(padx=10, pady=10)
            print("You should see this then another")
    print("this is the other you should see")#see above
    print(thisSportName)
    #HHH
    tabFrameList.append([thisSportName, sportNotebook])
    sportNotebook.add(tempFrame, text=thisSportName + " Home")

def teamButtonPress(sportNameIn, teamNameIn):#TODO FIX ALL THIS
    internalNotebook = None
    for i in range(len(tabFrameList)):
        if sportNameIn == tabFrameList[i][0]:
            internalNotebook = tabFrameList[i][1]
            break
    tempFrame = Frame(internalNotebook, width= 800, height=400)

    title = Label(tempFrame, text="Players:", font=("Arial",25))
    title.pack(padx=10, pady=10)


    for i in range(len(sportData)):#Each sport
        if sportNameIn == sportData[i].getSportName():
            for j in range(len(sportData[i].getTeamList())):
                if teamNameIn == sportData[i].getTeamList()[j].getTeamName():
                    for k in range(len(sportData[i].getTeamList()[j].getPlayerList())):
                        tempButton = Button(tempFrame, text=sportData[i].getTeamList()[j].getPlayerList()[k].getPlayerName(), font=("Arial",15))
                        tempButton.pack(padx=10, pady=10)


    internalNotebook.add(tempFrame, text=sportNameIn + ": " + teamNameIn)
    #sportNotebook.select(internalNotebook)


    #forgetWig(internamTempFrame)
    

top = Tk() #needs to be on top of other code, similar to main()
top.title("Lazie Sports")

notebook = ttk.Notebook(top)
notebook.pack(pady=10, expand=True)
topFrame = Frame(notebook, width= 800, height=400)

TennisCalendar = ImageTk.PhotoImage(Image.open("Tennis.png").resize((300,205), Image.ANTIALIAS))
BasketballCalendar = ImageTk.PhotoImage(Image.open("Basketball.png").resize((300,205), Image.ANTIALIAS))
FrisbeeCalendar = ImageTk.PhotoImage(Image.open("Frisbee.png").resize((300,205), Image.ANTIALIAS))
imageList = [TennisCalendar, BasketballCalendar, FrisbeeCalendar]


currentFrame = Frame(notebook, borderwidth = 2, bg="Black", width= 800, height=400)
#teamlist = []
sportList = ["Tennis", "Kickball", "Basketball", "Soccer"]
sportDict = {"Tennis": [{}, "ten2", "ten3"], "Kickball": ["kick1", "kick2", "kick3"], "Basketball": ["bask1", "bask2", "bask3"], "Soccer": ["socc1", "socc2", "socc3"]}

list_Tennis = ["WMT", "IML", "TMP"]
list_Kickball = ["WMT", "IML", "TMP"]

tabFrameList = []#list for holding tabs to refrence later

buttonList = []

for i in range(len(sportData)):#Each sport
    print("each sport button: " + sportData[i].getSportName())
    buttonList.append(Button(topFrame, text=sportData[i].getSportName(), command=lambda i=i: sportTabPress(sportData[i].getSportName()), font=("Arial",15)).grid(row=i+1, column=0, padx=10, pady=10))




welcome_label = Label(topFrame, text="Sports", font=("Arial",25)) #"Changed Washing Machine Team" to "Teams"
welcome_label.grid(row=0, column=0)

notebook.add(topFrame, text='Home')

top.mainloop()
