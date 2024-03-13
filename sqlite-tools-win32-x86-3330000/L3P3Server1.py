from tkinter import *
root = Tk ()
root.title ('Server')
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
host = ''
port = 12345
s.bind ((host,port))
s.listen (5)
print ('server is listening')
conn,addr = s.accept ()
print ('connected',addr)
##username = conn.recv (1024)
##username = username.decode ()

class Window:
    def __init__ (self):
        self.f1 = Frame (root)
        self.f2 = Frame (root)
        self.sende = Entry (self.f1)
        self.sendb = Button (self.f1,text = 'Send',command = self.send)
        self.f1.grid ()
        self.f2.grid (row = 1)
        self.sende.grid ()
        self.sendb.grid (row = 0,column = 1)
        self.recvthread = Thread (target = self.receiving, args = (1,))
        self.recvthread.start ()
        c.execute ('SELECT * FROM chatlog')
        rows = c.fetchall ()
        print ('here')
        for r in rows:
            self.templ = Label (self.f2,text = r)
            self.templ.pack (side = TOP)
    def send (self):
        msg_serv = self.sende.get ()
        c.execute ("INSERT INTO chatlog VALUES ('Server:','" + msg_serv + "')")
        l3p3db.commit ()
        msgl = Label (self.f2,text = 'Server: ' + msg_serv)
        msgl.pack (side = TOP)
        conn.sendall (msg_serv.encode ())
        self.sende.delete (0,END)
    def receiving (self,a):
    ##    global username
        while True:
            l3p3db1 = sqlite3.connect ('L3P3db.db')
            c1 = l3p3db1.cursor ()
            msg_client = conn.recv (1024)
            msg_client = msg_client.decode ()
            c1.execute ("INSERT INTO chatlog VALUES ('Client:','" + msg_client + "')")
            l3p3db1.commit ()
            msgl = Label (self.f2,text = 'Client: ' + msg_client)
            msgl.pack (side = TOP)
server1 = Window ()

root.mainloop ()
s.close ()
