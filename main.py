import pygame
from dna import DNA
from population import Population
from rocket import Rocket
from globals import *


def main():
    current_frame = 0
    population = Population()
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL]:
                running = False
            if keys[pygame.K_LSHIFT]:
                population = Population()
            if keys[pygame.K_SPACE]:
                pass

        screen.fill((0, 0, 0))

        population.update(current_frame)
        current_frame += 1
        current_frame %= frames

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
