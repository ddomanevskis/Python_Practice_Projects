import pygame
from pygame.locals import *
import sys
import random
from SimpleText import *
from SimpleButton import *
from Ball import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFrameCountLabel = SimpleText(window, (60, 20), 'Program has run through this many loops: ', WHITE)
oFrameCountDisplay = SimpleText(window, (500, 20), '', WHITE)
oRestartButton = SimpleButton(window, (280, 60), 'pgm/buttons/images/buttonUp.png', 'pgm/buttons/images/buttonDown.png')
frameCounter = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if oRestartButton.handleEvent(event):
        frameCounter = 0
    
    oBall.update()
    frameCounter = frameCounter + 1
    oFrameCountDisplay.setValue(str(frameCounter))

    window.fill(BLACK)

    oBall.draw()
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
