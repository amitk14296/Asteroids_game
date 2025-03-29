import pygame
from CircleShape import*
from constants import*

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)  # Call parent's __init__ with x, y, and shot radius
        
    def update(self, dt):
        self.position += self.velocity * dt  # Update position based on velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS)