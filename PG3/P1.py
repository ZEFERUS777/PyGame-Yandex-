import sys

import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Board:
    def __init__(self, width, height, left=10, top=10, cell_size=30):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.screen = pygame.display.set_mode((500, 500))

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for x in range(self.width):
            for y in range(self.height):
                rect = pygame.Rect(self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size,
                                   self.cell_size)
                pygame.draw.rect(screen, WHITE, rect, 1)

    def get_cell(self, nouse_pos):
        x, y = nouse_pos
        x -= self.left
        y -= self.top

        if x < 0 or y < 0 or x >= self.width * self.cell_size or y >= self.height * self.cell_size:
            return None
        return (x // self.cell_size, y // self.cell_size)

    def handle_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            print(cell)
        else:
            print(None)

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
