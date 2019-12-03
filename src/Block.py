import pygame as pg

class Block(pg.sprite.Sprite):

    def __init__(self,x,y,width,height):
        pg.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pg.surface([width,height])
        self.rect = self.image.get_rect()
