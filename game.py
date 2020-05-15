import pygame
import os, sys

from sprites.bucket import Bucket
from sprites.raindrop import Raindrop

class Game:
    def __init__(self):
        self.width, self.height = (800, 480)
        self.framerate = 60

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Raindrops')

        self.clock = pygame.time.Clock()
        self.running = True

        self.bucket = Bucket()
        self.bucket.set_location((self.width / 2, self.height - self.bucket.rect.height))

        self.raindrops = [Raindrop()]

        self.score = 0
        self.speed_multiplier = 0
        self.loop_in_game_time = 0.0
        self.spawn_threshold = 1.0

    def display_score(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('Score: ' + str(self.score), True, (255, 255, 255))
        rect = text.get_rect()
        rect.topleft = (10, 10)
        self.screen.blit(text, rect)

    def process_score(self):
        if self.score < 0:
            self.score = 0 # Temporary until we call game over
        elif self.score % 10 == 0 and self.score / 10 > self.speed_multiplier:
            self.speed_multiplier += 1
            Raindrop.speed_base += 50
            self.spawn_threshold -= .025

if __name__ == "__main__":
    game = Game()

    while game.running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() # quit the screen
                sys.exit()
                game.running = False

        # Manage in-game time
        game.loop_in_game_time += 1/60
        if game.loop_in_game_time > game.spawn_threshold:
            game.raindrops.append(Raindrop())
            game.loop_in_game_time = 0

        # Bucket moving
        game.bucket.handle_keys() # For arrow keys
        game.bucket.check_for_move() # For mouse or touch
        for drop in game.raindrops:
            drop.fall()

        # Raindrop events
        for drop in game.raindrops:
            if drop.rect.colliderect(game.bucket.rect):
                if drop.is_bad:
                    game.score -= game.score % 10
                else:
                    game.score += 1
                game.raindrops.remove(drop)
                del drop
            elif drop.rect.bottomleft[1] > game.height:
                if not drop.is_bad:
                    game.score -= 1
                game.raindrops.remove(drop)
                del drop

        # Drawing
        game.screen.fill((0,0,0))
        game.bucket.draw(game.screen)
        for drop in game.raindrops:
            drop.draw(game.screen)

        # Manage score    
        game.display_score()
        game.process_score()

        pygame.display.update()
        game.clock.tick(game.framerate)
