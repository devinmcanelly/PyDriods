import pygame
import circleshape, constants

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.hitbox = (self.radius * 0.33) # Close. Either a little bigger or add multiple hitboxes
        self.timer = 0
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
        self.timer -= 0.05
        if keys[pygame.K_i]:
            self.rotate(-dt)
        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_o]:
            self.move(dt)
        if keys[pygame.K_e]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            rotation = self.rotation
            self.shoot(rotation, dt)
            
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def shoot(self, rotation, dt):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(rotation) * constants.PLAYER_SHOOT_SPEED
            self.timer = constants.PLAYER_SHOOT_COOLDOWN

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=constants.SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, \
        center=(self.position.x,self.position.y), color="yellow",\
        radius=self.radius)

    def update(self, dt):
        self.position += dt * self.velocity

