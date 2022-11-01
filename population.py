from globals import *
from rocket import Rocket


class Population:
    def __init__(self) -> None:
        self.rockets: list[Rocket] = []
        self.repro_pool: list[Rocket] = []
        for _ in range(max_rockets):
            self.rockets.append(Rocket())

    def reproduce(self):
        pass

    def update(self, frame: int):
        if frame == frames - 1:
            self.reproduce()
        for r in self.rockets:
            r.update(frame)
