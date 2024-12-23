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

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode(
            (self.width * self.cell_size + 2 * self.left, self.height * self.cell_size + 2 * self.top))

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                color = self.get_color(self.board[y][x])
                rect = pygame.Rect(self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                                   self.cell_size)
                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, WHITE, rect, 1)

    def get_color(self, value):
        if value == 0:
            return BLACK
        elif value == 1:
            return RED
        elif value == 2:
            return BLUE

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
            self.toggle_colors(cell)

    def toggle_colors(self, cell):
        x, y = cell
        current_color = self.board[y][x]
        next_color = (current_color + 1) % 3
        self.board[y][x] = next_color

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
    b = Board(5, 7)
    b.set_view(100, 50, 50)
    b.run()


if __name__ == '__main__':
    main()
