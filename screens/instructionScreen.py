import pygame


class instructionScreen:
    def __init__(self, screen, res, btnColor, headFont, normFont):
        self.screen = screen
        self.res = res
        self.btnColor = btnColor
        self.headFont = headFont
        self.normFont = normFont

    def instructionText(self):
        title = "Controls"
        titleText = self.headFont.render(title, True, 'White')
        titleRect = titleText.get_rect(center=(self.res[0]/2, 100))
        self.screen.blit(titleText, titleRect)

        instructions = ["UP or SPACE or W = Jump", "DOWN or S = Crouch",
                        "LEFT or A = Move Left", "RIGHT or D = Move Right",
                        "J or X = Shoot", "ESC = Exit Game"]
        height = 200
        for line in instructions:
            instructionText = self.normFont.render(line, True, 'White')
            instructionRect = instructionText.get_rect(
                center=(self.res[0]/2, height))
            self.screen.blit(instructionText, instructionRect)
            height += 50  # increment height so new text moves down

    def backButton(self):
        # x pos = width/2 - 200 - 200 and y pos = height/2 + 100 + 50
        self.backBtn = [50, 650, 200, 50]
        pygame.draw.rect(self.screen, self.btnColor, self.backBtn)

        backBtnText = self.normFont.render("Back", True, 'White')
        # center = xpos+(200/2) ypos+(50/2)
        backBtnRect = backBtnText.get_rect(
            center=(self.backBtn[0]+100, self.backBtn[1]+25))
        self.screen.blit(backBtnText, backBtnRect)

    def run(self):
        self.instructionText()
        self.backButton()

    def getBtnPos(self):
        return self.backBtn[0:2]
