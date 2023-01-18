import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, pos, imagePath):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect()

        # basic attributes
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        # state variables for item objects
        self.show_item = False
        self.ability = False
        self.shoot = False
        self.abilityCounter = 20

    def generatePipes():  # *SIMPLIFY
        # x locations = 448 608 736 912 1278 1645 1810 2608 2864
        # y locations = 423 (short) 407 (medium) 423 (long)
        s = "assets/block_pipe_short.png"
        m = "assets/block_pipe_medium.png"
        l = "assets/block_pipe_long.png"
        xPos = [448, 608, 736, 912, 1278, 1645, 1810, 2608, 2864]
        yPos = [423, 407, 391, 391, 407, 407, 391, 423, 423]
        length = [s, m, l, l, m, m, l, s, s]
        pipes = [Block((xPos[i], yPos[i]), length[i])
                 for i in range(len(length))]
        return pipes

    def generatePlatform():
        # x locations = 240, 261, 282, 303 (increments of 21)
        # y location = 360
        mystery = "assets/block_mystery.png"
        tile = "assets/block_tile.png"
        xPos, yPos = [240, 261, 282], 360
        platform = [Block((x, yPos), tile) for x in xPos]
        platform.append(Block((303, yPos), mystery))
        return platform

    def shootFire(self, direction, speed):
        if self.shoot:
            if self.abilityCounter >= 0:
                if direction:
                    self.rect.x += speed
                else:
                    self.rect.x -= speed
                self.abilityCounter -= 1
            else:
                self.shoot = False
                self.abilityCounter = 20
