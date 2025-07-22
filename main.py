import pygame
from sys import exit
import config
import game
import population


pygame.init()
clock = pygame.time.Clock()
population = population.Population(50)
font = pygame.font.Font(None, 30)

start_time = pygame.time.get_ticks()
obstacles_passed = 0

def generate_obstalce():
    config.obstacles.append(game.Obstacle(config.window_width))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    global obstacles_passed
    obstacle_spawn_time = 10
    while True:
        quit_game()

        config.window.fill((0,0,0))

        config.ground.draw(config.window)

        if obstacle_spawn_time <= 0:
            generate_obstalce()
            obstacle_spawn_time = 200
        obstacle_spawn_time = obstacle_spawn_time - 1

        elapsed_seconds = (pygame.time.get_ticks() - start_time) // 1000

        for o in config.obstacles:
            o.draw(config.window)
            o.update()

            if o.passed and not hasattr(o, 'counted'):
                obstacles_passed += 1
                o.counted = True
            
            if o.off_screen:
                config.obstacles.remove(o)

        if not population.extinct():
            population.update_birds()
        else:
            pass
        
        alive_count = sum(1 for b in population.birds if b.alive)
        text_surface = font.render(f"Remaining Birds: {alive_count}", True, (255, 255, 255))
        
        time_text = font.render(f"Time: {elapsed_seconds}s", True, (255, 255, 255))
        obstacles_text = font.render(f"Obstacles Passed: {obstacles_passed}", True, (255, 255, 255))
        
        
        config.window.blit(text_surface, (10, config.window_height - 90))
        config.window.blit(time_text, (10, config.window_height - 60))
        config.window.blit(obstacles_text, (10, config.window_height - 30))

        clock.tick(60)
        pygame.display.flip()

main()