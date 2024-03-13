##import tkinter
##from tkinter import *
##root = Tk ()
##root.title ('Tkinter Screen')
##import sys
##sys.path.append ('/C:/Users/Brandon Tsai/OneDrive/Desktop/Level_2/Snake_Function')





import sqlite3
connection = sqlite3.connect ('SnakeScores.db')
cursor = connection.cursor ()
#root.geometry ('600x600')
def text (msg,x1,y1,msgcol):
    fontobj = pygame.font.SysFont ('Times New Roman',30)
    msgobj = fontobj.render (msg,False,msgcol)
    screen.blit (msgobj,(x1,y1))

first = True
score = 0
go = False
while True:
    if first:
        answer = int (input ('Snake\nSelect an option:\n 1. Start\n 2. High Scores\n 3. Exit\n'))
        if answer == 1:
            go = True
        if answer == 2:
            cursor.execute ('SELECT * FROM HighScores ORDER BY Score DESC LIMIT 5')
            data = cursor.fetchall ()
            print ('High Scores')
            for loop in data:
                print (loop [0])
            answer = int (input ('Select an option:\n 1. Start\n 2. High Scores\n 3. Exit\n'))
        if answer == 3:
            go = False
            break
        first = False
        
    if go:
        from Snake_Function import snakegm
        import pygame
        import random
        pygame.init ()
        from pygame.locals import *
        screen = pygame.display.set_mode ((600,600))
        pygame.display.set_caption ('Pygame Screen')
        print (go)
        score = snakegm ()
##        pygame.quit ()
##        exit ()
        answer = int (input ('Game Over! Your score was '+str (score)+'.\n 1. Restart\n 2. High Scores\n 3. Exit\n'))
        cursor.execute ('INSERT INTO HighScores values ('+str (score)+')')
        connection.commit ()
        go = False
        
    if answer == 1:
        print (go)
        go = True
        print ('restart',go)
    if answer == 2:
        cursor.execute ('SELECT * FROM HighScores ORDER BY Score DESC LIMIT 5')
        data = cursor.fetchall ()
        print ('High Scores')
        print (data)
        for loop in data:
            print (loop [0])
        answer = int (input ('Select an option:\n 1. Start\n 2. High Scores\n 3. Exit\n'))
    if answer == 3:
        go = False
        pygame.quit ()
        break

connection.commit ()
cursor.close ()
connection.close ()
