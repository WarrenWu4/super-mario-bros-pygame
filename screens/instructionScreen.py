import pygame


class instructionScreen:
    def __init__(self, surface):
        self.displaySurface = surface
        self.font = pygame.font.Font(None, 30)
        self.head = pygame.font.Font(None, 40)
        self.btnColor = (103, 106, 110)
        self.width = surface.get_width()
        self.height = surface.get_height()

    def instructionText(self):
        title = "Controls"
        titleText = self.head.render(title, True, 'White')
        titleRect = titleText.get_rect(center=(self.width/2, 100))
        self.displaySurface.blit(titleText, titleRect)

        instructions = ["UP or SPACE or W = Jump", "DOWN or S = Crouch",
                        "LEFT or A = Move Left", "RIGHT or D = Move Right",
                        "J or X = Shoot", "ESC = Exit Game"]
        height = 200
        for line in instructions:
            instructionText = self.font.render(line, True, 'White')
            instructionRect = instructionText.get_rect(
                center=(self.width/2, height))
            self.displaySurface.blit(instructionText, instructionRect)
            height += 50

    def backButton(self):
        # x pos = width/2 - 200 - 200 and y pos = height/2 + 100 + 50
        self.backBtn = [50, 650, 200, 50]
        pygame.draw.rect(self.displaySurface, self.btnColor, self.backBtn)

        backBtnText = self.font.render("Back", True, 'White')
        # center = xpos+(200/2) ypos+(50/2)
        backBtnRect = backBtnText.get_rect(
            center=(self.backBtn[0]+100, self.backBtn[1]+25))
        self.displaySurface.blit(backBtnText, backBtnRect)

    def getBtnPos(self):
        return self.backBtn[0:2]

    def run(self):
        self.instructionText()
        self.backButton()
