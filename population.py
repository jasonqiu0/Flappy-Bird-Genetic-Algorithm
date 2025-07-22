import config
import bird

class Population:
    def __init__(self):
        self.bird = bird.Bird()

    def update_birds(self):
        if self.bird.alive:
            self.bird.think()
            self.bird.draw(config.window)
            self.bird.update(config.ground)
