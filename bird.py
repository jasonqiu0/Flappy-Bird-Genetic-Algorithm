import random
import pygame
import config
import brain

class Bird:
    def __init__(self):
        self.x, self.y = 50, 400
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        self.color = random.randint(100,255), random.randint(100,255), random.randint(100,255)
        self.vel = 0
        self.flap = False
        self.alive = True

        self.lifespan = 0
        self.fitness = 0

        self.decision = None 
        self.vision = [0.5,1,0.5]
        self.inputs = 3
        self.brain = brain.Brain(self.inputs)
        self.brain.generate_net()

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def ground_collision(self, ground):
        return pygame.Rect.colliderect(self.rect, ground)
    
    def sky_collision(self):
        return bool(self.rect.y < 30)
    
    def obstacle_collision(self):
        for o in config.obstacles:
            return pygame.Rect.colliderect(self.rect, o.top_rect) or pygame.Rect.colliderect(self.rect, o.bottom_rect)
    
    def update(self, ground):
        if not (self.ground_collision(ground) or self.obstacle_collision()):
            self.vel = self.vel + 0.25
            self.rect.y = self.rect.y + self.vel 
            if self.vel > 5:
                self.vel = 5
            
            self.lifespan += 1 # increment lifespan everytime the function is called

        else:
            self.alive = False
            self.flap = False
            self.vel = 0
    
    def bird_flap(self):
        if not self.flap and not self.sky_collision():
            self.flap = True 
            self.vel = -5
        if self.vel >= 3:
            self.flap = False
    
    @staticmethod
    def closest_obstacle():
        for o in config.obstacles:
            if not o.passed:
                return o
    
    def look(self): # vision
        if config.obstacles:
            # i0 distance
            self.vision[0] = max(0,self.rect.center[1] - self.closest_obstacle().top_rect.bottom) / 600
            pygame.draw.line(config.window, self.color, self.rect.center, 
                             (self.rect.center[0], config.obstacles[0].top_rect.bottom))

            # i1 distance
            self.vision[1] = max(0,self.closest_obstacle().x - self.rect.center[0]) / 600
            pygame.draw.line(config.window, self.color, self.rect.center, 
                             (config.obstacles[0].x, self.rect.center[1]))

            # i2 distance
            self.vision[2] = max(0, self.closest_obstacle().bottom_rect.top - self.rect.center[1]) / 600
            pygame.draw.line(config.window, self.color, self.rect.center, 
                             (self.rect.center[0], config.obstacles[0].bottom_rect.top))

    def think(self):
        self.decision = self.brain.feed_forward(self.vision)
        if self.decision > 0.73:
            self.bird_flap()
    
    def calculate_fitness(self):
        self.fitness = self.lifespan

    def clone(self):
        clone = Bird()
        clone.fitness = self.fitness
        clone.brain = self.brain.clone()
        clone.brain.generate_net()
        return clone
    
