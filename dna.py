from pygame import Vector2 as v2
import random
from globals import *

speed = 360

def ra():
    vec = v2(random.randint(-speed, speed), random.randint(-speed,speed))
    if (x := vec.magnitude()) > max_force:
        return vec * (max_force / x)
    return vec


class DNA:
    def __init__(self) -> None:
        self.genes: list[v2] = []
        for _ in range(frames):
            self.genes.append(ra())

    def mutate(self):
        for g in self.genes:
            if random.random() == 0.01:
                g = self.ra()
