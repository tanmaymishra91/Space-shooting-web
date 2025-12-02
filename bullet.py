import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed=-10, color=(255, 255, 0)):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = speed

    def update(self):
        self.rect.y += self.speed_y

        if self.rect.bottom < 0:
            self.kill()
