import pygame, circleshape

class Asteroid(circleshape.CircleShape):
     def __init__(self, x, y, radius):
         super().__init__(x, y, radius)
         self.hitbox = radius 
     def draw(self, screen):
         pygame.draw.circle(surface=screen, \
         center=(self.position.x,self.position.y), color="grey",\
         radius=self.radius, width=2)

     def update(self, dt):
         self.position += dt * self.velocity
