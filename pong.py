import pygame, sys
from pygame.locals import*

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 450))
pygame.display.set_caption('Pong!')
while True: #game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
