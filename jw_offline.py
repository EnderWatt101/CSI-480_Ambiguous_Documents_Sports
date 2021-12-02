from tkinter import *
from tkinter import ttk
from typing import List
# ------------------------------
# Ambiguous Documents
# Software Engineering
# Coding Project: Recreating IM Leagues
# Evan McCarthy, Jakob Watt, Tegan McBride, Jack Maher, Christian Gruyon
# ------------------------------

top = Tk()
top.title("Sports For The Less Sporty")
#setup fancy windows

currentFrame = Frame(top, borderwidth = 50)
currentFrame.grid(row=0, column=0)

label = Label(currentFrame, text='Log in',  padx=20, pady=20)
label.config(width=50)

label.grid(row=0, column=0)

username_label = Label(currentFrame, text='Username: ')
password_label = Label(currentFrame, text='Password: ')

username_label.grid(row=1, column =0, padx=10)
password_label.grid(row=2, column=0, padx=10)

name_var=StringVar()
passw_var=StringVar()
Users = {}

def login(U):
    #Check the username and password entries for correct use
    name=name_var.get()
    password=passw_var.get()
    if name in U.keys():
        print("YES")
        print(U.values())
    else:
        print("NO")
    
def submit():
    #Use the boxes to generate a user in the dictionary
    name=name_var.get()
    password=passw_var.get()
    Users[name] = password
    print(name)
    print(password)
    name_var.set("")
    passw_var.set("")
    for key in Users:
        print(key+"_")
     
name_entry = Entry(currentFrame,textvariable = name_var, font=('calibre',10,'normal'))
passw_entry=Entry(currentFrame, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

name_entry.grid(row=1, column =1)
passw_entry.grid(row=2, column=1)

sub_btn=Button(currentFrame,text = 'Submit', command = submit)
sub_btn.grid(row=3, column=0)

new_user = Button(top, text="New User?", padx=40, pady=20, command = login(Users))
new_user.grid(row=4, column=0)

top.mainloop()