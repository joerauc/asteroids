import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    # Returns true if two circles collide. Otherwise returns false
    def collide_check(self, circle2):
        distance = self.position.distance_to(circle2.position)

        if distance <= (self.radius + circle2.radius):
            return True
        return False
