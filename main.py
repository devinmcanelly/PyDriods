import pygame, sys
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():

        pygame.init()
        clock = pygame.time.Clock()
        dt = 0 # Delta-Time
        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        updatables = pygame.sprite.Group()
        drawables = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        Asteroid.containers = (updatables, drawables, asteroids)
        Player.containers = (updatables, drawables)
        Shot.containers = (updatables, drawables, shots)
        AsteroidField.containers = (updatables)
        asteroidfield = AsteroidField()
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        
        
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit("Exiting...")
                screen.fill((0,0,0,0))

                for member in drawables:
                        member.draw(screen)
                for member in updatables:
                        member.update(dt)
                for asteroid in asteroids:
                        if player.collision_detection(asteroid) == True:
                                print("Game Over, Nerd!")
                                sys.exit("git reck'd")  
                pygame.display.flip()
                dt = clock.tick(60) / 1000



if __name__ == "__main__":
	main()




def test():
        print(f"Starting asteroid test!"
              f"Screen width: {SCREEN_WIDTH} "
              f"Screen height: {SCREEN_HEIGHT}"
        )
        
        pygame.init()
        clock = pygame.time.Clock()
        dt = 0 # Delta-Time
        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        updatables = pygame.sprite.Group()
        drawables = pygame.sprite.Group()
        player.containers = (updatables,drawables)
        print(f"clock = {clock}, dt = {dt}, player "
        f"position {player.position} rotation: {player.rotation}"
        f"{player.position.y}")
        pygame.quit()
        return 
