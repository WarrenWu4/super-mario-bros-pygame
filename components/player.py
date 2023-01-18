import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, res):
        # required by pygame to initialize sprite class
        # *sprite path might be different on different os types
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player_idle_right.png')
        self.rect = self.image.get_rect()

        # basic attributes
        self.res = res

        # player attributes
        self.rect.x = 40
        self.rect.y = res[1]-50
        self.groundLevel = res[1]-50
        self.rect.width = 23
        self.rect.height = 30

        # movement variables
        self.direction = 1  # 0 is left 1 is right
        self.speed = 5
        self.grav = 5
        self.jumpCount = 15

        # player states
        self.blocked = 0  # 0 = not blocked 1 = left blocked 2 = right blocked
        self.jumping = False
        self.falling = False
        self.ground = True
        self.onPipe = False

    '''Checking Functions'''

    def checkInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and (self.ground or self.onPipe):
            self.jumping = True

    def checkGround(self):
        if self.rect.y == self.groundLevel:
            self.ground = True
        else:
            self.ground = False

    '''Action Functions'''

    def gravity(self):  # falling
        # if it's in the air have gravity activate
        if self.rect.y < self.groundLevel:
            self.rect.y += self.grav
        # correct itself so it doesn't go below ground
        elif self.rect.y+self.grav > self.groundLevel:
            self.rect.y = self.groundLevel

        if self.falling:  # if falling fall below ground level
            self.rect.y += 30

    def jump(self):  # jumping
        # more parabolic movement
        if self.jumping:
            if self.jumpCount >= 0:
                self.rect.y -= self.jumpCount**2 * 0.1
                self.jumpCount -= 1
            else:
                self.jumping = False
                self.jumpCount = 15

    def left(self, speed):
        if self.rect.x >= 0:
            self.rect.x -= speed

    def right(self, speed):
        if self.rect.x <= self.res[0]-self.image.get_width():
            self.rect.x += speed

    def updateSprite(self):
        # if facing right
        if self.direction:
            if self.jumping:
                self.image = pygame.image.load('assets/player_jump_right.png')
            else:
                self.image = pygame.image.load('assets/player_idle_right.png')
        # otherwise if facing left
        else:
            if self.jumping:
                self.image = pygame.image.load('assets/player_jump_left.png')
            else:
                self.image = pygame.image.load('assets/player_idle_left.png')
        # if falling (directionless)
        if self.falling:
            self.image = pygame.image.load('assets/player_falling.png')

    def run(self):
        # check action functions
        self.jump()
        self.gravity()
        self.updateSprite()

        # check checking functions
        self.checkGround()
        self.checkInput()
