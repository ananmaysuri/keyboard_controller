import pygame
import sys
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((800, 800))
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                print("up")
            elif event.key==K_a:
                print("left")
            elif event.key==K_s:
                print("down")
            elif event.key==K_d:
                print("right")
        if event.type==pygame.QUIT:
            sys.exit()
