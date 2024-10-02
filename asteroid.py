import pygame, circleshape

class Asteroid(circleshape.CircleShape):
     def __init__(self, x, y, radius):
         super().__init__(x, y, radius)

     def draw(self, x, y, radius):
         pygame.draw.circle(surface, center=(self.x,self.y), radius=self.radius, width=2)

     def update(self, dt, velocity):
         self.position += dt * velocity
