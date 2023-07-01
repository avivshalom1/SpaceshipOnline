import random
import pygame
import json
import math


class SpecialAlienBullet:
    screen = None
    special_alien_bullet_image = None

    def __init__(self,screen, x, y, special_alien_bullet_image):
        self.x = x
        self.y = y

        self.special_alien_bullet_image = special_alien_bullet_image
        self.screen = screen
        self.special_alien_bullet_rect = self.special_alien_bullet_image.get_rect(center=(x, y))
        self.speed = 1
    
    def update(self, spaceship_x, spaceship_y):
        movement_vector = pygame.math.Vector2(spaceship_x - self.x, spaceship_y - self.y)
        self.rotate_angle = math.degrees(movement_vector.angle_to(pygame.math.Vector2(0, -1)))

        movement_vector.scale_to_length(self.speed)
        self.x += movement_vector.x
        self.y += movement_vector.y

    def draw(self):
        self.rotated_special_alien_bullet_image = pygame.transform.rotate(self.special_alien_bullet_image, 1)
        self.rotated_special_alien_bullet_rect = self.rotated_special_alien_bullet_image.get_rect(center = (self.x, self.y))
        self.screen.blit(self.rotated_special_alien_bullet_image, self.rotated_special_alien_bullet_rect)

