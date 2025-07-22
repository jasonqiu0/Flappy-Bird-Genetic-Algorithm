import pygame
from sys import exit
import config
import game
import population

pygame.init()
clock = pygame.time.Clock()
population = population.Population()

def generate_obstalce():
    config.obstacles.append(game.Obstacle(config.window_width))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    obstacle_spawn_time = 10
    while True:
        quit_game()

        config.window.fill((0,0,0))

        config.ground.draw(config.window)

        if obstacle_spawn_time <= 0:
            generate_obstalce()
            obstacle_spawn_time = 200
        obstacle_spawn_time = obstacle_spawn_time - 1

        for o in config.obstacles:
            o.draw(config.window)
            o.update()
            if o.off_screen:
                config.obstacles.remove(o)

        population.update_birds()
        
        clock.tick(60)
        pygame.display.flip()

main()