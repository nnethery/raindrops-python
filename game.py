import pygame
import os, sys

from sprites.bucket import *
from sprites.raindrop import *

pygame.init()
screen = pygame.display.set_mode((800, 480))
pygame.display.set_caption('Raindrops')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

screen.blit(background, (0, 0))
pygame.display.flip()

clock = pygame.time.Clock()
running = True

bucket = Bucket()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            sys.exit()
            running = False

    bucket.handle_keys()

    # screen.fill((255,255,255))
    bucket.draw(screen)

    pygame.display.flip()
    clock.tick(60)