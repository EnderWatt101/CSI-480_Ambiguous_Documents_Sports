from tkinter import *
from tkinter import ttk
from typing import List
# ------------------------------
# Ambiguous Documents
# Software Engineering
# Coding Project: Recreating IM Leagues
# Evan McCarthy, Jakob Watt, Tegan McBride, Jack Maher, Christian Gruyon
# ------------------------------


def newuser():
    name=name_var.get()
    password=passw_var.get()
    Users.append((name, password))
    print(Users)

def submit():
    name=name_var.get()
    password=passw_var.get()
    profile=[name, password]
    print(profile, "   ", Users[0])
    name_var.set("")
    passw_var.set("")
    if(len(Users) >0):
        for i in range(len(Users)):
            print("HEREEE")
            if profile == Users[i]:
                print("True")
                #go to new page @Jakob
            else:
                print("False")
                user_not_found.grid(row=4, column=1)
    else:
        print("False")
        print("HERE2")
        user_not_found.grid(row=4, column=1)

top = Tk()
top.title("Sports For The Less Sporty")
top.configure(bg='maroon')
#setup fancy windows

currentFrame = Frame(top, borderwidth = 50, bg="maroon")
currentFrame.grid(row=0, column=0)
label = Label(currentFrame, text='Log in',  padx=20, pady=20, bg="maroon", fg='white')
label.config(width=50)

label.grid(row=0, column=0)

username_label = Label(currentFrame, text='Username:', bg="maroon", fg='white')
password_label = Label(currentFrame, text='Password:', bg="maroon", fg='white')

name_var=StringVar()
passw_var=StringVar()
Users = []
profile=["Tegan", "isCool"]
Users.append(profile)
print(Users)
user_not_found = Label(currentFrame, text='Incorrect password or username. Please try again.', bg="maroon", fg='white')
name_entry = Entry(currentFrame,textvariable = name_var, font=('calibre',10,'normal'))
passw_entry= Entry(currentFrame, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
sub_btn=Button(currentFrame,text = 'Submit',bg='maroon', fg='white', command = submit)
new_user = Button(top, text="New User?", padx=40, pady=20, command = newuser, bg='maroon', fg='white')

username_label.grid(row=1, column =0, padx=10)
password_label.grid(row=2, column=0, padx=10)
name_entry.grid(row=1, column =1)
passw_entry.grid(row=2, column=1)
sub_btn.grid(row=3, column=0)
new_user.grid(row=5, column=0)

top.mainloop()