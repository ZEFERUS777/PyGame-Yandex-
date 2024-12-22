import sys

import pygame

pygame.init()

SIZE = width, height = (600, 95)
screen = pygame.display.set_mode(SIZE)

WHITE = (255, 255, 255)

car_pos_x = 5
car_pos_y = 5

car_speed = 10


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("data/car2.png")
        self.rect = self.image.get_rect()
        self.pos_x = car_pos_x
        self.pos_y = car_pos_y

    def update(self, side: str):
        if side == "left":
            self.pos_x -= car_speed
        if side == "right":
            self.pos_x += car_speed

    def render(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))

    def reflect(self):
        self.image = pygame.transform.flip(self.image, True, False)


car = Car()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and car.pos_x > -1:
                car.update('left')
            if event.key == pygame.K_RIGHT and car.pos_x < 460:
                car.update('right')
            if car.pos_x >= 455 or car.pos_x <= 0:
                car.reflect()

    screen.fill(WHITE)
    car.render(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
