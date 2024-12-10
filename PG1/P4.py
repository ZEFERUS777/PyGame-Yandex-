import pygame

# Инициализация Pygame
pygame.init()


# Функция для рисования мишени
def draw_target(screen, w, n):
    # Набор цветов RGB
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    color_index = 0

    # Радиус центрального круга
    radius = w

    # Вычисляем максимальный радиус для определения размера окна
    max_radius = radius + (n - 1) * w
    center_x = max_radius
    center_y = max_radius

    # Рисуем n колец и центральный круг
    for i in range(n):
        # Вычисляем радиус текущего кольца
        current_radius = radius + i * w

        # Рисуем кольцо или центральный круг
        if i == 0:
            pygame.draw.circle(screen, colors[color_index], (center_x, center_y), current_radius)
        else:
            pygame.draw.circle(screen, colors[color_index], (center_x, center_y), current_radius, w)

        # Меняем цвет
        color_index = (color_index + 1) % len(colors)


# Основная функция программы
def main():
    try:
        # Считываем входные данные
        w, n = map(int, input("Введите толщину кольца и количество колец (через пробел): ").split())

        # Проверяем корректность ввода
        if w <= 0 or n <= 0:
            print("Неправильный формат ввода")
            return

        # Вычисляем максимальный радиус для определения размера окна
        max_radius = w + (n - 1) * w
        window_size = 2 * max_radius

        # Создаем окно
        screen = pygame.display.set_mode((window_size, window_size))
        pygame.display.set_caption("RGB Мишень")

        # Заливаем фон белым цветом
        screen.fill((255, 255, 255))

        # Рисуем мишень
        draw_target(screen, w, n)

        # Обновляем экран
        pygame.display.flip()

        # Ожидаем закрытия окна
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        # Завершаем Pygame
        pygame.quit()

    except ValueError:
        print("Неправильный формат ввода")


if __name__ == "__main__":
    main()
