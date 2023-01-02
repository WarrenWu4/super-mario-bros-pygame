import pygame
import sys

from screens.startScreen import *
from screens.instructionScreen import *
from screens.gameScreen import *

from components.player import *
from components.map import *

'''intialize screen and clock'''
pygame.init()
display = pygame.display.set_mode((1280, 760))
timer = pygame.time.Clock()

'''declare and initialize screen states'''
start = True
gameplay = False
instructions = False

'''initialize gameplay components'''
# player starting position is 40 722
player = Player((40, 722))
map = Map()

'''initialize screens'''
beginScreen = startScreen(display)
controlsInfo = instructionScreen(display)
gaming = gameScreen(display, map, player)

'''game loop'''
while True:

    '''While in starting screen'''
    while start:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # if the user clicks 'instructions'
                if btn1Pos[0] <= mouse[0] <= btn1Pos[0]+200 and btn1Pos[1] <= mouse[1] <= btn1Pos[1]+50:
                    start, gameplay, instructions = False, False, True
                # if the user clicks 'start'
                if btn2Pos[0] <= mouse[0] <= btn2Pos[0]+200 and btn2Pos[1] <= mouse[1] <= btn2Pos[1]+50:
                    display.fill((0, 0, 0))  # resets screen
                    start, gameplay, instructions = False, True, False

        # get location of mouse (tuple of x y coord)
        mouse = pygame.mouse.get_pos()

        display.fill((0, 0, 0))  # resets screen

        beginScreen.run()
        btn1Pos, btn2Pos = beginScreen.getBtnPos()

        pygame.display.update()
        timer.tick(60)

    '''While on instruction screen'''
    while instructions:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            # if user clicks 'back' button moves then back to starting screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn3Pos[0] <= mouse[0] <= btn3Pos[0]+200 and btn3Pos[1] <= mouse[1] <= btn3Pos[1]+50:
                    start, gameplay, instructions = True, False, False

        mouse = pygame.mouse.get_pos()

        display.fill((0, 0, 0))  # resets screen

        controlsInfo.run()
        btn3Pos = controlsInfo.getBtnPos()

        pygame.display.update()
        timer.tick(60)

    '''If not on start or instruction screen, gameplay screen'''
    while gameplay:

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        # resets the screen to blue to it covers old sprite image
        display.fill((107, 140, 255))

        gaming.run()
        # if player.dead == True:
        #     gameplay = False
        #     pygame.quit()
        #     sys.exit()

        pygame.display.update()  # update the display
        timer.tick(60)  # for every second 60 frames will pass
