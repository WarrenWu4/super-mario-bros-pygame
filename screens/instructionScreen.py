import pygame


class instructionScreen:
    def __init__(self, screen, res):

        # basic attributes
        self.screen = screen
        self.res = res

        # button attributes
        self.btnColor = (103, 106, 110)
        self.btnWidth = 200
        self.btnHeight = 50

        # text attributes
        self.headFont = pygame.font.Font(None, 40)
        self.normFont = pygame.font.Font(None, 30)
        self.textHeight = 50

    def instructionText(self):
        # title text
        title = "Controls"
        titleText = self.headFont.render(title, True, 'White')
        titleRect = titleText.get_rect(center=(self.res[0]/2, self.textHeight))
        self.screen.blit(titleText, titleRect)

        # controls text
        textHeight = self.textHeight*2
        instructions = ["UP or SPACE or W = Jump", "DOWN or S = Crouch",
                        "LEFT or A = Move Left", "RIGHT or D = Move Right",
                        "J or X = Shoot", "ESC = Exit Game"]
        for line in instructions:
            instructionText = self.normFont.render(line, True, 'White')
            instructionRect = instructionText.get_rect(
                center=(self.res[0]/2, textHeight))
            self.screen.blit(instructionText, instructionRect)
            textHeight += 50  # increment height so new text moves down

    def backButton(self):

        # specify coordinates
        xPos = self.res[0] - (self.res[0] - 50)
        yPos = self.res[1] - 110

        # create button background
        self.backBtn = [xPos, yPos, self.btnWidth, self.btnHeight]
        pygame.draw.rect(self.screen, self.btnColor, self.backBtn)

        # create button text
        backBtnText = self.headFont.render("Back", True, 'White')
        centerPos = (xPos+(self.btnWidth/2), yPos+(self.btnHeight/2))
        backBtnRect = backBtnText.get_rect(center=centerPos)
        self.screen.blit(backBtnText, backBtnRect)

    def checkBtnPress(self):

        # for simplicity sake
        btnX, btnY = self.backBtn[0:2]
        mouseX, mouseY = pygame.mouse.get_pos()

        # check if the button is pressed
        if pygame.mouse.get_pressed()[0]:
            if btnX <= mouseX <= btnX+self.btnWidth and btnY <= mouseY <= btnY+self.btnHeight:
                return (True, False, False)  # navigate back to starting screen

        # otherwise stay on instruction screen
        return (False, False, True)

    def run(self):
        # run all texts / buttons
        self.instructionText()
        self.backButton()
