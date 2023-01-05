import pygame


class Map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets//map.png')
        self.rect = self.image.get_rect()

        # positions map at the bottom
        self.rect.y = (760-self.image.get_height())
