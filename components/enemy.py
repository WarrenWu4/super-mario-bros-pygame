import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/enemy_alive.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.bottom = pos[1]-25
        self.dead = False
        self.direction = -1

    def walk(self):
        if self.dead:
            return
        if self.direction == -1:
            self.rect.x -= 1
        else:
            self.direction += 1
   
    def steppedOn(self, player):
        if pygame.sprite.collide_rect(self, player) and (self.rect.top >= player.rect.centery):
            self.fall()

    def fall(self):
        self.rect.y += 3
        self.image = pygame.image.load('assets/enemy_dead.png')
        self.dead = True

    def run(self, player):
        self.walk()
        self.steppedOn(player)