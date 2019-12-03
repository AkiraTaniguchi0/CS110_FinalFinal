import pygame as pygame

class Block(pygame.sprite.Sprite):

    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface([width,height])
        self.rect = self.image.get_rect()
