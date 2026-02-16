import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT,PLAYER_RADIUS,LINE_WIDTH
from logger import log_state,log_event
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    pygame.init()
    display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        dt = clock.tick(60)/1000
        #print(dt)
        #player.update(dt)
        updatable.update(dt)
        collidable: Asteroid
        for collidable in asteroids:
            if collidable.collide_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        collidable: Asteroid
        for asteroid in asteroids:
            shot : Shot
            for shot in shots:
                if shot.collide_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()


        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        display.fill("black")
        #player.draw(display)
        for object in drawable:
            object.draw(display)
        pygame.display.flip()


if __name__ == "__main__":
    main()
