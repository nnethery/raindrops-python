import pygame
import random
image_files = ['images/droplet.png', 'images/bad droplet.png']

class Raindrop(pygame.sprite.Sprite):
    speed_base = 200

    def __init__(self, speed:int = 0, image_files:list = image_files, location:tuple = (50,50)):
        pygame.sprite.Sprite.__init__(self)
        self.is_bad = True if random.randrange(0,6) == 0 else False
        self.image = pygame.image.load(image_files[1]) if self.is_bad else pygame.image.load(image_files[0])
        self.rect = self.image.get_rect()
        self.y = 0 - self.rect.height
        self.x = random.randint(0, 800 - self.rect.width)
        self.rect.topleft = (self.x, self.y)
        self.speed = random.randint(Raindrop.speed_base, Raindrop.speed_base + 100)

    def fall(self):
        self.y += (self.speed) * (1/60)
        self.rect.topleft = (self.x, self.y)

    def draw(self, surface:pygame.Surface):
        surface.blit(self.image, (self.x, self.y))