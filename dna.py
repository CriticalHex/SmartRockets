from pygame import Vector2 as v2
import random
from globals import *


def ra():
    return v2(
        random.randint(-100, 100) * propulsion, random.randint(-100, 100) * propulsion
    )


class DNA:
    def __init__(self) -> None:
        self.genes = []
        for _ in range(frames):
            self.genes.append(ra())

    def mutate(self):
        for g in self.genes:
            if random.random() == 0.01:
                g = self.ra()
