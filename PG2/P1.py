import sys

import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Растущий жёлтый круг")

blue = (0, 0, 255)
yellow = (255, 255, 0)

circle_center = None
circle_radius = 0
growing = False
growth_speed = 10  # Пикселей в секунду

clock = pygame.time.Clock()
fps = 60


def reset_circle():
    global circle_center, circle_radius, growing
    circle_center = None
    circle_radius = 0
    growing = False


def draw_circle():
    if circle_center:
        pygame.draw.circle(screen, yellow, circle_center, circle_radius)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            reset_circle()
            circle_center = event.pos
            growing = True

    if growing:
        circle_radius += growth_speed / fps

    screen.fill(blue)

    draw_circle()

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()
