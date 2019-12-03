import sys
import pygame
import random
from src import Enemy_bullet
from src import Ship_bullet
from src import Enemy
from src import Ship

class Controller:
	def __init__(self, width = 800, height = 600):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.background = pygame.Surface(self.screen.get_size()).convert()
		pygame.font.init()
		self.state = "INTRO"

#the game intro screen
	def game_intro(self):
		while self.state == "INTRO":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					self.state == "GAME"

			self.screen.fill(255,255,255)
			text = pygame.font.Font('freesansbold.ttf', 115)
			TextSurf, TextRect = ('Galaxy Defender', largeText)
			TextRect.center = ((display_width / 2), (display_height / 2))
			self.screen.blit(TextSurf, TextRect)
			pygame.display.update()

	def createGroups(self):
		all_sprites = pygame.sprite.Group()
		block_list = pygame.sprite.Group()
		enemy_list = pygame.sprite.Group()
		enemy_bullet_list = pygame.sprite.Group()
		ship_bullet_list = pygame.sprite.Group()

	def setupSprites(self):
		createGroups()
		begin_x = 10
		begin_y = 10
		row = 5
		column = 6
		x_int = 0
		y_int = 0
		for x in range(row):
			enemy = Enemy(10 + (x * 25), begin_y)
			for y in range(column):
				enemy = Enemy(begin_x, begin_y + y_int)
				all_sprites.add(enemy)
				enemy_list.add(enemy)
				y_int += 20

		ship = ship.Ship(400,675)

		block = block.Block(400, 600, 5, 5)

		all_sprites.add(ship)
		all_sprites.add(block)
		block_list.add(block)

	def gameOver(self):
		self.Ship.kill()
		font = pygame.font.SysFont(None, 30)
		msg = font.render("Click Screen To Play Again", False, (0,0,0))
		self.screen.blit(message, (self.width / 2, self.height / 2))
		pygame.display.flip()
		while self.state == "GAMEOVER":
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					self.state == "GAME"

	def gameLoop(self):
		pygame.key.set_repeat(1,50)
		life = 3
		setupSprites()
		while self.state == "GAME":
			self.background.fill(250,250,250)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			for bullet in ship_bullet_list:#check for collision
				enemy_hit = pygame.sprite.spritecollide(bullet, enemy_list, dokill=True)
				block_hit = pygame.sprite.spritecollide(bullet, block_list, dokill=True)
			for enemy in enemy_list:
				bullet.kill()
				score += 1
			for block in block_list:
				bullet.kill()
			for bullet in enemy_bullet_list:
				ship_hit = pygame.sprite.collide_rect(bullet, ship)
				block_hit = pygame.sprite.spritecollide(bullet, block_list, dokill=True)
				if ship_hit:
					spaceship.rect.x = 390
					spaceship.rect.y = 290
					life -= 1
	#redraw the entire screen
			all_sprites.enemy.update()
			self.screen.blit(self.background, (0,0))
			if(life == 0):
				self.state = "GAMEOVER"
			font = pygame.fontSysFont(None, 30, True)
			enemy_left = font.render("Enemies Remaining:" + str(len(self.enemies)), False, (250,0,0))
			self.screen.blit(enemy_left, (10,50))
			self.all_sprite.draw(self.screen)
			pygame.display.flip()
	#score list
	def updateFile(self):
		"""Keeps track of and updates score"""
		f = open('scores.txt','r')
		file = f.readlines()
		last = int(file[0])
		if last < int(score):
			f.close()
			file = open('scores.txt', 'w')
			file.write(str(score))
			file.close()
			return score
		return last

	def mainLoop(self):
		while True:
			if(self.state == "GAME"):
				self.gameLoop()
			elif(self.state == "GAMEOVER"):
				self.gameOver()
			elif(self.state == "INTRO"):
				self.game_intro()
