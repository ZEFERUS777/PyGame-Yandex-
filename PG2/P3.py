import sys
import pygame

pygame.init()

SIZE = (300, 300)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("MOTION SQUARE")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

SQUARE_SIZE = 100
square_x, square_y = 0, 0

offset_x, offset_y = 0, 0
dragging = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = event.pos
                if square_x <= mouse_x <= square_x + SQUARE_SIZE and square_y <= mouse_y <= square_y + SQUARE_SIZE:
                    dragging = True
                    offset_x = mouse_x - square_x
                    offset_y = mouse_y - square_y
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
        if event.type == pygame.MOUSEMOTION:
            if dragging:
                mouse_x, mouse_y = event.pos
                square_x = mouse_x - offset_x
                square_y = mouse_y - offset_y

    square_x = max(0, min(square_x, SIZE[0] - SQUARE_SIZE))
    square_y = max(0, min(square_y, SIZE[1] - SQUARE_SIZE))

    screen.fill(BLACK)

    pygame.draw.rect(screen, GREEN, (square_x, square_y, SQUARE_SIZE, SQUARE_SIZE))

    pygame.display.flip()

pygame.quit()
sys.exit()
