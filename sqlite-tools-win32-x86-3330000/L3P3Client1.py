from tkinter import *
root = Tk ()
root.title ('Client')
import socket
import atexit
def handle_exit():
    s.close()
atexit.register (handle_exit)
from threading import Thread

import sqlite3
l3p3db = sqlite3.connect ('L3P3db.db')
c = l3p3db.cursor ()

s = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
host = 'localhost'
port = 12345

class Window:
    def __init__ (self):
        self.f1 = Frame (root)
        self.f2 = Frame (root)
        self.userl = Label (root,text = 'User')
        self.userl.grid ()
        self.usere = Entry (root)
        self.usere.grid (row = 0,column = 1)
        self.loginb = Button (root,text = 'Login',command = self.login)
        self.loginb.grid (row = 1)
        self.sendb = Button (self.f1,text = 'Send',command = self.send)
        self.sende = Entry (self.f1)
        self.recvthread = Thread (target = self.receiving, args = (1,))
        c.execute ('SELECT * FROM chatlog')
        rows = c.fetchall ()
        print ('here')
        for r in rows:
            self.templ = Label (self.f2,text = r)
            self.templ.pack (side = TOP)
    def login (self):
        s.connect ((host,port))
        print ('connected')
    ##    username = usere.get ()
    ##    s.sendall (username.encode ())
        self.userl.grid_forget ()
        self.usere.grid_forget ()
        self.loginb.grid_forget ()
        self.f1.grid ()
        self.f2.grid (row = 1)
        self.sende.grid ()
        self.sendb.grid (row = 0,column = 1)
        self.recvthread.start ()
    def send (self):
        global s
        msg_client = self.sende.get ()
        msgl = Label (self.f2,text = 'Client: ' + msg_client)
        msgl.pack (side = TOP)
        s.sendall (msg_client.encode ())
        self.sende.delete (0,END)
    def receiving (self,a):
        while True:
            msg_serv = s.recv (1024)
            msg_serv = msg_serv.decode ()
            msgl = Label (self.f2,text = 'Server: ' + msg_serv)
            msgl.pack (side = TOP)
client1 = Window ()

root.mainloop ()
s.close ()
