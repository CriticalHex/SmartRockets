from pygame import Vector2 as v2
import random
import globals as g


def ra():
    vec = v2(random.randint(-360, 360), random.randint(-360, 360))
    if (x := vec.magnitude()) > g.max_force:
        return vec * (g.max_force / x)
    return vec


class DNA:
    def __init__(self) -> None:
        self.genes: list[v2] = []
        for _ in range(g.frames):
            self.genes.append(ra())

    def mutate(self, score: float):
        chance = score # ((1 / score) / 5) / 100
        print(score, chance)
        new_genes = []
        for i in range(g.frames):
            if random.random() <= chance:
                new_genes.append(ra())
            else:
                new_genes.append(self.genes[i])
        self.genes = new_genes
