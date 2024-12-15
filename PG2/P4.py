import sys

import pygame

pygame.init()

SIZE = width, height = 200, 200

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("I'm watching you")

font = pygame.font.SysFont(None, 100)

BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen.fill(BLACK)

count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.WINDOWMINIMIZED:
            count += 1
        if event.type == pygame.WINDOWRESTORED:
            pass

    screen.fill(BLACK)

    text = font.render(f"{count}", True, RED)
    text_rect = text.get_rect(center=(width // 2, height // 2))

    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
