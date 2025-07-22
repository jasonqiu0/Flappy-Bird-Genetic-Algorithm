import config
import bird

class Population:
    def __init__(self, size):
        self.birds = []

        self.size = size
        for i in range(0,size):
            self.birds.append(bird.Bird())

    def update_birds(self):
        for b in self.birds:
            if b.alive:
                b.think()
                b.draw(config.window)
                b.update(config.ground)
    
    def extinct(self): 
        extinct = True
        for b in self.birds:
            if b.alive:
                extinct = False
        return extinct 