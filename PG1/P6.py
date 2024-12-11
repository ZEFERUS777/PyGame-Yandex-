import pygame
import sys


def draw_wireframe_sphere(screen, center, radius, n):
    # Рисуем горизонтальные эллипсы
    for i in range(n):
        angle = (i / (n - 1)) * 3.14159
        a = radius * abs(1 - (angle / 3.14159))
        b = radius
        pygame.draw.ellipse(screen, (255, 255, 255), (center[0] - a, center[1] - b, 2 * a, 2 * b), 1)

    # Рисуем вертикальные эллипсы
    for i in range(n):
        angle = (i / (n - 1)) * 3.14159
        a = radius
        b = radius * abs(1 - (angle / 3.14159))
        pygame.draw.ellipse(screen, (255, 255, 255), (center[0] - a, center[1] - b, 2 * a, 2 * b), 1)


def main():
    try:
        n = int(input())
    except ValueError:
        print("Неправильный формат ввода")
        return

    # Инициализация Pygame
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Проволочная сфера")

    # Центр и радиус сферы
    center = (150, 150)
    radius = 100

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        draw_wireframe_sphere(screen, center, radius, n)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
