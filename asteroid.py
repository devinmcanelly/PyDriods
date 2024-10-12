import pygame, random,circleshape

from constants import ASTEROID_MIN_RADIUS
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

     def split(self):
          self.kill()
          if self.radius <= ASTEROID_MIN_RADIUS:
               return
          else:
               rand_angle = random.uniform(20,50)
               vector0 = self.velocity.rotate(rand_angle)
               vector1 = self.velocity.rotate(-rand_angle)
               new_radius = self.radius - ASTEROID_MIN_RADIUS
               spawn0 = Asteroid(self.position.x, self.position.y, new_radius)
               spawn0.velocity = vector0 * 2.2
               spawn1 = Asteroid(self.position.x, self.position.y, new_radius)
               spawn1.velocity = vector1 * 2.2
               
               
