from imaplib import Flags

import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Custom Cursor")

cursor_image = pygame.image.load('data/arrow.png')
cursor_rect = cursor_image.get_rect()

pygame.mouse.set_visible(False)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_focused():
        mouse_x, mouse_y = pygame.mouse.get_pos()
        cursor_rect.topleft = (mouse_x, mouse_y)

        screen.fill((0, 0, 0))

        screen.blit(cursor_image, cursor_rect)

    pygame.display.flip()
pygame.quit()
sys.exit()
