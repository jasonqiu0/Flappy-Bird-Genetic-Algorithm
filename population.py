import config
import bird

class Population:
    def __init__(self):
        self.bird = bird.Bird()

    def update_birds(self):
        self.bird.draw(config.window)