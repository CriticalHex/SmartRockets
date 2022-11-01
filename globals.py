import pygame
import math

screen = pygame.display.set_mode((1000, 1000))
height = screen.get_height()
width = screen.get_width()
center = pygame.Vector2(width / 2, height / 2)
frames = 200
max_rockets = 25
max_force = 0.01

targetpos = pygame.Vector2(center.x, 100)
targetrad = 40


def heading(v: pygame.Vector2):
    if v.x > 0:
        if v.y > 0:
            return math.atan(v.y / v.x)
        if v.y < 0:
            return -math.atan(abs(v.y / v.x))
        return 0
    if v.x < 0:
        if v.y > 0:
            return math.pi - math.atan(abs(v.y / v.x))
        if v.y < 0:
            return math.atan(abs(v.y / v.x)) - math.pi
        return math.pi
    return math.pi / 2
