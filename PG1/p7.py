import random
import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BLOCK_SIZE = 10
BLOCK_SPEED = 10
fps = 30

pg.init()

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render(self, screen):
        pg.draw.rect(screen, GREEN, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

class Food:
    def __init__(self, screen_x, screen_y):
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.update_position()

    def update_position(self):
        self.fx = random.randint(0, (self.screen_x - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.fy = random.randint(0, (self.screen_y - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.coord = (self.fx, self.fy)

    def render(self, screen):
        pg.draw.rect(screen, RED, (self.fx, self.fy, BLOCK_SIZE, BLOCK_SIZE))

class Snake:
    def __init__(self):
        self.blocks = [Block(100, 100)]
        self.direction = 'RIGHT'
        self.grow = False

    def move(self):
        head = self.blocks[0]
        new_head = Block(head.x, head.y)

        if self.direction == 'UP':
            new_head.y -= BLOCK_SIZE
        elif self.direction == 'DOWN':
            new_head.y += BLOCK_SIZE
        elif self.direction == 'LEFT':
            new_head.x -= BLOCK_SIZE
        elif self.direction == 'RIGHT':
            new_head.x += BLOCK_SIZE

        self.blocks.insert(0, new_head)

        if not self.grow:
            self.blocks.pop()
        else:
            self.grow = False

    def change_direction(self, direction):
        if (direction == 'UP' and self.direction != 'DOWN') or \
                (direction == 'DOWN' and self.direction != 'UP') or \
                (direction == 'LEFT' and self.direction != 'RIGHT') or \
                (direction == 'RIGHT' and self.direction != 'LEFT'):
            self.direction = direction

    def render(self, screen):
        for block in self.blocks:
            block.render(screen)

    def check_collision(self, food):
        head = self.blocks[0]
        return (head.x, head.y) == (food.fx, food.fy)

    def check_self_collision(self):
        head = self.blocks[0]
        for block in self.blocks[1:]:
            if (head.x, head.y) == (block.x, block.y):
                return True
        return False

def main():
    screen_x = 600
    screen_y = 600
    screen = pg.display.set_mode((screen_x, screen_y))
    pg.display.set_caption("Snake")
    clock = pg.time.Clock()
    screen.fill(WHITE)

    food = Food(screen_x, screen_y)
    snake = Snake()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    snake.change_direction('UP')
                elif event.key == pg.K_DOWN:
                    snake.change_direction('DOWN')
                elif event.key == pg.K_LEFT:
                    snake.change_direction('LEFT')
                elif event.key == pg.K_RIGHT:
                    snake.change_direction('RIGHT')

        snake.move()

        if snake.check_collision(food):
            snake.grow = True
            food.update_position()

        if snake.check_self_collision() or \
                snake.blocks[0].x < 0 or snake.blocks[0].x >= screen_x or \
                snake.blocks[0].y < 0 or snake.blocks[0].y >= screen_y:
            running = False

        screen.fill(WHITE)
        snake.render(screen)
        food.render(screen)
        pg.display.update()
        clock.tick(fps)

    pg.quit()

if __name__ == '__main__':
    main()