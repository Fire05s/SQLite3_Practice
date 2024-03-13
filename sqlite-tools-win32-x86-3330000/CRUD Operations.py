import sqlite3

connection = sqlite3.connect ('crud.db')
cursor = connection.cursor ()

def createtable ():
    cursor.execute ('CREATE TABLE IF NOT EXISTS people (name text, sports1 text, sports2 text, grade integer)')
#createtable ()

def addinfo ():
    cursor.execute ('INSERT INTO people values ("John","Soccer","Basketball",7)')
    cursor.execute ('INSERT INTO people values ("Jane","Tennis","Track",9)')
#addinfo ()

def update ():
    cursor.execute ('UPDATE people SET sports2 = "Racketball" WHERE name = "John"')
#update ()

def read ():
    cursor.execute ('SELECT * FROM people')
    data = cursor.fetchall ()
#    print (data)
    for loop in data:
        print (loop [0][0])
#read ()

def useradd ():
    name = input ('Enter student\'s name: ')
    sports1 = input ('Enter student\'s first sport: ')
    sports2 = input ('Enter student\'s second sport: ')
    grade = input ('Enter student\'s grade: ')
    cursor.execute ('INSERT INTO people values ("'+name+'","'+sports1+'","'+sports2+'","'+grade+'")')
#useradd ()

def delete ():
    cursor.execute ('DELETE FROM people WHERE grade = 9')
#delete ()

connection.commit ()
cursor.close ()
connection.close ()
