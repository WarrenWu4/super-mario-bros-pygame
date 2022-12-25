import pygame


class Map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets//map.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = (760-self.image.get_height())

    def scroll(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] and self.rect.x > (1280-self.image.get_width()):
            self.rect.x -= 5
        if keys[pygame.K_LEFT] and self.rect.x < 0:
            self.rect.x += 5
