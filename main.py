import pygame
from constants import *
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
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    
    while True:
        # check for user events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update game state
        for element in updatable:
            element.update(dt)
            
        # check if any asteroids collide with player
        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Game Over!")
                return
        
        # draw game(screen, player, etc)
        screen.fill("black")
        
        for element in drawable:
            element.draw(screen)
            
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()