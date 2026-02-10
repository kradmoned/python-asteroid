import pygame
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT,PLAYER_RADIUS,LINE_WIDTH
from logger import log_state
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    pygame.init()
    display = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        dt = clock.tick(60)/1000
        #print(dt)
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            display.fill("black")
            player.draw(display)
            pygame.display.flip()


if __name__ == "__main__":
    main()
