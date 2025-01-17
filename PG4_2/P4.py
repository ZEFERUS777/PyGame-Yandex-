import sys
import pygame
import random
from collections import deque

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
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
        if self.board[y][x] == 1:  # Blue ball
            pygame.draw.circle(self.screen, BLUE, (cell_x + self.cell_size // 2, cell_y + self.cell_size // 2),
                               self.cell_size // 2 - 3)
        elif self.board[y][x] == 2:  # Red ball
            pygame.draw.circle(self.screen, RED, (cell_x + self.cell_size // 2, cell_y + self.cell_size // 2),
                               self.cell_size // 2 - 3)

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
        if self.board[y][x] == 0:  #
            if self.red_ball is None:
                self.board[y][x] = 1
            else:
                if self.has_path(*self.red_ball, x, y):
                    self.board[y][x] = 1
                    self.board[self.red_ball[1]][self.red_ball[0]] = 0
                    self.red_ball = None
        elif self.board[y][x] == 1:
            self.board[y][x] = 2
            self.red_ball = (x, y)
        elif self.board[y][x] == 2:
            self.board[y][x] = 1
            self.red_ball = None

    def has_path(self, x1, y1, x2, y2):
        if (x1, y1) == (x2, y2):
            return True

        queue = deque([(x1, y1)])
        visited = set([(x1, y1)])

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and (nx, ny) not in visited and self.board[ny][
                    nx] == 0:
                    if (nx, ny) == (x2, y2):
                        return True
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return False

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


class Lines(Board):
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        super().__init__(width, height, left, top, cell_size)
        self.red_ball = None

    def handle_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.change_value(cell)

    def change_value(self, cell):
        x, y = cell
        if self.board[y][x] == 0:
            if self.red_ball is None:
                self.board[y][x] = 1
            else:
                if self.has_path(*self.red_ball, x, y):
                    self.board[y][x] = 1
                    self.board[self.red_ball[1]][self.red_ball[0]] = 0
                    self.red_ball = None
        elif self.board[y][x] == 1:
            self.board[y][x] = 2
            self.red_ball = (x, y)
        elif self.board[y][x] == 2:
            self.board[y][x] = 1
            self.red_ball = None

    def has_path(self, x1, y1, x2, y2):
        if (x1, y1) == (x2, y2):
            return True

        queue = deque([(x1, y1)])
        visited = set([(x1, y1)])

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and (nx, ny) not in visited and self.board[ny][
                    nx] == 0:
                    if (nx, ny) == (x2, y2):
                        return True
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return False


if __name__ == "__main__":
    lines_game = Lines(10, 10)
    lines_game.run()
