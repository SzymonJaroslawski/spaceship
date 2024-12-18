import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init
    print("Starting asteroids!")
    print(
        f"Screen width: {SCREEN_WIDTH}\n"
        f"Screen height: {SCREEN_HEIGHT}"
)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    dt = 0



    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return

        for obj in updatable:
            obj.update(dt) 
        
        screen.fill("#000000")
        
        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("GAME OVER CRISTOFER!")
                exit()

            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.split()
            

        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000
        


if __name__ == "__main__":
    main()