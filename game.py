import pygame
import random

class Ground:
    ground_level = 600

    def __init__(self, window_width):
        self.x, self.y = 0, Ground.ground_level
        self.rect = pygame.Rect(self.x, self.y, window_width, 10)

    def draw(self, window):
        pygame.draw.rect(window, (255,255,255), self.rect)

class Obstacle:
    width = 10
    gap = 130

    def __init__(self, window_width):
        self.x = window_width
        self.bottom_height = random.randint(20,300)
        self.top_height = Ground.ground_level - self.bottom_height - self.gap
        self.bottom_rect, self.top_rect = pygame.Rect(0,0,0,0), pygame.Rect(0,0,0,0)
        self.passed = False
        self.off_screen = False

    def draw(self,window):
        self.bottom_rect = pygame.Rect(self.x, Ground.ground_level - self.bottom_height, self.width, self.bottom_height)
        pygame.draw.rect(window, (255,255,255), self.bottom_rect)

        self.top_rect = pygame.Rect(self.x, 0, self.width, self.top_height)
        pygame.draw.rect(window, (255,255,255), self.top_rect)
    
    def update(self):
        self.x = self.x-1
        if self.x + Obstacle.width <= 50:
            self.passed = True
        if self.x <= -self.width:
            self.off_screen = True