import pygame
import random

from components.player import *
from components.block import *
from components.fireball import *
from components.enemy import *
from components.pipe import *


class gameScreen:
    def __init__(self, screen, res):
        """basic attributes"""
        self.screen = screen
        self.res = res

        """game data"""
        self.win = False
        self.lose = False
        self.show_item = False
        self.item_fall = False
        self.item_ground = False
        self.ability = False

        """creates the map and gives default position"""
        self.map_image = pygame.image.load("assets/map.png")
        self.map = self.map_image.get_rect()
        self.map.x, self.map.y = 0, self.res[1]-self.map_image.get_height()

        """create player sprite"""
        self.playerSprite = pygame.sprite.Group()
        self.player = Player(res)
        self.playerSprite.add(self.player)

        """create enemy sprites"""
        self.enemySprites = pygame.sprite.Group()
        self.enemies = [Enemy((500, res[1])), Enemy((800, res[1])), Enemy((1400, res[1]))]
        for enemy in self.enemies:
            self.enemySprites.add(enemy)

        """create pipe sprite"""
        self.pipeSprites = pygame.sprite.Group()
        # 450 610 735 910 1280 1645 1810 2605 2865 
        self.pipes = generatePipes()
        for pipe in self.pipes:
            self.pipeSprites.add(pipe)

        """create platform sprite"""
        self.platformSprite = pygame.sprite.Group()
        platformPos = [res[0]/3, 3*res[1]/4]
        self.blocks, self.lucky = {}, random.randint(0, 3)
        for i in range(4):
            if i == self.lucky:
                self.blocks[i] = Block(platformPos, "assets/block_mystery.png")
            else:
                self.blocks[i] = Block(platformPos, "assets/block_tile.png")
            platformPos[0] += 21
        self.platformSprite.add(self.blocks.values())

        """create item sprite"""
        self.itemSprite = pygame.sprite.Group()
        itemPos = self.blocks[self.lucky].rect[0:2]
        self.blocks[4] = Block(itemPos, "assets/power_flower.png")
        self.itemSprite.add(self.blocks[4])

        """fireball sprite"""
        self.fireballSprite = pygame.sprite.Group()
        self.fireball = Fireball(self.player.rect[0:2])
        self.fireballSprite.add(self.fireball)

        """declare some more convienent variables"""
        self.map_rb = round(self.res[0]-self.map_image.get_width(), -1)

    def input(self):
        # for simplicity sake
        p = self.player
        m = self.map
        width = self.res[0]
        rightBorder = round(width-self.map_image.get_width(), -1)

        # check input
        keys = pygame.key.get_pressed()

        rightOfPipe = False
        leftOfPipe = False
        self.player.onPipe = False
        collision_tolerance = 6
        for pipe in self.pipes:
            if self.player.rect.colliderect(pipe.rect):
                if abs(pipe.rect.top - self.player.rect.bottom) < collision_tolerance:
                    self.player.rect.bottom = pipe.rect.top
                    self.player.onPipe = True
                elif abs(pipe.rect.left - self.player.rect.right) < collision_tolerance:
                    rightOfPipe = True
                elif abs(pipe.rect.right - self.player.rect.left) < collision_tolerance:
                    leftOfPipe = True
        if keys[pygame.K_RIGHT]:
            # update player facing direction
            p.direction = 1
            # if player is on the leftmost edge of map and not halfway up OR
            # if player is on the rightmost edge of map and not halfway down
            # +5 for reentry purposes exiting edge will result in p.rect.x == width/2
            if not rightOfPipe:
                if m.x == 0 and p.rect.x+5 <= width/2 or m.x == rightBorder and p.rect.x >= width/2:
                    p.right(p.speed)
                # otherwise move the map
                else:
                    self.map.x -= p.speed
                    for block in self.blocks.values():
                        block.rect.x -= p.speed
                    for enemy in self.enemies:
                        enemy.rect.x -= p.speed
                    for pipe in self.pipes:
                        pipe.rect.x -= p.speed
        if keys[pygame.K_LEFT]:
            # same logic when moving left
            p.direction = 0
            if not leftOfPipe:
                if m.x == 0 and p.rect.x <= width/2 or m.x == rightBorder and p.rect.x-5 >= width/2:
                    p.left(p.speed)
                else:
                    self.map.x += p.speed
                    for block in self.blocks.values():
                        block.rect.x += p.speed
                    for enemy in self.enemies:
                        enemy.rect.x += p.speed
                    for pipe in self.pipes:
                        pipe.rect.x += p.speed
        if keys[pygame.K_x] or keys[pygame.K_j]:
            if self.ability and not self.fireball.shoot:
                self.fireball.rect.x = self.player.rect.x + self.player.image.get_width()/2
                self.fireball.rect.y = self.player.rect.centery
                self.fireball.shoot = True

    def logic(self):
        """self correcting map position"""
        if self.map.x > 0:
            self.map.x = 0
        if self.map.x < self.map_rb:
            self.map.x = self.map_rb

        """set win to true if player passes castle door"""
        if self.map.x == self.map_rb and self.player.rect.x == self.res[0]-130:
            self.win = True

        """check holes"""
        holeCoords = [(-745, -755), (-1015, -1040), (-2090, -2095)]
        # check if player is in the right position
        if self.player.ground:
            # loop through to see if player has fallen in hole
            for hole in holeCoords:
                if hole[0] >= self.map.x >= hole[1] and self.player.rect.x == self.res[0]/2:
                    self.player.falling, self.lose = True, True

        """applies gravity to item"""
        if self.item_fall and self.blocks[4].rect.y < self.player.groundLevel:
            self.blocks[4].rect.y += self.player.grav
        if self.blocks[4].rect.y >= self.player.groundLevel:
            self.item_ground = True


    def collisions(self):
        """if player collides with platform tiles"""
        platCollide = pygame.sprite.spritecollide(
            self.player, self.platformSprite, True)
        if platCollide:
            self.player.jumping = False
            self.player.jumpCount = 15

        """if player collides with mystery block"""
        blockCollide = pygame.sprite.collide_rect(
            self.player, self.blocks[self.lucky])
        if blockCollide:
            self.show_item = True
            self.item_fall = True
        item_collide = pygame.sprite.collide_rect(self.player, self.blocks[4])
        if item_collide and self.item_ground:
            self.itemSprite.remove(self.blocks[4])
            self.ability = True

        """ if player collides with enemy """
        for enemy in self.enemies:
            if not enemy.dead and self.player.ground:
                if pygame.sprite.collide_rect(enemy, self.player):
                    self.player.falling, self.lose = True, True

        """ if fireball collides with enemy """
        for enemy in self.enemies:
            if not enemy.dead and self.fireball.shoot:
                if pygame.sprite.collide_rect(self.fireball, enemy):
                    enemy.fall()

    def run(self):
        """draws the map as background"""
        self.screen.blit(self.map_image, self.map[0:2])

        """scale any image/sprites"""
        self.player.image = pygame.transform.scale(self.player.image, (23, 26))
        # self.player.rect = self.player.image.get_rect()
        for block in self.blocks.values():
            block.image = pygame.transform.scale(block.image, (21, 21))
        self.fireball.image = pygame.transform.scale(
            self.fireball.image, (18, 18))

        """draws player, enemies, items, and misc. blocks as sprites"""
        self.platformSprite.draw(self.screen)
        if self.show_item:
            self.itemSprite.draw(self.screen)
        if self.fireball.shoot:
            self.fireball.fire(self.player.direction, self.player.speed)
            self.fireballSprite.draw(self.screen)
        self.playerSprite.draw(self.screen)
        self.enemySprites.draw(self.screen)
        self.pipeSprites.draw(self.screen)
        """keep running basic updates as long as no win and no lose"""
        if not self.win and not self.lose:
            self.input()  # input checker
            self.logic()  # runs the game logic
            self.collisions()  # detects collision between platform and player
            self.player.run()  # player specific functions
            for enemy in self.enemies:
                enemy.run(self.player)

        
        