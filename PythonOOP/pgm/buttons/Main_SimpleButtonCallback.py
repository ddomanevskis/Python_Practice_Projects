import pygame
from pygame.locals import *
from SimpleButton import *
import sys

GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

def myCallBackFunction():
    print('User pressed Button B, called myCallBackFunction')

class CallBackTest():
    def myMethod(self):
        print('User pressed ButtonC, called myMethod of the CallBackTest object')

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oCallBackTest = CallBackTest()

oButtonA = SimpleButton(window, (25, 30), 'pgm/buttons/images/buttonAUp.png', 'pgm/buttons/images/buttonADown.png')
oButtonB = SimpleButton(window, (150, 30), 'pgm/buttons/images/buttonBUp.png', 'pgm/buttons/images/buttonBDown.png', callBack=myCallBackFunction)
oButtonC = SimpleButton(window, (275, 30), 'pgm/buttons/images/buttonCUp.png', 'pgm/buttons/images/buttonCDown.png', callBack=oCallBackTest.myMethod)
counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oButtonA.handleEvent(event):
            print('User pressed button A, handled in the main loop')

        oButtonB.handleEvent(event)

        oButtonC.handleEvent(event)

    counter = counter + 1

    window.fill(GRAY)

    oButtonA.draw()
    oButtonB.draw()
    oButtonC.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
