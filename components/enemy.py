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
            self.rect.x += 1

    def changeDirection(self):
        self.direction *= -1
   
    def steppedOn(self, player):
        if pygame.sprite.collide_rect(self, player) and (self.rect.top >= player.rect.centery):
            self.fall()
            

    def fall(self):
        self.dead = True
        self.rect.y += 1
        self.image = pygame.image.load('assets/enemy_dead.png')
        if self.rect.y == 1000:
            self.dead = False
        

    def run(self, player):
        self.walk()
        self.steppedOn(player)
        if self.dead:
            self.fall()

def generateEnemies(res):
    return [
        Enemy((380, res[1])), 
        Enemy((500, res[1])), 
        Enemy((800, res[1])), 
        Enemy((820, res[1])), 
        Enemy((1475, res[1])),
        Enemy((2045, res[1])),
        Enemy((2065, res[1])),
        Enemy((2085, res[1])),
        Enemy((2735, res[1])),
        Enemy((2355, res[1])),
        ]

