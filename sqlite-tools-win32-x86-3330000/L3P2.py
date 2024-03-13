from tkinter import *
import time,random
root = Tk ()
root.title ('Screen')

import sqlite3
connection = sqlite3.connect ('MatchingLead.db')
cursor = connection.cursor ()
#cursor.execute ('DELETE FROM leaderboard WHERE time = 29')

revealed = 0
rev1 = 50
rev2 = 50
matches = 0

#f2 = Frame (root)
class tile:
    def __init__ (self,r,c,n,col):
        global f2
        self.num = n
        self.textvar = StringVar ()
        self.textvar.set ('')
        self.color = col
        self.r = r
        self.c = c
        self.b = Button (root,textvar = self.textvar,fg = self.color,height = 2,width = 10,command = self.check)
        self.state = 'not matched'
    def check (self):
        global revealed,rev1,rev2,blist,matches
        if self.state == 'not matched':
            if revealed < 2:
                if revealed == 0:
                    rev1 = self.num
                if revealed == 1:
                    rev2 = self.num
                self.textvar.set (bdict [self.num])
                revealed += 1
            elif revealed >= 2:
                print (revealed)
                blist [rev1].textvar.set ('')
                blist [rev2].textvar.set ('')
                revealed = 1
                rev1 = self.num
                rev2 = 50
                self.textvar.set (bdict [self.num])
            if revealed == 2:
                try:
                    if rev1 != rev2:
                        if bdict [rev1] == bdict [rev2]:
                            #blist [rev1].configure (fg = 'green') #can't change to green?
                            #blist [rev2].configure (fg = 'green')
                            blist [rev1].state = 'matched'
                            blist [rev2].state = 'matched'
                            rev1 = 50
                            rev2 = 50
                            print (rev1,rev2)
                            revealed = 0
                            matches += 1
                except:
                    pass
    def display (self):
        self.b.grid (row = self.r,column = self.c)
        
bdict = {}
setlist1 = ['a','b','c','d','e','f','g','h','a','b','c','d','e','f','g','h']
random.shuffle (setlist1)
bnum = 0
blist = []

start = False
for row in range (1,5,1):
    for column in range (0,4,1):
        b1 = tile (row,column,bnum,'black')
        blist.append (b1)
        bdict [bnum] = setlist1 [bnum]
        bnum += 1

def ghome ():
    global homeb,timel1,blist,bdict,bnum,setlist1,matches
    matches = 0
    for loop in blist:
        loop.b.grid_forget ()
    homeb.grid_forget ()
    timel1.grid_forget ()
    startb.grid ()
    leadb.grid (row = 1)
    endb.grid (row = 2)
    bnum = 0
    bdict = {}
    blist = []
    random.shuffle (setlist1)
    for row in range (1,5,1):
        for column in range (0,4,1):
            b1 = tile (row,column,bnum,'black')
            blist.append (b1)
            bdict [bnum] = setlist1 [bnum]
            bnum += 1
timeval = StringVar ()
timel1 = Label (root,textvariable = timeval)
homeb = Button (root,text = 'Home',command = ghome)

def lhome ():
    global lhomeb,startb,leadb
    for loop in blist:
        loop.b.grid_forget ()
    lhomeb.grid_forget ()
    lmsg.grid_forget ()
    startb.grid ()
    leadb.grid (row = 1)
    endb.grid (row = 2)
lhomeb = Button (root,text = 'Home',command = lhome)
ltext = StringVar ()
lmsg = Message (root,textvariable = ltext)

def startgame ():
    global start,bdict,setlist1,bnum,blist,matches
    #start = True
    #if start == True:
    startb.grid_forget ()
    leadb.grid_forget ()
    endb.grid_forget ()
    resetb.grid_forget ()
    timel1.grid (column = 3)
    for loop in blist:
        loop.display ()
    game = True
    starttime = time.time ()
    homeb.grid (row = 0,column = 0)
    while game:
        curtime = int (time.time () - starttime)
        timeval.set ('Timer: ' + str (curtime))
        if matches == 8:
            cursor.execute ('INSERT INTO leaderboard values (' + str (curtime) + ')')
            game = False
        root.update ()
    print (bdict)

def seelead ():
    startb.grid_forget ()
    leadb.grid_forget ()
    endb.grid_forget ()
    resetb.grid_forget ()
    lhomeb.grid ()
    lmsg.grid (row = 1)
    cursor.execute ('SELECT * FROM leaderboard ORDER BY time DESC LIMIT 5')
    data = cursor.fetchall ()
    print (data)
    cursor.execute ('SELECT MAX(time) FROM leaderboard')
    data = cursor.fetchall ()
    print ('Max:',data)
    cursor.execute ('SELECT MIN(time) FROM leaderboard')
    data = cursor.fetchall ()
    print ('Min:',data)
    temptext = ''
    place = 1
    for loop in data:
        temptext = temptext + '\n' + str (place) + '. ' + str (loop [0])
        place += 1
    ltext.set ('Top 5 Scores:' + temptext)

def end ():
    connection.commit ()
    cursor.close ()
    root.destroy ()

def reset ():
    #cursor.execute ('DROP TABLE leaderboard')
    cursor.execute ('DROP DATABASE MatchingLead.db')

startb = Button (root,text = 'Start',command = startgame)
leadb = Button (root,text = 'Leaderboard',command = seelead)
endb = Button (root,text = 'Quit',command = end)
resetb = Button (root,text = 'Reset',command = reset)
startb.grid ()
leadb.grid (row = 1)
endb.grid (row = 2)
resetb.grid (row = 3)

root.mainloop ()
