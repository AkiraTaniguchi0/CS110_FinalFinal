import sys
import pygame
import random
from src import Enemy_bullet
from src import Ship_bullet
from src import Enemy
from src import Ship
from src import Block

class Controller:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        pygame.font.init()
        self.state = "GAME"

    def mainLoop(self):
        while True:
            if (self.state == "GAME"):
                self.gameLoop()
            elif (self.state == "GAMEOVER"):
                self.gameOver()

    def gameIntro(self):
        #self.screen.fill((255, 255, 255))

        background = self.background
        background.fill((0, 0, 0))

        font = pygame.font.Font('freesansbold.ttf', 20)
        title = pygame.image.load("assets/galaxy_defender.png").convert_alpha()
        titlepos = title.get_rect()
        titlepos.centerx = background.get_rect().centerx
        text = font.render('Press Y to play or N to quit', 1,(255,255,255))
        textpos = text.get_rect()
        textpos.centerx = background.get_rect().centerx
        textpos.centery = background.get_rect().centery
        background.blit(text, textpos)
        background.blit(title, titlepos)
        self.screen.blit(background, (0, 0))
        pygame.display.update()

        while True:
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    break
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def gameOver(self):
        font = pygame.font.SysFont(None, 30)
        msg = font.render("Click Screen To Play Again", False, (0, 0, 0))
        self.screen.blit(msg, (self.width / 2, self.height / 2))
        pygame.display.flip()

        while self.state == "GAMEOVER":
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_y:
                    self.state == "GAME"
                elif event.type == pygame.K_n:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def gameLoop(self):
        pygame.key.set_repeat(1, 50)

        self.gameIntro()

        all_sprites = pygame.sprite.Group()
        block_list = pygame.sprite.Group()
        enemy_list = pygame.sprite.Group()
        enemy_bullet_list = pygame.sprite.Group()
        ship_bullet_list = pygame.sprite.Group()
        begin_x = 10
        begin_y = 10
        row = 5
        column = 6
        x_int = 0
        y_int = 0
        num_enemies = 30
        for i in range(num_enemies):
            for x in range(column):
                for y in range(row):
                    enemy = Enemy.Enemy(begin_x+x*100,begin_y+y*100)
                    enemy_list.add(enemy)
                    all_sprites.add(enemy)

        """for x in range(row):
            enemy = Enemy((10 + (x * 25)), begin_y)
            for y in range(column):
                enemy = Enemy(begin_x, begin_y + y_int)
                all_sprites.add(enemy)
                enemy_list.add(enemy)
                y_int += 20"""

        ship = Ship.Ship(250, 250)
        block = Block.Block(400, 600, 5, 5)

        all_sprites.add(ship)
        all_sprites.add(block)
        block_list.add(block)

        life = 3

        while self.state == "GAME":
            self.background.fill((250, 250, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for bullet in ship_bullet_list:  # check for collision
                enemy_hits = pygame.sprite.spritecollide(bullet, enemy_list, dokill=True)
                block_hits = pygame.sprite.spritecollide(bullet, block_list, dokill=True)
                for enemy in enemy_hits:
                    bullet.kill()
                    score += 1
                for block in block_hits:
                    bullet.kill()

            for bullet in enemy_bullet_list:
                ship_hit = pygame.sprite.collide_rect(bullet, ship)
                block_hits = pygame.sprite.spritecollide(bullet, block_list, dokill=True)
                for block in block_hits:
                    bullet.kill()
                if ship_hit:
                    spaceship.rect.x = 390
                    spaceship.rect.y = 290
                    life -= 1

            # redraw the entire screen
            all_sprites.update()
            for enemy in enemy_list:
                enemy.movingCloser()
            self.screen.blit(self.background, (0, 0))
            if (life == 0):
                self.state = "GAMEOVER"
            font = pygame.font.SysFont(None, 30, True)
            enemy_left = font.render("Enemies Remaining:" + str(len(enemy_list.sprites())), False, (250, 0, 0))

            self.screen.blit(enemy_left, (10, 50))
            all_sprites.draw(self.screen)
            pygame.display.flip()

    # score list
    def updateFile(self):
        """Keeps track of and updates score"""
        f = open('scores.txt', 'r')
        file = f.readlines()
        last = int(file[0])
        if last < int(score):
            f.close()
            file = open('scores.txt', 'w')
            file.write(str(score))
            file.close()
            return score
        return last


