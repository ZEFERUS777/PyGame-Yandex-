import sys
import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Board:
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode(
            (self.width * self.cell_size + 2 * self.left, self.height * self.cell_size + 2 * self.top))
        self.action = 'cross'

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode(
            (self.width * self.cell_size + 2 * self.left, self.height * self.cell_size + 2 * self.top))

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                                   self.cell_size)
                pygame.draw.rect(screen, BLACK, rect)
                pygame.draw.rect(screen, WHITE, rect, 1)
                self.draw_symbol(x, y)

    def draw_symbol(self, x, y):
        cell_x = self.left + x * self.cell_size
        cell_y = self.top + y * self.cell_size
        if self.board[y][x] == 10:
            pygame.draw.rect(self.screen, RED, (cell_x, cell_y, self.cell_size, self.cell_size))

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x -= self.left
        y -= self.top

        if x < 0 or y < 0 or x >= self.width * self.cell_size or y >= self.height * self.cell_size:
            return None
        return (x // self.cell_size, y // self.cell_size)

    def handle_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.change_value(cell)

    def change_value(self, cell):
        x, y = cell
        self.board[y][x] = 1 - self.board[y][x]

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.screen.fill(BLACK)
            self.render(self.screen)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        sys.exit()


class Minesweeper(Board):
    def __init__(self, width: int, height: int, number_min: int, left=10, top=10, cell_size=30):
        super().__init__(width, height, left, top, cell_size)
        self.number_min = number_min
        self.running = True
        self.font = pygame.font.SysFont('Arial', 30)
        self.text_surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.font_n = pygame.font.SysFont('Arial', 13)

    def create_board(self):
        new_board = [[0] * self.width for _ in range(self.height)]
        for _ in range(self.number_min):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            new_board[y][x] = 10
        return new_board

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                                   self.cell_size)
                pygame.draw.rect(screen, BLACK, rect)
                pygame.draw.rect(screen, WHITE, rect, 1)
                self.draw_symbol(x, y)
        screen.blit(self.text_surface, (0, 0))  # Накладываем поверхность с текстом

    def handle_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.change_value(cell)

    def change_value(self, cell):
        x, y = cell
        if self.board[y][x] == 10:
            self.running = False
            text = self.font.render("Game Over", True, GREEN)
            text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(3000)  # Ждем 3 секунды перед закрытием окна
        else:
            self.board[y][x] = 1 - self.board[y][x]
            bombs_nearby = self.get_bombs_nearby(x, y)
            text = self.font_n.render(str(bombs_nearby), True, GREEN)
            cell_x = self.left + x * self.cell_size
            cell_y = self.top + y * self.cell_size
            self.text_surface.blit(text, (cell_x, cell_y))  # Отрисовываем текст на поверхности
            pygame.display.flip()

    def get_bombs_nearby(self, x, y):
        bombs_nearby = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                    if self.board[y + dy][x + dx] == 10:
                        bombs_nearby += 1
        return bombs_nearby

    def run(self):
        self.board = self.create_board()
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.screen.fill(BLACK)
            self.render(self.screen)
            if not self.running:
                running = False
            pygame.display.flip()


if __name__ == "__main__":
    pygame.init()
    game = Minesweeper(10, 10, 10)
    game.run()
    pygame.quit()
