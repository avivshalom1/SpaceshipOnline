import random
import pygame

class Bullet:
    screen = None
    bullet_image = None

    def __init__(self, x, y, rotate_angle):
        self.x = x
        self.y = y
        self.bullet_rect = self.bullet_image.get_rect(center=(x, y))
        self.rotate_angle = rotate_angle
        self.speed = 5
        self.is_used = False
    
    def update(self):
        movement_vector = pygame.math.Vector2(0, -self.speed).rotate(-self.rotate_angle)
        self.x += movement_vector.x
        self.y += movement_vector.y

    def draw(self):
        self.rotated_bullet_image = pygame.transform.rotate(self.bullet_image, self.rotate_angle)
        self.rotated_bullet_rect = self.rotated_bullet_image.get_rect(center = (self.x, self.y))
        self.screen.blit(self.rotated_bullet_image, self.rotated_bullet_rect)

