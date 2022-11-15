import globals as g
from rocket import Rocket
import random
from dna import DNA


class Population:
    def __init__(self) -> None:
        self.generations = 0
        self.hit_at = None
        self.gen_font = g.font.render(
            f"Generations: {self.generations}", True, (0, 0, 255)
        )
        self.rockets: list[Rocket] = []
        self.repro_pool: list[Rocket] = []
        for _ in range(g.max_rockets):
            self.rockets.append(Rocket())

    def reproduce(self):
        self.normalize_scores()
        for r in self.rockets:
            r.dna.mutate(r.hit_target)
            select = 0
            selector = random.random()
            while selector > 0:
                selector -= self.rockets[select].score
                select += 1
            select -= 1
            self.repro_pool.append(self.rockets[select])
        new_rockets = []
        for r in self.repro_pool:
            mid = random.randrange(0, g.frames)
            p1 = self.repro_pool[random.randrange(0, g.max_rockets)]
            p2 = self.repro_pool[random.randrange(0, g.max_rockets)]
            new_dna = DNA()
            new_dna.genes.clear()
            new_dna.genes.extend(p1.dna.genes[0:mid])
            new_dna.genes.extend(p2.dna.genes[mid : g.frames])
            new_rockets.append(Rocket(new_dna))
        self.repro_pool.clear()
        self.rockets = new_rockets

    def update(self, frame: int):
        if frame == g.frames - 1:
            self.generations += 1
            self.gen_font = g.font.render(
                f"Generations: {self.generations}", True, (0, 0, 255)
            )
            for r in self.rockets:
                r.eval()
            self.reproduce()
        for r in self.rockets:
            r.update(frame)
            if not self.hit_at:
                if r.hit_target:
                    self.hit_at = self.generations
                    self.hit_font = g.font.render(
                        f"Hit Target at Generation: {self.hit_at}", True, (0, 0, 255)
                    )

    def draw(self):
        g.screen.blit(self.gen_font, (0, 0))
        if self.hit_at:
            g.screen.blit(self.hit_font, (0, self.gen_font.get_height()))
        for r in self.rockets:
            r.draw()

    def normalize_scores(self):
        total = 0
        for r in self.rockets:
            total += r.score
        for r in self.rockets:
            r.score /= total
            # print(r.score)
