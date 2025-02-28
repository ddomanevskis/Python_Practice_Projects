import pygame
from pygame.locals import *
from SimpleButton import *
import sys

GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oButton = SimpleButton(window, (150, 30), 'pygame/buttons/images/buttonUp.png', 'pygame/buttons/images/buttonDown.png')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if oButton.handleEvent(event):
            print('User clicked the button')

    window.fill(GRAY)

    oButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)