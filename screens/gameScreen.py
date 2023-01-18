import pygame

from components.player import *
from components.block import *
from components.enemy import *


class gameScreen:
    def __init__(self, screen, res):
        """basic attributes"""
        self.screen = screen
        self.res = res

        """game data"""
        self.win = False
        self.lose = False

        """creates the map and gives default position"""
        self.map = Block((0, 256), "assets/map.png")
        self.mapSprite = pygame.sprite.GroupSingle(self.map)

        """create player sprite"""
        self.player = Player(res)
        self.playerSprite = pygame.sprite.GroupSingle(self.player)

        """create enemy sprites"""
        self.enemies = generateEnemies(self.res)
        self.enemySprites = pygame.sprite.Group(self.enemies)

        """create pipe sprite"""
        self.pipes = Block.generatePipes()
        self.pipeSprites = pygame.sprite.Group(self.pipes)

        """create platform sprite"""
        self.platform = Block.generatePlatform()
        self.platformSprite = pygame.sprite.Group(self.platform)

        """create item sprite"""
        self.item = Block((303, 360), "assets/power_flower.png")
        self.itemSprite = pygame.sprite.Group(self.item)

        """fireball sprite"""
        self.fireball = Block((0, 0), "assets/power_fireball.png")
        self.fireballSprite = pygame.sprite.Group(self.fireball)

        """ For convienence """
        self.entities = self.pipes + self.platform + \
            self.enemies + [self.item, self.map]
        self.width = self.res[0]
        self.rightBorder = round(self.width-self.map.image.get_width(), -1)

    def input(self, p, m, w, rb):
        # check input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            # update player facing direction
            p.direction = 1
            # if player is on the leftmost edge of map and not halfway up OR
            # if player is on the rightmost edge of map and not halfway down
            # +5 for reentry purposes exiting edge will result in p.rect.x == width/2
            if p.blocked != 2:
                if m.rect.x == 0 and p.rect.x+5 <= w/2 or m.rect.x == rb and p.rect.x >= w/2:
                    p.right(p.speed)
                # otherwise move the map
                else:
                    for entity in self.entities:
                        entity.rect.x -= p.speed

        if keys[pygame.K_LEFT]:
            # same logic when moving left
            p.direction = 0
            if p.blocked != 1:
                if m.rect.x == 0 and p.rect.x <= w/2 or m.rect.x == rb and p.rect.x-5 >= w/2:
                    p.left(p.speed)
                else:
                    for entity in self.entities:
                        entity.rect.x += p.speed

        if keys[pygame.K_x] or keys[pygame.K_j]:
            if self.item.ability and not self.fireball.shoot:
                self.fireball.rect.x = p.rect.x + 6.5
                self.fireball.rect.y = p.rect.y + 5
                self.fireball.shoot = True

    def logic(self, p, m, w, rb):
        """self correcting map position"""
        if m.rect.x > 0:
            m.rect.x = 0
        if m.rect.x < rb:
            m.rect.x = rb

        """set win to true if player passes castle door"""
        if m.rect.x == rb and p.rect.x == w-130:
            self.win = True

        """check holes"""
        holeCoords = [(-745, -755), (-1015, -1040), (-2090, -2095)]
        # loop through to see if player has fallen in hole
        for hole in holeCoords:
            # check if player is in the right position
            if hole[0] >= m.rect.x >= hole[1] and p.rect.x == w/2 and p.ground:
                self.player.falling, self.lose = True, True

        """applies gravity to item"""
        if self.item.show_item and self.item.rect.y < p.groundLevel:
            self.item.rect.y += p.grav

    def collisions(self, p):
        """if player collides with platform tiles cancel jumping"""
        if pygame.sprite.spritecollide(p, self.platformSprite, True):
            p.jumping = False
            p.jumpCount = 15

        """if player collides with mystery block"""
        if pygame.sprite.collide_rect(p, self.platform[3]):
            self.item.show_item = True

        """ player collision with item """
        if pygame.sprite.collide_rect(p, self.item) and self.item.rect.y >= p.groundLevel:
            self.itemSprite.remove(self.item)
            self.item.ability = True

        """ enemy collision detection """
        for enemy in self.enemies:
            if pygame.sprite.collide_rect(enemy, p) and p.ground and not enemy.dead:
                p.falling, self.lose = True, True
            if pygame.sprite.collide_rect(self.fireball, enemy) and self.fireball.shoot:
                enemy.fall()
            if pygame.sprite.spritecollide(enemy, self.pipeSprites, False):
                enemy.changeDirection()

        """ pipes collision detection"""
        p.blocked, p.onPipe = 0, False
        collision_tolerance = 6
        for pipe in self.pipes:
            if p.rect.colliderect(pipe.rect):
                if abs(pipe.rect.top - p.rect.bottom) < collision_tolerance:
                    p.rect.bottom = pipe.rect.top
                    p.onPipe = True
                else:
                    p.blocked = 2 if (pipe.rect.x > p.rect.x) else 1
            if pygame.sprite.collide_rect(pipe, self.fireball):
                self.fireball.abilityCounter, self.fireball.shoot = 20, False

    def run(self):
        """scale any image/sprites"""
        self.player.image = pygame.transform.scale(self.player.image, (23, 26))
        for block in self.platform:
            block.image = pygame.transform.scale(block.image, (21, 21))
        self.fireball.image = pygame.transform.scale(
            self.fireball.image, (18, 18))

        """draws map, player, enemies, items, and misc. blocks as sprites"""
        self.mapSprite.draw(self.screen)
        self.platformSprite.draw(self.screen)
        self.playerSprite.draw(self.screen)
        self.enemySprites.draw(self.screen)
        self.pipeSprites.draw(self.screen)
        if self.item.show_item:
            self.itemSprite.draw(self.screen)
        if self.fireball.shoot:
            self.fireball.shootFire(self.player.direction, self.player.speed)
            self.fireballSprite.draw(self.screen)

        """keep running basic updates as long as no win and no lose"""
        if not self.win and not self.lose:
            self.input(self.player, self.map, self.res[0], self.rightBorder)
            self.logic(self.player, self.map, self.res[0], self.rightBorder)
            self.collisions(self.player)
            self.player.run()  # player specific functions
            for enemy in self.enemies:
                enemy.run(self.player)  # runs enemy specific functions
