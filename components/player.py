import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        # required by pygame to initialize sprite class
        pygame.sprite.Sprite.__init__(self)

        # *sprite path might be different on different os types
        self.image = pygame.image.load('assets\player_idle_right.png')
        self.scalePlayer()
        self.rect = self.image.get_rect(center=pos)

        # movement variables
        self.direction = 1  # facing right by default
        self.speed = 5
        self.gravity = 0.5
        self.jumpSpeed = 10

        # player status
        self.action = ['idle', 'run', 'jump']
        self.dead = False
        self.ground = False

    def input(self):
        keys = pygame.key.get_pressed()

        # have player face left and rescale image
        if keys[pygame.K_LEFT]:
            self.image = pygame.image.load('assets\player_idle_left.png')
            self.scalePlayer()
        # have player face right and rescale image
        if keys[pygame.K_RIGHT]:
            self.image = pygame.image.load('assets\player_idle_right.png')
            self.scalePlayer()

        if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and self.ground:
            self.jump()
        if keys[pygame.K_DOWN]:
            self.crouch()

    def moveLeft(self):
        # collision detection with left bound
        if 0 <= self.rect.x:
            self.rect.x -= 5

    def moveRight(self):
        # subtract by width of image to get true wall detection
        if self.rect.x <= 1280-self.image.get_width():
            self.rect.x += 5

    def scalePlayer(self):
        scaledWidth = self.image.get_width() + 10
        scaledHeight = self.image.get_height() + 10
        self.image = pygame.transform.scale(
            self.image, (scaledWidth, scaledHeight))

    def fall(self):
        pass
