import pygame as pygame
from src import Ship_bullet
import controller
class Ship(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/ship.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.health = 1

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_left()

                elif event.key == pygame.K_RIGHT:
                    self.move_right()

                elif event.key == pygame.K_SPACE:
                    ship_bullet = Ship_bullet.shipBullet(self.rect.x,self.rect.y-3)
                    all_sprites.add(ship_bullet)
                    ship_bullet_list.add(ship_bullet)
