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
        if self.map.y >= 709:
            self.player.fall()

    def run(self):
        self.map.scroll(self.player)
        self.player.input()

        self.mapSprite.draw(self.display)
        self.playerSprite.draw(self.display)
