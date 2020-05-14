import pygame
image_file = '/Users/noah/Documents/pygame/images/bucket.png'

class Bucket(pygame.sprite.Sprite):
    def __init__(self, image_file = image_file, location = (50,50)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.x, self.y = location
        # self.rect = pygame.image.get_rect()
        # self.rect.top, self.rect.left = location
        self.pixel_distance = 5
        print(self.image)

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def handle_keys(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_RIGHT]:
            self.x += self.pixel_distance
        elif key[pygame.K_LEFT]:
            self.x -= self.pixel_distance