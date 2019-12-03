import sys
import pygame
import random
from src import Enemy_bullet
from src import Ship_bullet
from src import Enemy
from src import Ship


class Controller:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        pygame.font.init()
        self.state = "GAME"

    def createGroups(self):
        all_sprites = pg.sprite.Group()
        block_list = pg.sprite.Group()
        enemy_list = pg.sprite.Group()
        enemy_bullet_list = pg.sprite.Group()
        ship_bullet_list = pg.sprite.Group()

    def setupSprites(self):
        createGroups()
        begin_x = 10
        begin_y = 10
        row = 5
        column = 6
        x = 0
        y = 0
        for i in range(row):
            for i in range(column):
                enemy = enemy.Enemy(begin_x + x, begin_y + y)
                all_sprites.add(enemy)
                enemy_list.add(enemy)
                y += 20
                x += 25

        ship = ship.Ship(400, 675)

        block = block.Block(400, 600, 5, 5)

        all_sprites.add(ship)
        all_sprites.add(block)
        block_list.add(block)

    def mainLoop(self):
        while True:
            if (self.state == "GAME"):
                self.gameLoop()
            elif (self.state == "GAMEOVER"):
                self.gameOver()

    def gameOver(self):
        font = pygame.font.SysFont(None, 30)
        msg = font.render("Click Screen To Play Again", False, (0, 0, 0))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()

        while self.state == "GAMEOVER":
            event = pygame.event.poll():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_y:
                    self.state == "GAME"
                elif event.type == pygame.K_n:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

    def gameIntro(self):
        self.screen.fill(255, 255, 255)
        text = pygame.font.Font('freesansbold.ttf', 115)
        textSurf, textRect = ('Galaxy Defender: Press Y to play or N to quit', largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        self.screen.blit(textSurf, textRect)
        pygame.display.update()

        while True:
            event = pygame.event.poll():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    break
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()


    def gameLoop(self):
        pygame.key.set_repeat(1, 50)

        gameIntro()

        life = 3
        setupSprites()

        while self.state == "GAME":
            self.background.fill(250, 250, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            for bullet in ship_bullet_list:  # check for collision
                enemy_hits = pg.sprite.spritecollide(bullet, enemy_list, dokill=True)
                block_hits = pg.sprite.spritecollide(bullet, block_list, dokill=True)
                for enemy in enemy_hits:
                    bullet.kill()
                    score += 1
                for block in block_hits:
                    bullet.kill()

            for bullet in enemy_bullet_list:
                ship_hit = pg.sprite.collide_rect(bullet, ship)
                block_hits = pg.sprite.spritecollide(bullet, block_list, dokill=True)
                for block in block_hits:
                    bullet.kill()
                if ship_hit:
                    spaceship.rect.x = 390
                    spaceship.rect.y = 290
                    life -= 1

            # redraw the entire screen
            all_sprites.enemy.update()
            for enemy in enemy_list:
                enemy.movingCloser()
            self.screen.blit(self.background, (0, 0))
            if (life == 0):
                self.state = "GAMEOVER"
            font = pygame.fontSysFont(None, 30, True)
            enemy_left = font.render("Enemies Remaining:" + str(len(self.enemies)), False, (250, 0, 0))
            self.screen.blit(enemy_left, (10, 50))
            self.all_sprite.draw(self.screen)
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


