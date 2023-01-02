import pygame


class gameScreen:
    def __init__(self, surface, map, player):

        self.display = surface

        self.map = map
        self.mapSprite = pygame.sprite.Group()
        self.mapSprite.add(map)

        self.player = player
        self.playerSprite = pygame.sprite.GroupSingle()
        self.playerSprite.add(player)

    def floorHoles(self):
        holeCoords = [(-455, -465), (-730, -755), (-1805, -1815)]
        # check if player is in the right position
        if self.player.ground and self.player.rect.x == 644:
            for hole in holeCoords:
                if hole[0] >= self.map.rect.x >= hole[1]:
                    self.player.fall()

    def run(self):
        if not self.player.dead:
            self.map.scroll(self.player, self.player.speed)
            self.player.updateStatus()
            self.player.gravity()
            self.player.input()
            self.floorHoles()
            if self.player.jump:
                if self.player.jumpHeight >= 0:
                    self.player.rect.y -= (self.player.jumpHeight)
                    self.player.jumpHeight -= 1
                else:
                    self.player.jumpHeight = 12
                    self.player.jump = False

        self.mapSprite.draw(self.display)
        self.playerSprite.draw(self.display)
