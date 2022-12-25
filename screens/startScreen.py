import pygame


class startScreen:
    def __init__(self, surface):
        self.displaySurface = surface
        self.font = pygame.font.Font(None, 40)
        self.btnColor = (103, 106, 110)
        self.width = surface.get_width()
        self.height = surface.get_height()

    def introText(self):
        startText = self.font.render("Repus Oiram Orb", True, 'White')
        startPos = startText.get_rect(center=(self.width/2, self.height/2))
        self.displaySurface.blit(startText, startPos)

    def instructionButton(self):
        # x pos = width/2 - 50 - 200 and y pos = height/2 + 20 + 50
        self.btn1Pos = [390, 450, 200, 50]
        pygame.draw.rect(self.displaySurface, self.btnColor, self.btn1Pos)

        insBtnText = self.font.render("Instructions", True, 'White')
        # center = xpos+(200/2) ypos+(50/2)
        insBtnRect = insBtnText.get_rect(center=(490, 475))
        self.displaySurface.blit(insBtnText, insBtnRect)

    def gameplayButton(self):
        # x pos = width/2 + 50 - 200 and y pos = same as instruction button
        self.btn2Pos = [690, 450, 200, 50]
        pygame.draw.rect(self.displaySurface, self.btnColor, self.btn2Pos)

        gameBtnText = self.font.render("Start Game", True, 'White')
        # center = xpos+(200/2) ypos+(50/2)
        gameBtnRect = gameBtnText.get_rect(center=(790, 475))
        self.displaySurface.blit(gameBtnText, gameBtnRect)

    def run(self):
        self.introText()
        self.instructionButton()
        self.gameplayButton()

    def getBtnPos(self):
        return self.btn1Pos[0:2], self.btn2Pos[0:2]
