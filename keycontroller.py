import pygame
import sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((200, 200),0)
pygame.key.set_repeat(100,100)

RED = (255,0,0)
BLUE = (0,0,255)

font = pygame.font.SysFont ("Arial", 72)
text = font.render ("Hello!", True, RED)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                print("up")
                screen.fill(RED)
                pygame.display.update()
            elif event.key==K_a:
                print("left")
            elif event.key==K_s:
                print("down")
            elif event.key==K_d:
                print("right")
        if event.type == pygame.KEYUP:
            if event.key==K_w:
                print("up")
                screen.fill(BLUE)
                pygame.display.update()
        if event.type==pygame.QUIT:
            sys.exit()
