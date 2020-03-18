from pygame.locals import * 
import pygame

class Stick:
	def __init__(self, size, x, y):
		self.size = size
		self.x = x
		self.y = y

	def render(self, surface, stickImage):
		for i in range(self.size): 
			surface.blit(stickImage, (self.x, self.y - i*20))
			surface.blit(stickImage, (self.x, self.y + i*20))

	def moveUp(self):
		self.y-=1

	def moveDown(self):
		self.y+=1


class App:
	windowWidth = 1000
	windowHeight = 600

	def __init__(self):
		self._background = None
		self._image = None
		self._stick1 = Stick(5, 50, 250)
		self._stick2 = Stick(5, 950, 250)

	def init(self):
		pygame.init()
		self._background = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)
		pygame.display.set_caption('my snake game')
		self._image = pygame.image.load('stick.jpg').convert()

	def loop(self):
		pass

	def render(self):
		self._background.fill((0,0,0))
		self._stick1.render(self._background, self._image)
		self._stick2.render(self._background, self._image)
		pygame.display.flip()

	def quit_game(self):
		pygame.quit()
		
	def execute(self):
		self.init()
		while (True): 
			pygame.event.pump()
			keys = pygame.key.get_pressed()

			if (keys[K_ESCAPE]):
				self.quit_game()

			if (keys[K_UP]):
				self._stick2.moveUp()

			if (keys[K_DOWN]):
				self._stick2.moveDown()

			if (keys[K_w]): 
				self._stick1.moveUp()

			if (keys[K_s]): 
				self._stick1.moveDown()

			self.loop()
			self.render()
		quit_game()

if __name__== "__main__":
	APP = App()
	APP.execute()