from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "#FFFFFF", self.position, self.radius, 2)

    def update(self, dt):
         self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20.0, 50.0)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid1.velocity = a * 1.2

        asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
        asteroid2.velocity = b * 1.2

        
        