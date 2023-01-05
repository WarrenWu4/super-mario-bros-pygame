import pygame
import sys

from screens.startScreen import *
from screens.instructionScreen import *
from screens.gameScreen import *

from components.player import *
from components.map import *

'''intialize screen and clock'''
pygame.init()
res = (1280, 760)  # screen resolution
screen = pygame.display.set_mode(res)
timer = pygame.time.Clock()

'''initializing other settings/predefined variables'''
btnColor = (103, 106, 110)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
headFont = pygame.font.Font(None, 40)
normFont = pygame.font.Font(None, 30)

'''declare and initialize screen states'''
gameLoop = True
startState = True
gameState = False
instState = False

'''initialize gameplay components'''
# player starting position is 40 722
playerStartPos = (40, 722)
player = Player(playerStartPos)
map = Map()

'''initialize screens'''
start_screen = startScreen(screen, res, btnColor, headFont)
inst_screen = instructionScreen(screen, res, btnColor, headFont, normFont)
game_screen = gameScreen(screen, map, player)

'''game loop'''
while gameLoop:

    '''check events globally regardless of state'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            gameLoop = False  # exit out of loop
            pygame.quit()  # then quits pygame
            sys.exit()  # then quits the program

        if event.type == pygame.MOUSEBUTTONDOWN:
            # get location of mouse (tuple of x y coord)
            mouse = pygame.mouse.get_pos()

            # state specific event for startin screen
            if startState:
                # if the user clicks 'instructions'
                if btn1Pos[0] <= mouse[0] <= btn1Pos[0]+200 and btn1Pos[1] <= mouse[1] <= btn1Pos[1]+50:
                    startState, gameState, instState = False, False, True
                # if the user clicks 'start'
                if btn2Pos[0] <= mouse[0] <= btn2Pos[0]+200 and btn2Pos[1] <= mouse[1] <= btn2Pos[1]+50:
                    startState, gameState, instState = False, True, False

            # state specific event for instructions screen
            elif instState:
                # if user clicks 'back' button moves then back to starting screen
                if btn3Pos[0] <= mouse[0] <= btn3Pos[0]+200 and btn3Pos[1] <= mouse[1] <= btn3Pos[1]+50:
                    startState, gameState, instState = True, False, False

    '''if in starting screen'''
    if startState:
        screen.fill((0, 0, 0))  # resets screen
        start_screen.run()
        btn1Pos, btn2Pos = start_screen.getBtnPos()

    '''if in instruction screen'''
    if instState:
        screen.fill((0, 0, 0))  # resets screen
        inst_screen.run()
        btn3Pos = inst_screen.getBtnPos()

    '''If not on start or instruction screen, gameplay screen'''
    if gameState:
        # resets the screen to blue to it covers old sprite image
        screen.fill((107, 140, 255))
        game_screen.run()

        # just create a mini screen within gameplay loop based on conditionals
        if game_screen.win:
            win = pygame.font.Font(None, 40)
            winText = win.render(
                "Congrats on winning! Click to play again", True, 'White')
            winRect = winText.get_rect(center=(1280/2, 640/2))
            screen.blit(winText, winRect)
            # get the button 1 state
            if pygame.mouse.get_pressed()[0]:
                game_screen.win = False
                map.rect.x = 0
                player.rect.x = 40
                player.rect.y = 709
        if game_screen.lose:
            lose = pygame.font.Font(None, 40)
            loseText = lose.render(
                "Game Over! Click to play again", True, 'White')
            loseRect = loseText.get_rect(center=(1280/2, 640/2))
            screen.blit(loseText, loseRect)
            # get the button 1 state
            if pygame.mouse.get_pressed()[0]:
                game_screen.lose = False
                player.dead = False
                map.rect.x = 0
                player.rect.x = 40
                player.rect.y = 709

    pygame.display.update()  # updates the screen
    timer.tick(60)  # 60 fps
