import pygame

class Pipe(pygame.sprite.Sprite):

    def __init__(self, type, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/block_pipe_{}.png".format(type))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.bottom = pos[0], pos[1]
        

def generatePipes():
    # 448 608 736 912 1278 1645 1810 2608 2864 
    pipes = [
            Pipe("short", (448, 455)), 
            Pipe("medium", (608, 455)), 
            Pipe("long", (736, 455)),  
            Pipe("long", (912, 455)),
            Pipe("medium", (1278, 455)),  
            Pipe("medium", (1645, 455)),  
            Pipe("long", (1810, 455)),
            Pipe("short", (2608, 455)),
            Pipe("short", (2864, 455)),
            ]

    return pipes