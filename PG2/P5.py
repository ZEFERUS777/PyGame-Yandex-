import math
import pygame
import sys

pygame.init()

SIZE = width, height = 501, 501
CENTER = (width // 2, height // 2)
RADIUS = 20
SPEED = 2

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("P5")

BLACK = (0, 0, 0)
RED = (255, 0, 0)

circle_pos = list(CENTER)


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def move_towards(current, target, speed):
    dx = target[0] - current[0]
    dy = target[1] - current[1]
    distance_to_target = distance(current, target)

    if distance_to_target < SPEED:
        return target

    direction = (dx / distance_to_target, dy / distance_to_target)
    new_pos = (current[0] + direction[0] * SPEED, current[1] + direction[1] * SPEED)
    return new_pos


target_pos = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            target_pos = event.pos

    if target_pos:
        circle_pos = move_towards(circle_pos, target_pos, SPEED)
        if distance(circle_pos, target_pos) < SPEED:
            target_pos = None

    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, circle_pos, RADIUS)
    pygame.display.flip()

pygame.quit()
sys.exit()
