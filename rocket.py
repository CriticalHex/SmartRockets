from math import dist
import pygame
from pygame import Vector2 as v2
from globals import *
from dna import DNA


class Rocket:
    def __init__(self, dna: DNA = None) -> None:
        self.flying = True
        self.hit_target = False
        self.pos = v2(center.x, height - 100)
        self.vel = v2(0, 0)
        self.acc = v2(0, 0)
        if not dna:
            self.dna = DNA()
        else:
            self.dna = dna
        self.image = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.image.fill((pygame.Color(0, 0, 0, 0)))
        self.irect = pygame.Rect(0, 0, 50, 10)
        self.irect.center = self.image.get_rect().center
        pygame.draw.rect(self.image, (255, 255, 255), self.irect)
        self.rect = self.image.get_rect(center=(self.pos))

    def update(self, frame: int):
        if self.flying and not self.hit_target:
            self.collision()
            self.acc = self.dna.genes[frame]
            self.accelerate()
        self.draw()

    def accelerate(self):
        self.vel += self.acc
        if self.vel.magnitude() > 0:
            self.vel = self.vel.normalize()
        self.pos += self.vel
        self.rect.center = self.pos

    def draw(self):
        image = pygame.transform.rotate(self.image, -math.degrees(heading(self.vel)))
        screen.blit(image, self.rect)

    def stop(self):
        self.flying = False
        self.image.set_alpha(100)

    def collision(self):
        if dist(self.pos, targetpos) <= targetrad:
            self.hit_target = True
            self.stop()
        if (
            self.pos.y <= 0
            or self.pos.y >= height
            or self.pos.x <= 0
            or self.pos.x >= width
        ):
            self.stop()
