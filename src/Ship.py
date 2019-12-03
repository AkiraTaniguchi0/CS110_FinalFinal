import pygame as pg
from src import Ship_bullet
class Ship(pg.sprite.Sprite):

    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.speed = 5
        self.health = 1

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def update(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.Ship.move_left()

            elif event.key == pygame.K_RIGHT:
                self.Ship.move_right()

            elif event.key == pygame.K_SPACE:
                ship_bullet = Ship_bullet.shipBullet()
                ship_bullet.rect.x = ship.rect.x
                ship_bullet.rect.y = ship.rect.y - 3
                all_sprites.add(ship_bullet)
                ship_bullet_list.add(ship_bullet)
