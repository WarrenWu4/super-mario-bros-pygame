import pygame


class startScreen:
    def __init__(self, screen, res, btnColor, headFont):
        self.screen = screen
        self.res = res
        self.btnColor = btnColor
        self.headFont = headFont

    def introText(self):
        startText = self.headFont.render("Repus Oiram Orb", True, 'White')
        startPos = startText.get_rect(center=(self.res[0]/2, self.res[1]/2))
        self.screen.blit(startText, startPos)

    def instructionButton(self):
        # x pos = width/2 - 50 - 200 and y pos = height/2 + 20 + 50
        self.btn1Pos = [390, 450, 200, 50]
        pygame.draw.rect(self.screen, self.btnColor, self.btn1Pos)

        # overlay text on rectangle
        insBtnText = self.headFont.render("Instructions", True, 'White')
        # center = xpos+(200/2) ypos+(50/2)
        insBtnRect = insBtnText.get_rect(center=(490, 475))
        self.screen.blit(insBtnText, insBtnRect)

    def gameplayButton(self):
        # x pos = width/2 + 50 - 200 and y pos = same as instruction button
        self.btn2Pos = [690, 450, 200, 50]
        pygame.draw.rect(self.screen, self.btnColor, self.btn2Pos)

        # overlay text on rectangle
        gameBtnText = self.headFont.render("Start Game", True, 'White')
        # center = xpos+(200/2) ypos+(50/2)
        gameBtnRect = gameBtnText.get_rect(center=(790, 475))
        self.screen.blit(gameBtnText, gameBtnRect)

    def run(self):
        self.introText()
        self.instructionButton()
        self.gameplayButton()

    def getBtnPos(self):
        return self.btn1Pos[0:2], self.btn2Pos[0:2]
