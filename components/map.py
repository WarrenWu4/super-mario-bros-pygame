import pygame


class Map(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets//map.png')
        self.rect = self.image.get_rect()

        # positions map at the bottom
        self.rect.y = (760-self.image.get_height())

    def scroll(self, player, speed):
        keys = pygame.key.get_pressed()

        # scroll right when right key pressed
        if keys[pygame.K_RIGHT]:
            # if player below middle point of left most area of map move player
            if self.rect.x == 0 and -5 <= player.rect.x <= 640:
                player.moveRight()
            # if player above middle point of right most area of map move player
            elif self.rect.x == round(1280-self.image.get_width(), -1) and 620 <= player.rect.x <= 1280:
                player.moveRight()
            else:
                self.rect.x -= speed

        # scroll left when left key pressed
        if keys[pygame.K_LEFT]:
            # if player below middle point of left most area of map move player
            # want it to be a bit offcenter so reentry is easier
            if self.rect.x == 0 and -5 <= player.rect.x <= 650:
                player.moveLeft()
            # if player above middle point of right most area of map move player
            elif self.rect.x == round(1280-self.image.get_width(), -1) and 645 <= player.rect.x <= 1280:
                player.moveLeft()
            # otherwise just move the map
            else:
                self.rect.x += speed
