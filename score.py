import pygame
from constants import *

class Score(pygame.sprite.Sprite):
    def __init__(self):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.score = 0
        self.font = pygame.font.SysFont("Arial", 30)
        self.surface = self.font.render("Score: 0", True, (255, 255, 255))
        self.display_x = SCORE_OFFSET
        self.display_y = BUFFER
    
    def earn_points_from_asteroid(self, asteroid):
        asteroid_type = asteroid.radius / ASTEROID_MIN_RADIUS # Currently 1, 2, or 3
        self.score += int(asteroid_type * SCORE_MODIFIER)
    
    def update(self, dt):
        self.surface = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.display_x = SCORE_OFFSET - len(str(self.score)) * CHAR_LEN

    def draw(self, screen):
        screen.blit(self.surface, (self.display_x, self.display_y))