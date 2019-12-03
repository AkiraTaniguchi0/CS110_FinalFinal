import pygame,sys
from pygame.locals import *


import random
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/invader.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(30,20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = "right"
        self.speed = 1
        self.closer = False
        self.health = 3
        self.difficulty = 0

    def update(self):
        if self.direction == "right" and self.rect.x < 770:
            self.rect.x += self.speed

        elif self.direction == "right" and self.rect.x >= 770:
            self.rect.x = 750
            self.closer = True
            self.direction = "left"

        elif self.direction == "left" and self.rect.x > 30:
            self.rect.x -= self.speed

        elif self.direction == "left" and self.rect.x <= 30:
            self.rect.x = 30
            self.closer = True
            self.direction = "right"

    def movingCloser(self):
        if self.closer:
            self.rect.y += 25
            self.closer = False
        #self.closer determines if an enemy hits the side of the screen, which will make them move down
