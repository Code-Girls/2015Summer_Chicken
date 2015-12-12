#1 import library
import pygame
from pygame.locals import *
import math
import random

#2 initialize the game
pygame.init()
width,height = 756,650
screen = pygame.display.set_mode((width,height))
keys = [False,False]
eggShellPosition = [200,600]
chickLose = []
healthvalue=100
pygame.mixer.init()
gameEnd = 1
timersp = 100
timersp1 = 0
#win
chick1 = []
#lose
chick2 = []
# array of chicken
chickPosition = [[350,100]]
# array of speed5
speed = [[0]]
#3 load images
seconds = 0
background = pygame.image.load("resources/images/background.png")
eggShell = pygame.image.load("resources/images/eggshell.png")
chicken = pygame.image.load("resources/images/thankyou.png")
chickWin = pygame.image.load("resources/images/chickwin.png")
chickLose = pygame.image.load("resources/images/chickLose.png")
healthbar = pygame.image.load("resources/images/healthbar.png")
health = pygame.image.load("resources/images/health.png")
gameover = pygame.image.load("resources/images/gameover.png")
youwin = pygame.image.load("resources/images/youwin.png")
    

    #3.1 load music
pygame.mixer.music.load('resources/audio/bgm.wav')
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.25)
shout = pygame.mixer.Sound("resources/audio/shout.wav")
shout.set_volume(0.15)
# 4 keep looping through
running = 1 
exitcode = 0
time = 0
period = 100
chickLostTime = 0
while running:
    time += 1
    # increase speed
    for sp in speed:
        sp[0] += 0.1
    #draw the screen element
    screen.blit(background,(0,0))
    screen.blit(eggShell,(eggShellPosition[0],eggShellPosition[1]))
    #draw chick
    for chickpos in chickPosition:
        screen.blit(chicken,chickpos)
    # add a chick
    if time % period == 0:
        chickPosition.append([random.randint(30,700),60])
        speed.append([3])
        period -= 5
        if period < 70:
            period = 70
                            
    # draw health bar
    screen.blit(healthbar, (4,5))
    for health1 in range(healthvalue-0):
        screen.blit(health, (health1+6,8))
    #  Draw clock
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((68000-pygame.time.get_ticks())/60000)+":"+str((68000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright=[635,5]
    screen.blit(survivedtext, textRect)
    # Move chicken
    i = 0
    for chickpos in chickPosition:
        chickpos[1] += speed[i][0]
        if chickpos[1] > 580:
            healthvalue -= 20
            chickPosition.pop(i)
            speed.pop(i)
            chick1.append([chickpos[0],chickpos[1]])
            shout.play()
    for chick in chick1:
        screen.blit(chickLose,(chick[0],chick[1]))
        seconds += 1
        if seconds == 5:
            chick1.remove(chick)
            seconds = 0

    i += 1
    #check for collisions
    eggshellrect=pygame.Rect(eggShell.get_rect())
    eggshellrect.top=eggShellPosition[1]
    eggshellrect.left=eggShellPosition[0]
    for chickpos in chickPosition:
        chickrect=pygame.Rect(chicken.get_rect())
        chickrect.top=chickpos[1]
        chickrect.left=chickpos[0]
        index = 0
        if chickrect.colliderect(eggshellrect):
            healthvalue += 10
            chickPosition.pop(index)
            speed.pop(index)
            screen.blit(chickWin,(eggShellPosition[0],eggShellPosition[1]))
        index += 1

     # move eggshell
    for event in pygame.event.get():
        if event.type == USEREVENT+1:
            for chick in chick1:
                chick.remove(chick)
        if event.type==pygame.KEYDOWN:
            if event.key==K_RIGHT:
                keys[0]=True
            elif event.key==K_LEFT:
                keys[1]=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                keys[0]=False
            elif event.key==pygame.K_LEFT:
                keys[1]=False
                          
    if keys[0]:
        eggShellPosition[0]+=10
    elif keys[1]:
        eggShellPosition[0]-=10
     
    # win/lose check
    if healthvalue<0:
        running=0
        exitcode=0
    if healthvalue>194:
        running=0
        exitcode=1
    if pygame.time.get_ticks()>= 68000:
        running=0
        exitcode=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
# Win/Lose display
while gameEnd:
    if exitcode==0:
        screen.blit(gameover,(0,0))
        gameEnd = 0
    if exitcode==1:
        screen.blit(youwin,(0,0))
        gameEnd = 0
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        




