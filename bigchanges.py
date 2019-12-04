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
        self.background = pygame.image.load("assets/spacebackground.png").convert()
        self.background1 = pygame.image.load("assets/spacebackground.png").convert()
        pygame.font.init()
        pygame.display.set_caption("Galaxy Defender")
        self.all_sprites = pygame.sprite.Group()
        self.block_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.enemy_bullet_list = pygame.sprite.Group()
        self.ship_bullet_list = pygame.sprite.Group()
        self.life = 3
        self.score = 0
        self.level = 1
        self.nextlevel = False
        self.state = True

    def mainLoop(self):
        while True:
            if self.state:
                self.screen.blit(self.background, [0,0])
                self.gameLoop()
            elif not self.state:
                self.screen.blit(self.background, [0,0])
                self.gameOver()

    def gameIntro(self):
        font = pygame.font.Font('freesansbold.ttf', 20)
        title = pygame.image.load("assets/galaxy_defender.png").convert_alpha()
        titlepos = title.get_rect()
        titlepos.centerx = self.screen.get_rect().centerx
        text1 = font.render('You Must Move With Arrow Keys Before Firing Another Bullet With Space Bar.', 1, (200,255,255))
        text2 = font.render('When Aliens Hit The Barrier Layer, All Barriers Will Be Destroyed.', 1, (200,255,255))
        text3 = font.render("Bullets Kill You; You Have 1 Life.", 1, (200,255,255))
        text4 = font.render("Eliminate All Aliens To Progress To The Next Level; Levels Increase In Difficulty.", 1, (200,255,255))
        text5 = font.render("Each Alien Kill = 1 Point; Each Barrier Block Remaining = 1 Point.", 1, (200,255,255))
        text = font.render('Press Y To Play Or N To Quit.', 1, (255,200,255))
        textpos = text.get_rect()
        textpos.centerx = self.screen.get_rect().centerx
        textpos.centery = self.screen.get_rect().centery - 30
        text1pos = text1.get_rect()
        text2pos = text2.get_rect()
        text3pos = text3.get_rect()
        text4pos = text4.get_rect()
        text5pos = text5.get_rect()
        text1pos.centerx = self.screen.get_rect().centerx
        text1pos.centery = self.screen.get_rect().centery
        text2pos.centerx = self.screen.get_rect().centerx
        text2pos.centery = self.screen.get_rect().centery + 30
        text3pos.centerx = self.screen.get_rect().centerx
        text3pos.centery = self.screen.get_rect().centery + 60
        text4pos.centerx = self.screen.get_rect().centerx
        text4pos.centery = self.screen.get_rect().centery + 90
        text5pos.centerx = self.screen.get_rect().centerx
        text5pos.centery = self.screen.get_rect().centery + 120
        self.background.blit(text1, text1pos)
        self.background.blit(text2, text2pos)
        self.background.blit(text3, text3pos)
        self.background.blit(text4, text4pos)
        self.background.blit(text5, text5pos)
        self.background.blit(text, textpos)
        self.background.blit(title, titlepos)
        self.screen.blit(self.background, (0, 0))
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
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Thanks for playing", 1, (255, 255, 255))
        textpos = text.get_rect()
        textpos.centerx = self.screen.get_rect().centerx
        textpos.centery = self.screen.get_rect().centery
        text1 = font.render("Press Any Key To Exit", 1, (255,200,255))
        text1pos = text1.get_rect()
        text1pos.centerx = self.screen.get_rect().centerx
        text1pos.centery = self.screen.get_rect().centery + 60
        self.background1.blit(text, textpos)
        self.background1.blit(text1, text1pos)
        self.screen.blit(self.background1, (0, 0))
        pygame.display.update()
        event = pygame.event.poll()
        if (event.type == pygame.KEYDOWN) or (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

    def gameLoop(self):
        pygame.display.update()
        pygame.key.set_repeat(1, 50)

        if not self.nextlevel:
            self.gameIntro()

        begin_x = 10
        begin_y = 25
        row = 5
        column = 6
        x_int = 0
        y_int = 0


        num_enemies = 30
        for x in range(column):
            for y in range(row):
                enemy = Enemy.Enemy(begin_x+x*75,begin_y+y*50)
                enemy.speed += self.level
                self.enemy_list.add(enemy)
                self.all_sprites.add(enemy)
        beg_y = 500
        for beg_x in range(50,750,150):
            for i in range(3):
                for j in range(9):
                    block = Block.Block(beg_x + j*10, beg_y + i*10, 10, 10)
                    self.block_list.add(block)
                    self.all_sprites.add(block)



        ship = Ship.Ship(250, 575)
        self.all_sprites.add(ship)

        shoot_control = True

        while self.state:
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
                levelcap = self.level
                if levelcap > 10:
                    levelcap = 10
                if random.randrange(1100 - levelcap*100) == 0:
                    enemy_bullet = Enemy_bullet.enemyBullet(enemy.rect.x + 10, enemy.rect.y + 5)
                    self.all_sprites.add(enemy_bullet)
                    self.enemy_bullet_list.add(enemy_bullet)

            for bullet in self.ship_bullet_list:  # check for collision
                enemy_hits = pygame.sprite.spritecollide(bullet, self.enemy_list, dokill=True)
                block_hits = pygame.sprite.spritecollide(bullet, self.block_list, dokill=True)
                for enemy in enemy_hits:
                    bullet.kill()
                    self.score += 1
                for block in block_hits:
                    bullet.kill()

            for bullet in self.enemy_bullet_list:
                ship_hit = pygame.sprite.collide_rect(bullet, ship)
                block_hits = pygame.sprite.spritecollide(bullet, self.block_list, dokill=True)
                for block in block_hits:
                    bullet.kill()
                if ship_hit:
                    bullet.kill()
                    self.life -= 1

            # redraw the entire screen
            self.all_sprites.update()
            for enemy in self.enemy_list:
                enemy.movingCloser()
                if enemy.rect.y >= 485:
                    for block in self.block_list:
                        block.kill()
            self.screen.blit(self.background, (0, 0))

            font = pygame.font.SysFont(None, 25, True)
            enemy_left = font.render("Enemies Remaining:" + str(len(self.enemy_list.sprites())), False, (250, 0, 0))
            score = font.render("Score:" +str(self.score), False,(250,0,0))
            level = font.render("Level:" + str(self.level),False,(250,0,0))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(enemy_left, (575, 5))
            self.screen.blit(score, (380, 5))
            self.screen.blit(level, (5, 5))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

            if (self.life <= 0):
                self.state = False

            for enemy in self.enemy_list:
                if enemy.rect.y >= 550:
                    self.state = False

            if len(self.enemy_list) == 0:
                self.score += len(self.block_list)
                self.all_sprites.empty()
                for bullet in self.ship_bullet_list:
                    bullet.kill()
                self.nextlevel = True
                self.level += 1
                print(self.score)
                break
    # score
        def updateFile(self):
            f = open('scores.txt', 'r')
            file = f.readlines()
            last = int(file[0])
            if last < int(self.score):
                f.close()
                file = open('scores.txt', 'w')
                file.write(str(self.score))
                file.close()
                return self.score
            return last
