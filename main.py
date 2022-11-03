import pygame
from population import Population
import globals as g


def main():
    mouse = g.targetpos
    current_frame = 0
    population = Population()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mouse = pygame.Vector2(*pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONDOWN:
                g.targetpos = mouse
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LCTRL]:
                running = False
            if keys[pygame.K_LSHIFT]:
                population = Population()
            if keys[pygame.K_SPACE]:
                pass
            
            
        population.update(current_frame)
        if current_frame % 100 == 0:
            g.screen.fill((0, 0, 0))
            pygame.draw.circle(g.screen, (0, 255, 0), g.targetpos, g.targetrad)
            population.draw()
            pygame.display.flip()
            
        
        current_frame += 1
        current_frame %= g.frames
    pygame.quit()


if __name__ == "__main__":
    main()
