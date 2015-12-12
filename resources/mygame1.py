# 1 import library
import pygame
from pygame.locals import *

# 2  initialize the game
pygame.init()
width, height = 640,480
screen = pygame.display.set_mode((width.height))

# 3 load images
player = pygame.image.load("resources/images/dude.png")

# 4 keep looping through
while 1:
    # 5 clear the screeen before drawing it again
    screen.fill(0)
    # 6 draw the screen elements
    screen.blit(player,(100,100))
    # 7 update the screen
    pygame.display.flip()
    # 8 loop through the events
    for event in pygame.event.get():
        # check if the events is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
