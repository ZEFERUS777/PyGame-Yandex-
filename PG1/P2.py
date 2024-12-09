import pygame as pg

width, height = input().split()

try:
    pg.init()
    screen = pg.display.set_mode((int(width), int(height)))
    pg.display.set_caption("P2")
    pg.draw.rect(screen, (255, 0, 0), (1, 1, int(width) - 2, int(height) - 2))
    pg.display.flip()

    while pg.event.wait().type != pg.QUIT:
        pass
except Exception:
    print("Неправильный формат ввода")
