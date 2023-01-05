import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        # required by pygame to initialize sprite class
        pygame.sprite.Sprite.__init__(self)

        # *sprite path might be different on different os types
        self.image = pygame.image.load('assets/player_idle_right.png')
        self.rect = self.image.get_rect(center=pos)
        self.scalePlayer()

        # movement variables
        self.speed = 5
        self.grav = 5
        self.jumpCount = 15
        self.jumping = False

    def scalePlayer(self):
        scaledWidth = self.image.get_width() + 10
        scaledHeight = self.image.get_height() + 10
        self.image = pygame.transform.scale(
            self.image, (scaledWidth, scaledHeight))

    def jump(self):
        # more parabolic movement
        if self.jumping:
            if self.jumpCount >= 0:
                self.image = pygame.image.load("assets\player_jump_left.png")
                self.scalePlayer()
                self.rect.y -= self.jumpCount**2 * 0.1
                self.jumpCount -= 1
            else:
                self.jumping = False
                self.jumpCount = 15

    def gravity(self):
        # if it's in the air have gravity activate
        if self.rect.y+self.grav < 710:
            self.image = pygame.image.load('assets\player_falling.png')
            self.scalePlayer()
            self.rect.y += self.grav
        elif self.rect.y+self.grav > 710:
            self.rect.y = 710

    # def gravity(self):
    #     if not self.ground:
    #         self.rect.y += self.grav

    def fall(self):
        self.image = pygame.image.load('assets\player_falling.png')
        self.scalePlayer()
        self.rect.y += 25
