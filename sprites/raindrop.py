import pygame

class Raindrop(pygame.sprite.Sprite):
    def __init__(self, image_file, left, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = pygame.image.get_rect()
        self.rect.top = 50
        self.rect.left = left
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)