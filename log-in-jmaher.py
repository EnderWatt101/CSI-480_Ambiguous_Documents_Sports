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

username_label = Label(currentFrame, text='Username:')
password_label = Label(currentFrame, text='Password:')

username_label.grid(row=1, column =0, padx=10)
password_label.grid(row=2, column=0, padx=10)

name_var=StringVar()
passw_var=StringVar()

name_var_new=StringVar()
passw_var_new=StringVar()

Users = []

def submit():
 
    name=name_var.get()
    password=passw_var.get()
    #Users.append((name, ",", password))
    #print("The name is : " + name)
    #print("The password is : " + password)
    #print(Users[0])
    name_var.set("")
    passw_var.set("")
    for i in range(len(Users)):
        if name and password in Users[i]:
            print("True")
        else:
            print("False")

def create():
    new_name=name_var_new.get()
    new_password=passw_var_new.get()
    Users.append((new_name, new_password))
    print("The name is : " + new_name)
    print("The password is : " + new_password)
    #print(Users[0])
    name_var_new.set("")
    passw_var_new.set("")
    


def newuser():
    newWindow = Toplevel (top)
    newWindow.title("New User")
    newWindow.geometry("750x250")
    label = Label(newWindow, text='Log in',  padx=20, pady=20)
    label.config(width=50)
    username_label = Label(newWindow, text='Username:')
    password_label = Label(newWindow, text='Password:')
    username_label.grid(row=1, column =0, padx=10)
    password_label.grid(row=2, column=0, padx=10)
    name_entry = Entry(newWindow,textvariable = name_var_new, font=('calibre',10,'normal'))
    passw_entry=Entry(newWindow, textvariable = passw_var_new, font = ('calibre',10,'normal'), show = '*')
    name_entry.grid(row=1, column =1)
    passw_entry.grid(row=2, column=1)
    label.grid(row=0, column=0)
    sub_btn=Button(newWindow,text = 'Create New User', command = create)
    sub_btn.grid(row=3, column=0)

    
name_entry = Entry(currentFrame,textvariable = name_var, font=('calibre',10,'normal'))
passw_entry=Entry(currentFrame, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

name_entry.grid(row=1, column =1)
passw_entry.grid(row=2, column=1)

sub_btn=Button(currentFrame,text = 'Submit', command = submit)
sub_btn.grid(row=3, column=0)

new_user = Button(top, text="New User?", padx=40, pady=20, command = newuser)
new_user.grid(row=4, column=0)

top.mainloop()