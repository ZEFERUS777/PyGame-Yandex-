import pygame
import sys
import math

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Balls")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

radius = 10
speed = 100  # пикселей в секунду
angle_deg = 45
angle_rad = math.radians(angle_deg)
velocity_x = speed * math.cos(angle_rad) / 60  # 60 FPS
velocity_y = -speed * math.sin(angle_rad) / 60  # 60 FPS

balls = []


def create_ball(x, y):
    return {
        'x': x,
        'y': y,
        'vx': velocity_x,
        'vy': velocity_y
    }


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            balls.append(create_ball(x, y))

    for ball in balls:
        ball['x'] += ball['vx']
        ball['y'] += ball['vy']

        if ball['x'] - radius <= 0 or ball['x'] + radius >= width:
            ball['vx'] = -ball['vx']
        if ball['y'] - radius <= 0 or ball['y'] + radius >= height:
            ball['vy'] = -ball['vy']

    screen.fill(BLACK)
    for ball in balls:
        pygame.draw.circle(screen, WHITE, (int(ball['x']), int(ball['y'])), radius)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
sys.exit()
