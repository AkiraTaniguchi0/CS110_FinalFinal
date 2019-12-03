import pygame as pygame

class enemyBullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([5,10])
        self.image.fill((0,0,255))
        self.rect = self.image.get_rect()
        self.speed = 5
        self.rect.x = x
        self.rect.y = y

def update(self):
        self.rect.y -= self.speed
        if self.rect.y > 700 or self.rect.y < 0:
            self.kill()
