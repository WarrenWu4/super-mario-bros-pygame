import pygame


class Map(pygame.sprite.Sprite):
    def __init__(self, res):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets//map.png')
        self.rect = self.image.get_rect()

        # basic attributes
        self.res = res

        # default set position
        self.rect.x = 0  # left
        self.rect.y = (res[1] - self.image.get_height())  # bottom

    def correctPos(self):
        # correct position if past leftmost or rightmost point
        if self.rect.x > 0:
            self.rect.x = 0
        if self.rect.x < self.res[0]-self.image.get_width():
            self.rect.x = round(self.res[0]-self.image.get_width(), -1)

    def right(self, speed):
        self.rect.x -= speed

    def left(self, speed):
        self.rect.x += speed

    def run(self):
        self.correctPos()
