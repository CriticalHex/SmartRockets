from globals import *
from rocket import Rocket


class Population:
    def __init__(self) -> None:
        self.rockets: list[Rocket] = []
        for _ in range(max_rockets):
            self.rockets.append(Rocket())

    def update(self, frame: int):
        for r in self.rockets:
            r.update(frame)
