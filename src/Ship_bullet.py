import pygame as pg

class shipBullet(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5,10])
        self.image.fill(255,0,0)
        self.rect = self.image.get_rect()
        self.speed = 5

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > 800 or self.rect.y < 0:
            self.kill()
