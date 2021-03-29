import sys
import pygame

from game_objects import Player, Background
from settings import WIDTH, HEIGHT

pygame.init()
pygame.display.set_caption('My game')

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

all_objects = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player(clock, bullets)
background = Background()

all_objects.add(background)
all_objects.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255, 255, 255))

    all_objects.update()
    bullets.update()
    all_objects.draw(screen)
    bullets.draw(screen)

    # player.update()
    # screen.blit(background.image, background.rect)
    # screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(30)
