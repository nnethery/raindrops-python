import pygame
import os, sys

from sprites.bucket import Bucket
from sprites.raindrop import Raindrop

width, height = (800, 480)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Raindrops')

clock = pygame.time.Clock()
running = True

bucket = Bucket()
bucket.set_location((width / 2,height - bucket.rect.height))

raindrops = [Raindrop()]

score = 0
speed_multiplier = 0
loop_in_game_time = 0.0
spawn_threshold = 1.0

def display_score():
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Score: ' + str(score), True, (255, 255, 255))
    rect = text.get_rect()
    rect.topleft = (10, 10)
    screen.blit(text, rect)

def process_score():
    global speed_multiplier
    if score < 0:
        score = 0 # Temporary until we call game over
    elif score % 10 == 0 and score / 10 > speed_multiplier:
        speed_multiplier += 1
        Raindrop.speed_base += 50
        spawn_threshold -= .025

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            sys.exit()
            running = False

    # Manage in-game time
    loop_in_game_time += 1/60
    if loop_in_game_time > spawn_threshold:
        raindrops.append(Raindrop())
        loop_in_game_time = 0

    # Bucket moving
    bucket.handle_keys()
    bucket.check_for_move()
    for drop in raindrops:
        drop.fall()

    # Raindrop events
    for drop in raindrops:
        if drop.rect.colliderect(bucket.rect):
            if drop.is_bad:
                score -= score % 10
            else:
                score += 1
            raindrops.remove(drop)
            del drop
        elif drop.rect.bottomleft[1] > height:
            if not drop.is_bad:
                score -= 1
            raindrops.remove(drop)
            del drop

    # Drawing
    screen.fill((0,0,0))
    bucket.draw(screen)
    for drop in raindrops:
        drop.draw(screen)

    # Manage score    
    display_score()
    process_score()

    pygame.display.flip()
    clock.tick(60)