import pygame
from constants import *
from player import Player

def main():
        print(f"Starting asteroids!"
              f"Screen width: {SCREEN_WIDTH} "
              f"Screen height: {SCREEN_HEIGHT}"
              )
        
        pygame.init()
        clock = pygame.time.Clock()
        dt = 0 # Delta-Time
        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        
        updatables = pygame.sprite.Group()
        drawables = pygame.sprite.Group()
        Player.containers = (updatables, drawables)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return 
                screen.fill((0,0,0,0))

                for member in drawables:
                        member.draw(screen)
                for member in updatables:
                        member.update(dt)

                pygame.display.flip()
                dt = clock.tick(60) / 1000



if __name__ == "__main__":
	main()




def test():
        print(f"Starting asteroid test!"
              f"Screen width: {SCREEN_WIDTH} "
              f"Screen height: {SCREEN_HEIGHT}"
              ) # This looks less bad I guess
        
        pygame.init()
        clock = pygame.time.Clock()
        dt = 0 # Delta-Time
        # screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        updatables = pygame.sprite.Group()
        drawables = pygame.sprite.Group()
        player.containers = (updatables,drawables)
        print(f'clock = {clock}, dt = {dt}, player containers {player.containers[0]}')
        return player
