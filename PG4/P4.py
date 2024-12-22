import sys

import pygame
import random

pygame.init()

bomb_image = pygame.image.load('data/bomb.png')
boom_image = pygame.image.load('data/boom.png')

SIZE = width, height = (500, 500)
screen = pygame.display.set_mode(SIZE)

BOMB_WIDTH, BOMB_HEIGHT = bomb_image.get_size()
BOOM_WIDTH, BOOM_HEIGHT = boom_image.get_size()


class Bomb:
    def __init__(self):
        self.x = random.randint(0, width - BOMB_WIDTH)
        self.y = random.randint(0, height - BOMB_HEIGHT)
        self.exploded = False

    def render(self, screen):
        if not self.exploded:
            screen.blit(bomb_image, (self.x, self.y))
        else:
            screen.blit(boom_image, (self.x, self.y))

    def explode(self):
        self.exploded = True

    def is_clicked(self, pos):
        return self.x <= pos[0] <= self.x + BOMB_WIDTH and self.y <= pos[1] <= self.y + BOMB_HEIGHT


bombs = [Bomb() for _ in range(20)]

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for bomb in bombs:
                if bomb.is_clicked(pos):
                    bomb.explode()

    for bomb in bombs:
        bomb.render(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
