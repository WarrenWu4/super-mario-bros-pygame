import pygame

from components.player import *
from components.map import *
from components.tile import *


class gameScreen:
    def __init__(self, screen):

        self.win = False
        self.lose = False
        self.screen = screen

        self.mapSprite = pygame.sprite.Group()
        self.map = Map()
        self.mapSprite.add(self.map)

        self.playerSprite = pygame.sprite.GroupSingle()
        self.player = Player((40, 718))  # starting pos is 40, 718
        self.playerSprite.add(self.player)

    def update(self, p, m):
        # p and m shorthand for player and map respectively
        keys = pygame.key.get_pressed()

        # scroll right when right key pressed
        if keys[pygame.K_RIGHT]:
            # update playuer sprite
            p.image = pygame.image.load('assets\player_idle_right.png')
            p.scalePlayer()

            # if player below middle point of left most area of map move player
            if m.rect.x == 0 and -5 <= p.rect.x <= 640:
                if -5 <= p.rect.x:  # detects left wall
                    p.rect.x += p.speed
            # if player above middle point of right most area of map move player
            elif m.rect.x == round(1280-m.image.get_width(), -1) and 620 <= p.rect.x <= 1280:
                if p.rect.x <= 1280 - p.image.get_width():  # detects right wall
                    p.rect.x += p.speed
            # otherwise move all the map pieces
            else:
                m.rect.x -= p.speed

        # scroll left when left key pressed
        if keys[pygame.K_LEFT]:
            # update player sprite
            p.image = pygame.image.load('assets\player_idle_left.png')
            p.scalePlayer()

            # want it to be a bit offcenter so reentry is easier (movement speed factor)
            # if player below middle point of left most area of map move player
            if m.rect.x == 0 and -5 <= p.rect.x <= 650:
                if 0 <= p.rect.x:  # detects left wall
                    p.rect.x -= p.speed
            # if player above middle point of right most area of map move player
            elif m.rect.x == round(1280-m.image.get_width(), -1) and 645 <= p.rect.x <= 1280:
                if p.rect.x <= 1280 - p.image.get_width():  # detects right wall
                    p.rect.x -= p.speed
            # otherwise just move the map
            else:
                m.rect.x += p.speed

        # player jumps when up or space bar or w is pressed
        if keys[pygame.K_UP] or keys[pygame.K_SPACE] or keys[pygame.K_w]:
            if p.rect.y >= 710:
                p.jumping = True

    def fallen(self):
        holeCoords = [(-455, -465), (-730, -755), (-1805, -1815)]
        # check if player is in the right position
        if self.player.rect.y >= 710 and 644 <= self.player.rect.x <= 645:
            # loop through to see if player has fallen in hole
            for hole in holeCoords:
                if hole[0] >= self.map.rect.x >= hole[1]:
                    self.player.fall()
                    self.lose = True

    def collisionDetection(self):
        # set dokill argument to false by default
        # blockCollide = pygame.sprite.collide_rect(self.player)
        # if blockCollide:
        #     self.player.jump = False
        pass

    def run(self):
        # keep running basic updates as long as no win and no lose
        if not self.win and not self.lose:
            self.update(self.player, self.map)
            self.fallen()
            self.player.gravity()
            self.player.jump()
        # self.player.updateStatus()
        # self.player.gravity()
        # self.floorHoles()
        # if self.player.jump:
        #     if self.player.jumpHeight >= 0:
        #         self.player.rect.y -= (self.player.jumpHeight)
        #         self.player.jumpHeight -= 1
        #     else:
        #         self.player.jumpHeight = 12
        #         self.player.jump = False
        # self.collisionDetection()

            # if player reaches castle door then set win to true
            if 1144 <= self.player.rect.x <= 1154 and -2105 >= self.map.rect.x >= -2115:
                self.win = True

        self.mapSprite.draw(self.screen)
        self.playerSprite.draw(self.screen)
