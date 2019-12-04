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
        self.all_sprites = pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.enemy_bullet_list = pygame.sprite.Group()
        self.ship_bullet_list = pygame.sprite.Group()

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
        self.all_sprites.empty()
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


        begin_x = 10
        begin_y = 10
        row = 5
        column = 6
        x_int = 0
        y_int = 0
        num_enemies = 30
        for x in range(column):
            for y in range(row):
                enemy = Enemy.Enemy(begin_x+x*75,begin_y+y*50)
                self.enemy_list.add(enemy)
                self.all_sprites.add(enemy)

        ship = Ship.Ship(250, 575)
        block = Block.Block(400, 400, 10, 10)

        self.all_sprites.add(ship)
        self.all_sprites.add(block)
        self.block_list.add(block)
        score = 0
        life = 3
        shoot_control = True

        while self.state == "GAME":
            self.background.fill((0, 0, 0))
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        ship.move_left()
                        shoot_control = True
                    elif event.key == pygame.K_RIGHT:
                        ship.move_right()
                        shoot_control = True
                    elif event.key == pygame.K_SPACE and shoot_control:
                        ship_bullet = Ship_bullet.shipBullet(ship.rect.x+10, ship.rect.y - 5)
                        self.all_sprites.add(ship_bullet)
                        self.ship_bullet_list.add(ship_bullet)
                        shoot_control = False

            for enemy in self.enemy_list:
                if random.randrange(1000) == 0:
                    enemy_bullet = Enemy_bullet.enemyBullet(enemy.rect.x + 10, enemy.rect.y + 5)
                    self.all_sprites.add(enemy_bullet)
                    self.enemy_bullet_list.add(enemy_bullet)

            for bullet in self.ship_bullet_list:  # check for collision
                enemy_hits = pygame.sprite.spritecollide(bullet, self.enemy_list, dokill=True)
                block_hits = pygame.sprite.spritecollide(bullet, self.block_list, dokill=True)
                for enemy in enemy_hits:
                    bullet.kill()
                    score += 1
                for block in block_hits:
                    bullet.kill()

            for bullet in self.enemy_bullet_list:
                ship_hit = pygame.sprite.collide_rect(bullet, ship)
                block_hits = pygame.sprite.spritecollide(bullet, self.block_list, dokill=True)
                for block in block_hits:
                    bullet.kill()
                if ship_hit:
                    bullet.kill()
                    life -= 1

            # redraw the entire screen
            self.all_sprites.update()
            for enemy in self.enemy_list:
                enemy.movingCloser()
            self.screen.blit(self.background, (0, 0))
            if (life == 0 or life < 0):
                self.state = "GAMEOVER"

            font = pygame.font.SysFont(None, 30, True)
            enemy_left = font.render("Enemies Remaining:" + str(len(self.enemy_list.sprites())), False, (250, 0, 0))

            self.screen.blit(enemy_left, (10, 50))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

    # score
        def updateFile(self):
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


