import pygame
image_file = 'images/bucket.png'
pixel_distance = 5

class Bucket(pygame.sprite.Sprite):
    def __init__(self, image_file:str = image_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.can_move = False

    def draw(self, surface:pygame.Surface):
        surface.blit(self.image, (self.x, self.y))

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.move(1)
        elif key[pygame.K_LEFT]:
            self.move(0)

    def move(self, direction, distance = pixel_distance):
        if direction == 1:
            self.x = self.x + distance if self.x + distance < 800 else 800
        else:
            self.x = self.x - distance if self.x - distance > 0 else 0
        self.keep_in_bounds()
        self.rect.topleft = (self.x, self.y)

    def keep_in_bounds(self):
        if self.x < 0:
            self.x = 0
        elif self.x > 800 - self.rect.width:
            self.x = 800 - self.rect.width

    def check_for_move(self):
        mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(mouse):
            self.can_move = True

        if self.can_move and pygame.mouse.get_pressed()[0]:
            if self.mouse_distance == None:
                self.mouse_distance = mouse[0] - self.x
            if self.lastX == None:
                self.lastX = mouse[0]
            else:
                self.x = mouse[0] - self.mouse_distance
        else:
            self.mouse_distance = None
            self.lastX = None
            self.can_move = False
        
        self.keep_in_bounds()
        self.rect.topleft = (self.x, self.y)
    
    def set_location(self, location):
        self.x, self.y = location
        self.rect.topleft = (self.x, self.y)
        self.lastX = self.x