import sys
import pygame

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
        if self.board[y][x] == 1:
            pygame.draw.rect(self.screen, GREEN, (cell_x, cell_y, self.cell_size, self.cell_size))

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


class Life(Board):
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        super().__init__(width, height, left, top, cell_size)
        self.running = False
        self.speed = 10

    def count_neighbors(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.board[ny][nx] == 1:
                    count += 1
        return count

    def next_move(self):
        new_board = [[0] * self.width for _ in range(self.height)]
        for x in range(self.width):
            for y in range(self.height):
                neighbors = self.count_neighbors(x, y)
                if self.board[y][x] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_board[y][x] = 0
                    else:
                        new_board[y][x] = 1
                else:
                    if neighbors == 3:
                        new_board[y][x] = 1
        self.board = new_board

    def run(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        self.handle_click(event.pos)
                    elif event.button == 3:  # Right mouse button
                        self.running = not self.running
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.running = not self.running
                if event.type == pygame.MOUSEWHEEL:
                    self.speed += event.y
                    self.speed = max(1, self.speed)

            if self.running:
                self.next_move()

            self.screen.fill(BLACK)
            self.render(self.screen)
            pygame.display.flip()
            clock.tick(self.speed)

        pygame.quit()
        sys.exit()


def main():
    l = Life(50, 30)
    l.run()


if __name__ == '__main__':
    main()
