import pygame
import sys
from constants import *
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    
    while True:
        # check for user events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update game state
        for element in updatable:
            element.update(dt)
            
        # check if any asteroids collide with player or shots
        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Game Over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.is_collision(shot):
                    shot.kill()
                    asteroid.split()
            
        
        # draw game(screen, player, etc)
        screen.fill("black")
        
        for element in drawable:
            element.draw(screen)
            
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()