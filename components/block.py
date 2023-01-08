import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, pos, imagePath):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect()

        # basic attributes
        self.rect.x = pos[0]
        self.rect.y = pos[1]
