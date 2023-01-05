import pygame
import sys

from screens.startScreen import *
from screens.instructionScreen import *
from screens.gameScreen import *

'''intialize screen and clock'''
pygame.init()
res = (1280, 760)  # screen resolution
screen = pygame.display.set_mode(res)
timer = pygame.time.Clock()

'''predefine colors'''
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

'''declare and initialize screen states'''
done = False
startState = True
gameState = False
instState = False

'''initialize screens'''
start_screen = startScreen(screen, res)
inst_screen = instructionScreen(screen, res)
game_screen = gameScreen(screen)

'''game loop'''
while not done:

    '''if user wants to close out of program'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True  # exit out of loop
            pygame.quit()  # then quits pygame
            sys.exit()  # then quits the program

    '''if in starting screen'''
    if startState:
        screen.fill((0, 0, 0))  # resets screen
        start_screen.run()
        # check if buttons were pressed
        startState, gameState, instState = start_screen.checkBtnPress()

    '''if in instruction screen'''
    if instState:
        screen.fill((0, 0, 0))  # resets screen
        inst_screen.run()
        # check if button was pressed
        startState, gameState, instState = inst_screen.checkBtnPress()

    '''If not on start or instruction screen, gameplay screen'''
    if gameState:
        # resets the screen to blue to it covers old sprite image
        screen.fill((107, 140, 255))
        game_screen.run()

        # create mini gameover screen
        if game_screen.win or game_screen.lose:
            # blip the text on screen
            overContent = "Congrats on winning! Click to play again" if game_screen.win else "Game Over! Click to play again"
            over = pygame.font.Font(None, 40)
            overText = over.render(overContent, True, 'White')
            overRect = overText.get_rect(center=(1280/2, 640/2))
            screen.blit(overText, overRect)

            # get the button 1 state
            if pygame.mouse.get_pressed()[0]:
                # reset everything by reinitializing
                game_screen.__init__(screen)

    pygame.display.update()  # updates the screen
    timer.tick(60)  # 60 fps
