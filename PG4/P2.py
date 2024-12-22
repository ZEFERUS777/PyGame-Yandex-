import sys

import pygame

pygame.init()

img_x = 10
img_y = 10

img = pygame.image.load('data/creature.png')
img_rect = img.get_rect()
screen = pygame.display.set_mode((300, 300))

screen.blit(img, (img_x, img_y))
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                img_x -= 10
            if event.key == pygame.K_RIGHT:
                img_x += 10
            if event.key == pygame.K_UP:
                img_y -= 10
            if event.key == pygame.K_DOWN:
                img_y += 10

        screen.fill((255, 255, 255))
        screen.blit(img, (img_x, img_y))
        pygame.display.flip()

pygame.quit()
sys.exit()
