import pygame

from components.player import *
from components.map import *
from components.tile import *


class gameScreen:
    def __init__(self, screen, res):

        # basic attributes
        self.screen = screen
        self.res = res

        # game attributes
        self.win = False
        self.lose = False

        # map sprite attributes
        self.mapSprite = pygame.sprite.Group()
        self.map = Map(res)
        self.mapSprite.add(self.map)

        # player sprite attributes
        self.playerSprite = pygame.sprite.GroupSingle()
        self.player = Player(res)
        self.playerSprite.add(self.player)

        # platform sprite attributes
        self.platformSprite = pygame.sprite.Group()
        platformPos = [res[0]/3, 3*res[1]/4]
        self.blocks = []
        self.luckyBlock = Tile(platformPos, 'assets/block_mystery.png')
        self.blocks.append(self.luckyBlock)
        for i in range(4):
            platformPos[0] += self.luckyBlock.image.get_width()
            self.blocks.append(Tile(platformPos, "assets/block_tile.png"))
        self.platformSprite.add(self.blocks)

    def update(self):
        # for simplicity sake
        p = self.player
        m = self.map
        width = self.res[0]
        rightBorder = round(width-m.image.get_width(), -1)

        # check input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            # update player facing direction
            p.direction = 1
            # if player is on the leftmost edge of map and not halfway up OR
            # if player is on the rightmost edge of map and not halfway down
            # +5 for reentry purposes exiting edge will result in p.rect.x == width/2
            if m.rect.x == 0 and p.rect.x+5 <= width/2 or m.rect.x == rightBorder and p.rect.x >= width/2:
                p.right(p.speed)
            # otherwise move the map
            else:
                m.right(p.speed)
                for block in self.blocks:
                    block.right(p.speed)

        if keys[pygame.K_LEFT]:
            # same logic when moving left
            p.direction = 0
            if m.rect.x == 0 and p.rect.x <= width/2 or m.rect.x == rightBorder and p.rect.x-5 >= width/2:
                p.left(p.speed)
            else:
                m.left(p.speed)
                for block in self.blocks:
                    block.left(p.speed)

        # set win to true if player passes castle door
        if m.rect.x == rightBorder and p.rect.x == width-130:
            self.win = True

        # check holes
        holeCoords = [(-745, -755), (-1015, -1040), (-2090, -2095)]
        # check if player is in the right position
        if p.ground and p.rect.x == width/2:
            # loop through to see if player has fallen in hole
            for hole in holeCoords:
                if hole[0] >= m.rect.x >= hole[1]:
                    p.falling, self.lose = True, True

    def collisionDetection(self):
        # set dokill argument to false by default
        blockCollide = pygame.sprite.spritecollide(
            self.player, self.platformSprite, False)
        if blockCollide:
            self.player.jumping = False
            self.player.jumpCount = 15

    def run(self):
        # keep running basic updates as long as no win and no lose
        if not self.win and not self.lose:
            self.update()  # game logic/main input checker
            self.collisionDetection()  # detects collision between platform and player
            self.map.run()  # map specific functions
            self.player.run()  # player specific functions

        self.mapSprite.draw(self.screen)
        self.platformSprite.draw(self.screen)
        self.playerSprite.draw(self.screen)
