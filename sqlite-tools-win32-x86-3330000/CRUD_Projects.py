import sqlite3
import tkinter
from tkinter import *
from tkinter import messagebox
root = Tk ()
root.title ('Screen')
#root.geometry ('600x600')

connection = sqlite3.connect ('login.db')
cursor = connection.cursor ()

cursor.execute ('CREATE TABLE IF NOT EXISTS logins (Name text,Username text,Password text)')

f1 = Frame (root,width = 300,height = 100)
lf = Frame (root,width = 300,height = 100)
rf = Frame (root,width = 300,height = 100)
resf = Frame (root,width = 300,height = 100)
df = Frame (root,width = 300,height = 100)
status = StringVar ()
f1.pack ()
l1 = Label (f1,text = 'Select one of the buttons below to Login or Register')
l1.grid ()

lf1 = Label (lf,text = 'Login')
u = Label (lf,text = 'Username')
p = Label (lf,text = 'Password')
lfe1 = Entry (lf)
lfe2 = Entry (lf)

resl = Label (resf,text = 'Reset Password')
u2 = Label (resf,text = 'Username')
u2e = Entry (resf)
newpl = Label (resf,text = 'New Password')
newp = Entry (resf)

rf1 = Label (rf,text = 'Register')
n = Label (rf,text = 'Name')
u1 = Label (rf,text = 'Username')
p1 = Label (rf,text = 'Password')
cp = Label (rf,text = 'Confirm Password')
rfe1 = Entry (rf)
rfe2 = Entry (rf)
rfe3 = Entry (rf)
rfe4 = Entry (rf)
s1 = Label (rf,textvariable = status)

def deleteacc ():
    user = lfe1.get ()
    cursor.execute ("DELETE FROM logins WHERE Username = '"+str(user)+"'")
    connection.commit ()
    messagebox.showinfo ('Account Deleted','Your account has been deleted.')

db = Button (lf,text = 'Delete Account',state = DISABLED,command = deleteacc)

def lsubmit ():
    user = lfe1.get ()
    password = lfe2.get ()
    cursor.execute ('SELECT * FROM logins')
    data = cursor.fetchall ()
    match = False
    for loop in data:
        if loop [1] == user and loop [2] == password:
            messagebox.showinfo ('Login Successful','Welcome, '+loop [0]+'!')
            match = True
            db.config (state = NORMAL)
    if match == False:
        messagebox.showerror ('Login Failed','Record not found. Try again.')

lfs = Button (lf,text = 'Submit',command = lsubmit)

def ressubmit ():
    user = u2e.get ()
    print (user)
    newpas = newp.get ()
    print (newpas)
    cursor.execute ('SELECT * FROM logins')
    data = cursor.fetchall ()
    match = False
    for loop in data:
        if loop [1] == user:
            print (loop [1],user)
            cursor.execute ("UPDATE logins SET Password = '"+str (newpas)+"' WHERE Username = '"+str (user)+"'")
            #print ("UPDATE logins SET Password = '"+str (newpas)+"' WHERE Username = '"+str (user)+"'")
            connection.commit ()
            messagebox.showinfo ('Password Change','Your password has been changed.')
            match = True
    if match == False:
        messagebox.showerror ('Reset Failed','User not found.')

ressub = Button (resf,text = 'Submit',command = ressubmit)

def reset ():
    lf.forget ()
    resf.pack ()
    resl.grid (columnspan = 2)
    u2.grid (row = 1)
    u2e.grid (row = 1,column = 1)
    newpl.grid (row = 2)
    newp.grid (row = 2,column = 1)
    ressub.grid (row = 3,columnspan = 2)

resb = Button (lf,text = 'Reset Password',command = reset)

def rsubmit ():
    name = rfe1.get ()
    user = rfe2.get ()
    password = rfe3.get ()
    cpass = rfe4.get ()
    if password == cpass:
        cursor.execute ('INSERT INTO logins values ("'+name+'","'+user+'","'+password+'")')
        status.set ('Registration Successful')
        connection.commit ()
    else:
        status.set ('Password does not match.')

rfs = Button (rf,text = 'Submit',command = rsubmit)

def login ():
##    check = True
##    while check == True:
##        user = input ('Username: ')
##        password = input ('Password: ')
##        cursor.execute ('SELECT * FROM logins')
##        data = cursor.fetchall ()
##        for loop in data:
##            if loop [1] == user and loop [2] == password:
##                print ('Welcome,',loop [0]+'!')
##                check = False
##            else:
##                print ('Record not found. Try again.')

    f1.pack_forget ()
    lf.pack ()
    lf1.grid (columnspan = 2)
    u.grid (row = 1)
    p.grid (row = 2)
    lfe1.grid (row = 1,column = 1)
    lfe2.grid (row = 2,column = 1)
    lfs.grid (row = 3)
    resb.grid (row = 3,column = 1)
    db.grid (row = 4,columnspan = 2)

def home ():
        rf.pack_forget ()
        rf1.forget ()
        f1.pack ()
        l1.grid ()
        b1.grid (row = 1)
        b2.grid (row = 2)

rh = Button (rf,text = 'Return to Home',command = home)

def register ():
##    name = input ('Name: ')
##    user = input ('Username: ')
##    password = input ('Password: ')
##    cursor.execute ('INSERT INTO logins values ("'+name+'","'+user+'","'+password+'")')
##    print ('SIGN-UP SUCESSFUL')

    global home
    f1.pack_forget ()
    rf.pack ()
    rf1.grid (columnspan = 2)
    n.grid (row = 1)
    u1.grid (row = 2)
    p1.grid (row = 3)
    cp.grid (row = 4)
    rfs.grid (row = 5)
    rfe1.grid (row = 1,column = 1)
    rfe2.grid (row = 2,column = 1)
    rfe3.grid (row = 3,column = 1)
    rfe4.grid (row = 4,column = 1)
    rh.grid (row = 5,column = 1)
    s1.grid (row = 6,column = 1)

##response = int (input ('LOGIN MENU\n1. LOGIN\n2. SIGNUP\nEnter your choice (1/2): '))
##if response == 1:
##    login ()
##if response == 2:
##    register ()

b1 = Button (f1,text = 'Login',command = login)
b1.grid (row = 1)
b2 = Button (f1,text = 'Register',command = register)
b2.grid (row = 2)

root.mainloop ()
connection.commit ()
cursor.close ()
connection.close ()
