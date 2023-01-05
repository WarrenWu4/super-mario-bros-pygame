import pygame


class startScreen:
    def __init__(self, screen, res):

        # basic attributes
        self.screen = screen
        self.res = res

        # button attributes
        self.btnColor = (103, 106, 110)
        self.btnWidth = 200
        self.btnHeight = 50

        # font attributes
        self.headFont = pygame.font.Font(None, 40)

    def introText(self):
        startText = self.headFont.render("Repus Oiram Orb", True, 'White')
        startPos = startText.get_rect(center=(self.res[0]/2, self.res[1]/2))
        self.screen.blit(startText, startPos)

    def instructionButton(self):

        # specify coordinates
        xPos = self.res[0]/2 - self.btnWidth - 50
        yPos = self.res[1]/2 + self.btnHeight + 20

        # create button background
        self.btn1Pos = [xPos, yPos, self.btnWidth, self.btnHeight]
        pygame.draw.rect(self.screen, self.btnColor, self.btn1Pos)

        # create button text
        insBtnText = self.headFont.render("Instructions", True, 'White')
        centerPos = (xPos+(self.btnWidth/2), yPos+(self.btnHeight/2))
        insBtnRect = insBtnText.get_rect(center=centerPos)
        self.screen.blit(insBtnText, insBtnRect)

    def gameplayButton(self):

        # specify coordinates
        xPos = self.res[0]/2 - self.btnWidth + 250
        yPos = self.res[1]/2 + self.btnHeight + 20

        # create button background
        self.btn2Pos = [xPos, yPos, self.btnWidth, self.btnHeight]
        pygame.draw.rect(self.screen, self.btnColor, self.btn2Pos)

        # create button text
        gameBtnText = self.headFont.render("Start Game", True, 'White')
        centerPos = (xPos+(self.btnWidth/2), yPos+(self.btnHeight/2))
        gameBtnRect = gameBtnText.get_rect(center=centerPos)
        self.screen.blit(gameBtnText, gameBtnRect)

    def checkBtnPress(self):

        # for simplicity sake
        btn1X, btn1Y = self.btn1Pos[0:2]
        btn2X, btn2Y = self.btn2Pos[0:2]
        mouseX, mouseY = pygame.mouse.get_pos()

        # check if one of the buttons were pressed
        if pygame.mouse.get_pressed()[0]:
            if btn1X <= mouseX <= btn1X+self.btnWidth and btn1Y <= mouseY <= btn1Y+self.btnHeight:
                return (False, False, True)  # navigate to instructions
            if btn2X <= mouseX <= btn2X+self.btnWidth and btn2Y <= mouseY <= btn2Y+self.btnHeight:
                return (False, True, False)  # navigate to gameplay

        # otherwise stay on starting screen
        return (True, False, False)

    def run(self):
        # run all text / buttons
        self.introText()
        self.instructionButton()
        self.gameplayButton()
