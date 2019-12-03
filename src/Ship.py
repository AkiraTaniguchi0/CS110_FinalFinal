import pygame as pygame
from src import Ship_bullet
import controller
class Ship(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/ship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(25,25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.health = 1

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.x <= 50:
            self.rect.x = 50

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.x >= 750:
            self.rect.x = 750