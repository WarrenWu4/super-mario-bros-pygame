import pygame
import sys
from userSettings import *
from level import *
from player import *

'''intialize screen and clock'''
pygame.init()
# gets variables from userSettings.py
display = pygame.display.set_mode((displayWidth, displayHeight))
timer = pygame.time.Clock()

game = Level(1, display)
sprites = pygame.sprite.Group()
player = Player((displayWidth/2, displayHeight/2))
sprites.add(player)

'''game loop'''
while True:

    '''look for any user in76put'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # updates the position of player
    player.input()
    # resets the screen to black to it covers old sprite image
    display.fill('black')
    # displays new sprite image
    sprites.draw(display)

    pygame.display.update()  # update the display
    timer.tick(60)  # for every second 60 frames will pass
