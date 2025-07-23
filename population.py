import operator
import math

import config
import bird
import species

class Population:
    def __init__(self, size):
        self.birds = []
        self.generation = 1
        self.species = []
        self.size = size
        for _ in range(size):
            self.birds.append(bird.Bird())

    def update_birds(self):
        for b in self.birds:
            if b.alive:
                b.look()
                b.think()
                b.draw(config.window)
                b.update(config.ground)
    
    def natural_selection(self):
        print("SPECIATE")
        self.speciate()

        print("CALCULATE FITNESS")
        self.calculate_fitness()

        print("SORT BY FITNESS")
        self.sort_species_by_fitness()

        print("CREATE CHILDREN FOR NEXT GEN.")
        self.next_gen()
    
    def speciate(self):
        for s in self.species:
            s.birds = []
        
        for b in self.birds:
            add_to_species = False
            for s in self.species:
                if s.similarity(b.brain):
                    s.add_to_species(b)
                    add_to_species = True
                    break
            if not add_to_species:
                self.species.append(species.Species(b))
    
    def calculate_fitness(self):
        for b in self.birds:
            b.calculate_fitness()
        for s in self.species:
            s.calculate_average_fitness()
    
    def sort_species_by_fitness(self):
        for s in self.species:
            s.sort_birds_by_fitness()
        
        self.species.sort(key=operator.attrgetter('benchmark_fitness'),reverse=True)
    
    def next_gen(self):
        children = []

        for s in self.species:
            children.append(s.champion.clone())
        
        children_per_species = math.floor((self.size - len(self.species) / len(self.species)))
        for s in self.species:
            for i in range(0, children_per_species):
                children.append(s.offspring())
        
        while len(children) < self.size:
            children.append(self.species[0].offspring())
        
        self.birds = []
        for child in children:
            self.birds.append(child)
        self.generation += 1
    
    def extinct(self): 
        extinct = True
        for b in self.birds:
            if b.alive:
                extinct = False
        return extinct 