import pygame


def draw_chessboard(a, n):
    # Инициализация Pygame
    pygame.init()

    # Установка размеров окна
    size = (a, a)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Шахматное поле")

    # Цвета
    black = (0, 0, 0)
    white = (255, 255, 255)

    # Размер одной клетки
    cell_size = a // n

    # Основной цикл программы
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Очистка экрана
        screen.fill(white)

        # Рисование шахматного поля
        for row in range(n):
            for col in range(n):
                color = black if (row + col) % 2 == 0 else white
                pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

        # Обновление экрана
        pygame.display.flip()

    # Завершение Pygame
    pygame.quit()


def main():
    try:
        # Считывание входных данных
        input_str = input("Введите размер стороны окна и количество клеток (через пробел): ")
        a, n = map(int, input_str.split())

        # Проверка, что a кратно n
        if a % n != 0:
            print("Неправильный формат ввода")
            return

        # Создание и отображение шахматного поля
        draw_chessboard(a, n)
    except ValueError:
        print("Неправильный формат ввода")


if __name__ == "__main__":
    main()
