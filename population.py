from globals import *
from rocket import Rocket
import random
from dna import DNA


class Population:
    def __init__(self) -> None:
        self.rockets: list[Rocket] = []
        self.repro_pool: list[Rocket] = []
        for _ in range(max_rockets):
            self.rockets.append(Rocket())

    def reproduce(self):
        self.normalize_scores()
        for r in self.rockets:
            r.dna.mutate(r.score)
            select = 0
            selector = random.random()
            while selector > 0:
                selector -= self.rockets[select].score
                select += 1
            select -= 1
            self.repro_pool.append(self.rockets[select])
        new_rockets = []
        for r in self.repro_pool:
            mid = random.randrange(0, frames)
            p1 = self.repro_pool[random.randrange(0, max_rockets)]
            p2 = self.repro_pool[random.randrange(0, max_rockets)]
            new_dna = DNA()
            new_dna.genes.clear()
            new_dna.genes.extend(p1.dna.genes[0:mid])
            new_dna.genes.extend(p2.dna.genes[mid:frames])
            new_rockets.append(Rocket(new_dna))
        self.repro_pool.clear()
        self.rockets = new_rockets

    def update(self, frame: int):
        if frame == frames - 1:
            for r in self.rockets:
                r.eval()
            self.reproduce()
        for r in self.rockets:
            r.update(frame)
            
    def draw(self):
        for r in self.rockets:
            r.draw()

    def normalize_scores(self):
        total = 0
        for r in self.rockets:
            total += r.score
        for r in self.rockets:
            r.score /= total
            #print(r.score)
