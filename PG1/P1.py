import pygame

width, height = input().split(' ')

screen = pygame.display.set_mode((int(width), int(height)))
pygame.init()

screen.fill((0, 0, 0))
pygame.draw.line(screen, (255, 255, 255), (0, 0), (int(width), int(height)), 5)
pygame.draw.line(screen, (255, 255, 255), (0, int(height)), (int(width), 0), 5)
pygame.display.flip()

while pygame.event.wait().type != pygame.QUIT:
    pass
