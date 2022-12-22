import pygame
from userSettings import *
from gameData import *


class Level:
    def __init__(self, currentLevel, surface):
        self.displaySurface = surface
        self.currentLevel = currentLevel
        levelData = levels[currentLevel]
        levelContent = levelData['content']

        self.font = pygame.font.Font(None, 40)
        self.textSurf = self.font.render(levelContent, True, 'White')
        self.textRect = self.textSurf.get_rect(
            center=(displayWidth/2, displayHeight/2))

    def input(self):
        keys = pygame.key.get_pressed()

    def instructions(self):
        self.displaySurface.blit(self.textSurf, self.textRect)
