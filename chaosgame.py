"""
This is a Program to make a small visualisation of the Chaos Game
Written by Jonas
Things to do:
    draggable nodes
    changeable distance of where the next point is drawn
    add restart button
    add different polygons
    user interface with start stop and change buttons
USAGE:
1. Input your value for r into factor
2. Run
3. Click on Window where your nodes should be (you can have as many as you want)
4. Hit any key and let the magic begin
"""

import pygame
import random
from pygame.locals import *
pygame.init()

# screen initialisation to have the screen as global variable
size = 720, 480
screen = pygame.display.set_mode(size)

# colors
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# this is how nodes will look: nodes = {"node1": (360, 20), "node2": (580, 46), "node3": (140, 460), "node4": (570, 60)}
nodes = {}
# counter to check how many nodes there are
mousecount = 0
# random starting point
randPoint = random.randint(150, 439), random.randint(20, 459)


factor = 0.5


def calcmiddle(point1, point2):
    x = ((1 - factor) * point1[0] + factor * point2[0])
    y = ((1 - factor) * point1[1] + factor * point2[1])
    return int(x), int(y)


def drawnode():
    # print("MOUSE")
    mousepos = pygame.mouse.get_pos()
    print(mousepos)
    pygame.draw.circle(screen, red, mousepos, 7)
    nodes["node" + str(random.randint(0, 100))] = mousepos
    # mousecount += 1
    print(nodes)
    # print(mousecount)


def chaos():
    # main game function where points get iterated and drawn

    oldpoint = randPoint

    # print(randPoint)
    pygame.draw.circle(screen, black, randPoint, 1)
    for i in range(10000):
        newpoint = calcmiddle(oldpoint, random.choice(list(nodes.items()))[1])
        # print(newpoint)
        pygame.draw.circle(screen, black, newpoint, 1)
        oldpoint = newpoint


def main():
    # main function that initializes the chaos game

    pygame.display.set_caption("Chaos - Game")

    screen.fill(white)
    """
    for i in nodes:
        pygame.draw.circle(screen, red, nodes[i], 7)
    """


if __name__ == '__main__':
    main()


while True:
    # function for Pygame updating the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == MOUSEBUTTONUP:
            print("MOUSE")
            drawnode()

        if event.type == KEYUP:
            print("SPACE")
            chaos()

    pygame.display.update()
