import pygame
import os
from bullet import Bullet

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("assets", "player_ship.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0
        self.power_level = 1

    def update(self):
        self.speed_x = 0
        

        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.rect.centerx = mouse_x
        else:

            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT] or keystate[pygame.K_a]:
                self.speed_x = -5
            if keystate[pygame.K_RIGHT] or keystate[pygame.K_d]:
                self.speed_x = 5
            
            self.rect.x += self.speed_x
        

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullets = []

        if self.power_level == 1:
            bullets.append(Bullet(self.rect.centerx, self.rect.top))
            

        elif self.power_level == 2:
            bullets.append(Bullet(self.rect.left, self.rect.centery))
            bullets.append(Bullet(self.rect.right, self.rect.centery))
            

        elif self.power_level == 3:
            bullets.append(Bullet(self.rect.centerx, self.rect.top, speed=-15, color=(0, 255, 255)))
            

        elif self.power_level == 4:
            bullets.append(Bullet(self.rect.left, self.rect.centery, speed=-15, color=(0, 255, 255)))
            bullets.append(Bullet(self.rect.right, self.rect.centery, speed=-15, color=(0, 255, 255)))
            

        elif self.power_level == 5:
            bullets.append(Bullet(self.rect.centerx, self.rect.top, color=(0, 255, 0)))
            bullets.append(Bullet(self.rect.left, self.rect.centery, color=(0, 255, 0)))
            bullets.append(Bullet(self.rect.right, self.rect.centery, color=(0, 255, 0)))
            

        elif self.power_level == 6:
            bullets.append(Bullet(self.rect.centerx, self.rect.top, speed=-15, color=(0, 255, 0)))
            bullets.append(Bullet(self.rect.left, self.rect.centery, speed=-15, color=(0, 255, 0)))
            bullets.append(Bullet(self.rect.right, self.rect.centery, speed=-15, color=(0, 255, 0)))
            

        elif self.power_level == 7:
            bullets.append(Bullet(self.rect.left, self.rect.centery, color=(255, 0, 255)))
            bullets.append(Bullet(self.rect.right, self.rect.centery, color=(255, 0, 255)))
            bullets.append(Bullet(self.rect.left + 10, self.rect.top, color=(255, 0, 255)))
            bullets.append(Bullet(self.rect.right - 10, self.rect.top, color=(255, 0, 255)))
            

        elif self.power_level == 8:
            bullets.append(Bullet(self.rect.left, self.rect.centery, speed=-18, color=(255, 0, 255)))
            bullets.append(Bullet(self.rect.right, self.rect.centery, speed=-18, color=(255, 0, 255)))
            bullets.append(Bullet(self.rect.left + 10, self.rect.top, speed=-18, color=(255, 0, 255)))
            bullets.append(Bullet(self.rect.right - 10, self.rect.top, speed=-18, color=(255, 0, 255)))
            

        elif self.power_level == 9:
            bullets.append(Bullet(self.rect.centerx, self.rect.top, speed=-25, color=(255, 0, 0)))
            bullets.append(Bullet(self.rect.centerx - 10, self.rect.top + 10, speed=-22, color=(255, 0, 0)))
            bullets.append(Bullet(self.rect.centerx + 10, self.rect.top + 10, speed=-22, color=(255, 0, 0)))


        elif self.power_level >= 10:
            bullets.append(Bullet(self.rect.centerx, self.rect.top, speed=-25, color=(255, 215, 0)))
            bullets.append(Bullet(self.rect.left, self.rect.centery, speed=-20, color=(255, 215, 0)))
            bullets.append(Bullet(self.rect.right, self.rect.centery, speed=-20, color=(255, 215, 0)))
            bullets.append(Bullet(self.rect.left - 20, self.rect.bottom, speed=-15, color=(255, 215, 0)))
            bullets.append(Bullet(self.rect.right + 20, self.rect.bottom, speed=-15, color=(255, 215, 0)))
            
        return bullets
