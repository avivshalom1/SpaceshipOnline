import random
import pygame

class Spaceship:

    def __init__(self, x, y, rotate_angle, screen, spaceship_image):
        self.x = x
        self.y = y
        self.spaceship_image = spaceship_image
        self.spaceship_rect = self.spaceship_image.get_rect(center=(x, y))
        self.rotated_spaceship_rect = self.spaceship_image.get_rect(center = (self.x, self.y))
        self.rotate_angle = rotate_angle
        self.speed = 5  
        self.screen = screen

    def update(self, rotate_angle):
        
         self.rotate_angle = rotate_angle
         movement_vector = pygame.math.Vector2(0, -self.speed).rotate(-self.rotate_angle)
         self.y += movement_vector.y 
         self.x += movement_vector.x

    def draw(self):
        self.rotate_spaceship_image = pygame.transform.rotate(self.spaceship_image, self.rotate_angle)
        self.rotated_spaceship_rect = self.rotate_spaceship_image.get_rect(center = (self.x, self.y))
        self.screen.blit(self.rotate_spaceship_image, self.rotated_spaceship_rect)
