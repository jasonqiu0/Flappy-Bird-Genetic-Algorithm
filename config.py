import pygame
import game

window_height = 800
window_width = 650
window = pygame.display.set_mode((window_width,window_height))

ground = game.Ground(window_width)
obstacles = []