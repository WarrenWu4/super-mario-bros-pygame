import pygame
from userSettings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        # required by pygame to initialize sprite class
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets\player.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.moveLeft()
        if keys[pygame.K_RIGHT]:
            self.moveRight()
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            self.jump()
        if keys[pygame.K_DOWN]:
            self.crouch()

    def moveLeft(self):
        # collision detection with left bound
        if 0 <= self.rect.x:
            self.rect.x -= 5

    def moveRight(self):
        # subtract by width of image to get true wall detection
        if self.rect.x <= displayWidth-self.image.get_width():
            self.rect.x += 5

    def jump(self):
        self.rect.y -= 5

    def crouch(self):
        self.image = pygame.image.load(
            'assets\player_crouch.png').convert_alpha()
