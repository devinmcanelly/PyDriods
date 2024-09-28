import pygame
import circleshape, constants

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self,screen):
        points = self.triangle()
        pygame.draw.polygon(screen,"white",points,2)
    def rotate(self,dt):
        self.rotation += (constants.PLAYER_TURN_SPEED * dt)
    def update(self,dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_i]:
            self.rotate(-dt)
        if keys[pygame.K_a]:
            self.rotate(dt)

        if keys[pygame.K_o]:
            self.move(dt)

        if keys[pygame.K_e]:
            self.move(-dt)
            
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt