import pygame
from constants import *
from player import Player

def main():
        print(f"""Starting asteroids!
Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}""")
        
        pygame.init()
        clock = pygame.time.Clock()
        dt = 0 # Delta-Time
        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        updatables = pygame.sprite.Group()
        drawables = pygame.sprite.Group()
        player.containers = (updatables, drawables)
        print(player.containers)
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return 
                screen.fill((0,0,0,0))
                player.draw(screen)
                player.update(dt)
                pygame.display.flip()
                dt = clock.tick(60) / 1000
if __name__ == "__main__":
	main()
