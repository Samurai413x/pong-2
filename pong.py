#import modules
import pygame, sys, time
from pygame.locals import*

pygame.init() #set up pygame

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 450

#set up window 
windowSurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption('Pong!')

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#ball
ball = {'rect':pygame.Rect(100, 80, 10, 10), 'color':WHITE, 'xVelocity': 1, 'yVelocity': 1}

while True: #game loop 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #background
    windowSurface.fill(BLACK)

    #draw ball
    pygame.draw.rect(windowSurface, ball['color'], ball['rect'])
            
    pygame.display.update()
    time.sleep(0.02) #time reset
