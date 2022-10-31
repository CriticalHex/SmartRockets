import pygame
from pygame import Vector2 as v2
from globals import *
from dna import DNA, ra

counter = 0


class Rocket:
    def __init__(self) -> None:
        self.pos = v2(center.x, height)
        self.vel = v2(0, 0)
        self.acc = ra()
        self.dna = DNA()
        self.crashed = False
        self.rect = pygame.Rect(0, 0, 10, 50)
        self.rect.center = self.pos
        self.image = pygame.Surface((10, 50))
        self.image.fill((pygame.Color(255, 0, 0)))
        pygame.draw.rect(self.image, (255, 255, 255), self.rect)

    def update(self, frame: int):
        self.acc += self.dna.genes[frame]
        self.accelerate()
        self.draw()

    def accelerate(self):
        self.vel += self.acc
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel = self.vel.normalize()
        self.pos += self.vel
        self.rect.center = self.pos

    def draw(self):
        pygame.transform.rotate(self.image, 10)
        screen.blit(self.image, self.rect)
