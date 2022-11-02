from pygame import Vector2 as v2
import random
from globals import *


def ra():
    vec = v2(random.randint(-360, 360), random.randint(-360, 360))
    if (x := vec.magnitude()) > max_force:
        return vec * (max_force / x)
    return vec


class DNA:
    def __init__(self) -> None:
        self.genes: list[v2] = []
        for _ in range(frames):
            self.genes.append(ra())

    def mutate(self):
        new_genes = []
        for i in range(frames):
            if random.random() == 0.01:
                new_genes.append(ra())
            else:
                new_genes.append(self.genes[i])
        self.genes = new_genes
