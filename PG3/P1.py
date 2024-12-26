import sys
import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


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
        if self.board[y][x] == 'cross':
            pygame.draw.line(self.screen, BLUE, (cell_x + 2, cell_y + 2),
                             (cell_x + self.cell_size - 2, cell_y + self.cell_size - 2), 2)
            pygame.draw.line(self.screen, BLUE, (cell_x + self.cell_size - 2, cell_y + 2),
                             (cell_x + 2, cell_y + self.cell_size - 2), 2)
        elif self.board[y][x] == 'no':
            pygame.draw.circle(self.screen, RED, (cell_x + self.cell_size // 2, cell_y + self.cell_size // 2),
                               self.cell_size // 2 - 2, 2)

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
        if self.board[y][x] != 'cross' or self.board[y][x] != 'no':
            if self.board[y][x] == 0:
                self.board[y][x] = self.action
                self.action = 'no' if self.action == 'cross' else 'cross'

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


def main():
    b = Board(10, 7)
    b.run()


if __name__ == '__main__':
    main()
