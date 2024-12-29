import pygame
import random

pygame.init()

all_sprites = pygame.sprite.Group()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))


class Mountain(pygame.sprite.Sprite):
    image = pygame.image.load('mountains.png')

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = height


# Создаем горы с случайным смещением по горизонтали
mountain = Mountain()


class Landing(pygame.sprite.Sprite):
    image = pygame.image.load('pt.png')

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = pos

    def update(self):
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect.y += 1


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            landing = Landing(event.pos)
            all_sprites.add(landing)

    all_sprites.update()
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
