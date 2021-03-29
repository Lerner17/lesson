import pygame

from pygame.sprite import Sprite
from settings import WIDTH, HEIGHT


class Bullet(Sprite):

    SPEED = -15

    def __init__(self, position):
        super(Bullet, self).__init__()

        self.image = pygame.image.load('assets/b.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = position

    def update(self):
        self.rect.move_ip((0, self.SPEED))


class Player(Sprite):

    MAX_SPEED = 10

    def __init__(self, clock, bullets):
        ''' Функция вызывается в момент создания экземпляра класса '''
        super(Player, self).__init__()
        self.clock = clock
        self.bullets = bullets
        self.image = pygame.image.load('assets/player.png') # Загружаем картинку player.png
        self.rect = self.image.get_rect() # Определяем размер нашего объекта
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.current_speed = 0

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.current_speed -= self.MAX_SPEED
        elif keys[pygame.K_RIGHT]:
            self.current_speed += self.MAX_SPEED
        else:
            self.current_speed = 0

        self.rect.move_ip((self.current_speed, 0))
        self.process_shooting()

    def process_shooting(self):
        ''' Функция для стрельбы '''

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.bullets.add(Bullet(self.rect.midtop))


class Background(Sprite):

    def __init__(self):
        super(Background, self).__init__()
        self.image = pygame.image.load('assets/back.png')
        self.rect = self.image.get_rect()

        self.rect.bottom = HEIGHT
