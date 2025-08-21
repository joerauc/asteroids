import pygame
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from score import Score

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize game
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Load background image
    background_path = "imgs/galaxy_background.jpg"
    loaded_background = True
    try:
        image = pygame.image.load(background_path).convert()
    except pygame.error as e:
        print(f"Error loading image: {e}")
        loaded_background = False

    # Create groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign containers
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updateable, drawable)

    Player.containers = (updateable, drawable)
    player_one = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Score.containers = (updateable, drawable)
    score = Score()

    playing = True
    while(playing):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.collide_check(player_one) == True:
                print("Game over!")
                exit()
            for bullet in shots:
                if asteroid.collide_check(bullet) == True:
                    bullet.kill()
                    score.earn_points_from_asteroid(asteroid)
                    asteroid.split()
        
        screen.fill((0,0,0))
        screen.blit(image, (0,0))
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
