import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
        # Below attribute only intended for troubleshooting. Exists in the "update(dt)" and "shoot()" methods.
        # self.troubleshoot_slowdown = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        # self.troubleshoot_slowdown += 1
        # if  self.troubleshoot_slowdown >= 120:
        #     print(self.rotation)
        #     self.troubleshoot_slowdown = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        if self.shot_cooldown_timer > 0:
            self.shot_cooldown_timer -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shot_cooldown_timer <= 0:
            bullet = Shot(self.position.x, self.position.y)
            bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN

        # self.troubleshoot_slowdown += 1
        # if  self.troubleshoot_slowdown >= 120:
        #     print(bullet.velocity)
        #     self.troubleshoot_slowdown = 0