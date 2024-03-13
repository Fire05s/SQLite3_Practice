import pygame
import random
pygame.init ()
from pygame.locals import *
screen = pygame.display.set_mode ((600,600))
pygame.display.set_caption ('Screen')
def snakegm ():
    def text (msg,x1,y1,msgcol):
        fontobj = pygame.font.SysFont ('Times New Roman',30)
        msgobj = fontobj.render (msg,False,msgcol)
        screen.blit (msgobj,(x1,y1))
    clock = pygame.time.Clock ()
    foodx = (random.randint (0,600) // 20)*20
    foody = (random.randint (0,600) // 20)*20
    snakex = (random.randint (0,600) // 20)*20
    snakey = (random.randint (0,600) // 20)*20
    snakelist = []
    snakelist.append ([snakex,snakey])

    snakef = False
    snakel = False
    snakeb = False
    snaker = False

    score = 0

    time = 60
    timertxt = '60'.rjust (10)
    pygame.time.set_timer (pygame.USEREVENT,1000)
    font = pygame.font.SysFont ('Times New Roman',20)

    def grid ():
        for loop in range (0,600,20):
            pygame.draw.line (screen,(255,255,255),(loop,0),(loop,600))
            pygame.draw.line (screen,(255,255,255),(0,loop),(600,loop))
    print (snakelist)
    while True:
        clock.tick (10)
        screen.fill ((0,0,0))
        screen.blit (font.render (timertxt,True,(0,255,255)),(250,20))
        text ('Score: '+str(score),250,50,(225,0,225))
        grid ()
        snakelist.insert (0,[snakex,snakey])
        snakelist.pop ()
        pygame.draw.rect (screen,(255,255,0),(foodx,foody,20,20))
        for loop1 in snakelist:
            pygame.draw.rect (screen,(0,255,0),(loop1+[20,20]))
        if [snakex,snakey] in snakelist [1:]:
            text ('Game Over!',225,25,(255,0,0))
            pygame.display.update ()
            break
        if snakex == foodx and snakey == foody:
            snakelist.append ([snakex,snakey])
            score = score + 1
            foodx = (random.randint (0,600) // 20)*20
            foody = (random.randint (0,600) // 20)*20
            print (len(snakelist))
            print (snakelist)
            
        if time > 0 and score == 11:
            text ('You Win!',250,30,(0,255,0))
            pygame.display.update ()
            break
        
        if time == 0 and score != 11:
            text ('Game Over!',225,25,(255,0,0))
            pygame.display.update ()
            break
        
        for event in pygame.event.get ():
            if event.type == pygame.USEREVENT:
                time = time - 1
                timertxt = str(time).rjust (10)
            if event.type == pygame.KEYDOWN:
                if event.key == K_w and snakeb != True:
                    snakef = True
                    snakel = False
                    snakeb = False
                    snaker = False
                if event.key == K_a and snaker != True:
                    snakef = False
                    snakel = True
                    snakeb = False
                    snaker = False
                if event.key == K_s and snakef != True:
                    snakef = False
                    snakel = False
                    snakeb = True
                    snaker = False
                if event.key == K_d and snakel != True:
                    snakef = False
                    snakel = False
                    snakeb = False
                    snaker = True
            if event.type == QUIT:
                pygame.quit ()
                exit ()
        if snakef == True:
            snakey = snakey - 20
        if snakeb == True:
            snakey = snakey + 20
        if snaker == True:
            snakex = snakex + 20
        if snakel == True:
            snakex = snakex - 20
        if snakex >= 600 or snakey >= 600 or snakex <= -20 or snakey <= -20:
            text ('Game Over!',225,25,(255,0,0))
            pygame.display.update ()
            break
        pygame.display.update ()
    return score
