import pygame


class Fireball(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/power_fireball.png")
        self.rect = self.image.get_rect()

        self.rect.x = pos[0]
        self.rect.y = pos[1] 
        self.abilityCounter = 20
        self.shoot = False

    def fire(self, direction, speed):
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
