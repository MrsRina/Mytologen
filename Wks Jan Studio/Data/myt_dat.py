from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *

import pygame as MYengine # I used pygame as myengine for not having code conflicts

import json
import math
import sys
import os

KEY_MOUSE_BINDS = {
	"mouse"    	   : MYengine.MOUSEBUTTONDOWN,
	"mouse-up" 	   : MYengine.MOUSEBUTTONUP,
	"mouse-motion" : MYengine.MOUSEMOTION,
}

class load_event(object):
	def __init__(self, event, display, resolution, json):
		try:
			self.main_event      = event
			self.main_display    = display
			self.main_resolution = resolution
			self.main_json       = json
		except:
			raise
		return None

	def mouse(self, key, value, command):
		try:
			if self.main_event.type is KEY_MOUSE_BINDS[style]:
				if self.main_event.button is value:
					run = True
					while run:
						command()
						run = False
		except:
			raise
		return None

	def quit(self, var):
		try:
			if self.main_event.type == MYengine.QUIT:
				var = False
				sys.exit()
		except:
			raise
		return None

class loadImage(object):
	JANJA_IMAGE=None
	JANJA_IMAGE_DATA=None
	JANJA_DATA_IMAGE=None

	JANJA_COLOR_IMAGE_R=1
	JANJA_COLOR_IMAGE_G=1
	JANJA_COLOR_IMAGE_B=1
	JANJA_COLOR_IMAGE_A=1
	JANJA_COLOR_IMAGE_FORMAT=None

	JANJA_ID_IMAGE=None

	JANJA_TAG_IMAGE=None
	JANJA_PATH_IMAGE=None

	JANJA_IMAGE_RENDERING=False

	JANJA_IMAGE_RENDERING_SET_POS=False

	JANJA_IMAGE_RENDERING_SET_X=False

	JANJA_IMAGE_RENDERING_SET_Y=False

	JANJA_IMAGE_RENDERING_SET_SIZE=False

	JANJA_IMAGE_RENDERING_SET_COLOR=False

	JANJA_IMAGE_RENDERING_SET_NEW_IMAGE=False

	JANJA_IMAGE_RENDERED=False

	def __init__(self, pathImage):
		try:
			self.JANJA_PATH_IMAGE = pathImage

			try:
				self.JANJA_IMAGE_DATA = MYengine.image.load(self.JANJA_PATH_IMAGE)
			except:
				print("Error")

			self.JANJA_DATA_IMAGE = MYengine.image.tostring(self.JANJA_IMAGE_DATA, "RGBX")

			self.JANJA_IMAGE = self.JANJA_IMAGE_DATA.get_rect()
		
			self.JANJA_ID_IMAGE = glGenTextures(1)

			glBindTexture(GL_TEXTURE_2D, self.JANJA_ID_IMAGE)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
			glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)

			glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.JANJA_IMAGE.w, self.JANJA_IMAGE.h, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.JANJA_DATA_IMAGE)
			glBindTexture(GL_TEXTURE_2D, 0)
			
			self.JANJA_TAG_IMAGE = None
		except:
			raise
		return None

	def setPos(self, pos):
		try:
			if self.JANJA_IMAGE_RENDERED == False:
				self.JANJA_IMAGE.x, self.JANJA_IMAGE.y = pos

			elif self.JANJA_IMAGE_RENDERED == True:
				self.JANJA_IMAGE_RENDERING               = False
				self.JANJA_IMAGE_RENDERING_SET_POS       = True
				self.JANJA_IMAGE_RENDERING_SET_X         = False
				self.JANJA_IMAGE_RENDERING_SET_Y         = False
				self.JANJA_IMAGE_RENDERING_SET_SIZE      = False
				self.JANJA_IMAGE_RENDERING_SET_COLOR     = False
				self.JANJA_IMAGE_RENDERING_SET_NEW_IMAGE = False
			
				self.JANJA_IMAGE.x, self.JANJA_IMAGE.y = pos

				if self.JANJA_IMAGE_RENDERING_SET_POS:
					self.create()
		except:
			raise
		return None

	def setX(self, x):
		try:
			if self.JANJA_IMAGE_RENDERED == False:
				self.JANJA_IMAGE.x = x

			elif self.JANJA_IMAGE_RENDERED == True:
				self.JANJA_IMAGE_RENDERING               = False
				self.JANJA_IMAGE_RENDERING_SET_POS       = False
				self.JANJA_IMAGE_RENDERING_SET_X         = True
				self.JANJA_IMAGE_RENDERING_SET_Y         = False
				self.JANJA_IMAGE_RENDERING_SET_SIZE      = False
				self.JANJA_IMAGE_RENDERING_SET_COLOR     = False
				self.JANJA_IMAGE_RENDERING_SET_NEW_IMAGE = False

				self.JANJA_IMAGE.x = x
				
				if self.JANJA_IMAGE_RENDERING_SET_X:
					self.create()
		except:
			raise
		return None

	def setY(self, y):
		try:
			if self.JANJA_IMAGE_RENDERED == False:
				self.JANJA_IMAGE.y = y

			elif self.JANJA_IMAGE_RENDERED == True:
				self.JANJA_IMAGE_RENDERING               = False
				self.JANJA_IMAGE_RENDERING_SET_POS       = False
				self.JANJA_IMAGE_RENDERING_SET_X         = False
				self.JANJA_IMAGE_RENDERING_SET_Y         = True
				self.JANJA_IMAGE_RENDERING_SET_SIZE      = False
				self.JANJA_IMAGE_RENDERING_SET_COLOR     = False
				self.JANJA_IMAGE_RENDERING_SET_NEW_IMAGE = False

				self.JANJA_IMAGE.y = y
				
				if self.JANJA_IMAGE_RENDERING_SET_Y:
					self.create()
		except:
			raise
		return None

	def setColor(self, r, g, b, a):
		try:
			if self.JANJA_IMAGE_RENDERED == False:			
				# Equivalente a cache =  93 bytes (93 bytes):
				janja_cache_color_r, janja_cache_color_g, janja_cache_color_b, janja_cache_color_a=r, g, b, a

				# Implementar cache + 218 bytes (218 bytes):
				self.JANJA_COLOR_IMAGE_R = janja_cache_color_r/255
				self.JANJA_COLOR_IMAGE_G = janja_cache_color_g/255
				self.JANJA_COLOR_IMAGE_B = janja_cache_color_b/255
				self.JANJA_COLOR_IMAGE_A = janja_cache_color_a/255

				# Total:
				# 311 bytes (311 bytes) #
				
			elif self.JANJA_IMAGE_RENDERED == True:
				self.JANJA_IMAGE_RENDERING               = False
				self.JANJA_IMAGE_RENDERING_SET_POS       = False
				self.JANJA_IMAGE_RENDERING_SET_X         = False
				self.JANJA_IMAGE_RENDERING_SET_Y         = False
				self.JANJA_IMAGE_RENDERING_SET_SIZE      = False
				self.JANJA_IMAGE_RENDERING_SET_COLOR     = True
				self.JANJA_IMAGE_RENDERING_SET_NEW_IMAGE = False

				# Equivalente a cache =  93 bytes (93 bytes):
				janja_cache_color_r, janja_cache_color_g, janja_cache_color_b, janja_cache_color_a=r, g, b, a

				# Implementar cache + 218 bytes (218 bytes):
				self.JANJA_COLOR_IMAGE_R = janja_cache_color_r/255
				self.JANJA_COLOR_IMAGE_G = janja_cache_color_g/255
				self.JANJA_COLOR_IMAGE_B = janja_cache_color_b/255
				self.JANJA_COLOR_IMAGE_A = janja_cache_color_a/255

				# Total:
				# 311 bytes (311 bytes) #

				if self.JANJA_IMAGE_RENDERING_SET_COLOR:				
					self.create()
		except:
			raise
		return None

	def setSize(self, width, height):
		try:
			if self.JANJA_IMAGE_RENDERED == False:
				self.JANJA_IMAGE.w = width; self.JANJA_IMAGE.h = height

			elif self.JANJA_IMAGE_RENDERED == True:
				self.JANJA_IMAGE_RENDERING               = False
				self.JANJA_IMAGE_RENDERING_SET_POS       = False
				self.JANJA_IMAGE_RENDERING_SET_X         = False
				self.JANJA_IMAGE_RENDERING_SET_Y         = False
				self.JANJA_IMAGE_RENDERING_SET_SIZE      = True
				self.JANJA_IMAGE_RENDERING_SET_COLOR     = False
				self.JANJA_IMAGE_RENDERING_SET_NEW_IMAGE = False

				self.JANJA_IMAGE.w, self.JANJA_IMAGE.h=width, height
				
				if self.JANJA_IMAGE_RENDERING_SET_SIZE:			
					self.create()
		except:
			raise
		return None

	def setNewImage(self, pathImage, frames=None):
		try:
			if self.JANJA_IMAGE_RENDERED == False:
				self.JANJA_PATH_IMAGE = pathImage

				if os.path.exists(self.JANJA_PATH_IMAGE) == True:
					pass
				else:
					print("Error")

			elif self.JANJA_IMAGE_RENDERED == True:
				self.JANJA_IMAGE_RENDERING               = False
				self.JANJA_IMAGE_RENDERING_SET_POS       = False
				self.JANJA_IMAGE_RENDERING_SET_X         = False
				self.JANJA_IMAGE_RENDERING_SET_Y         = False
				self.JANJA_IMAGE_RENDERING_SET_SIZE      = False
				self.JANJA_IMAGE_RENDERING_SET_COLOR     = False
				self.JANJA_IMAGE_RENDERING_SET_NEW_IMAGE = True

				self.JANJA_PATH_IMAGE = pathImage

				if self.JANJA_IMAGE_RENDERING_SET_NEW_IMAGE:						
					glLoadIdentity()

					self.JANJA_PATH_IMAGE = pathImage
	
					try:
						self.JANJA_IMAGE_DATA=pygame.image.load(self.JANJA_PATH_IMAGE)
					except:
						print("Error")
	
					self.JANJA_DATA_IMAGE = pygame.image.tostring(self.JANJA_IMAGE_DATA, "RGBX")
	
					self.JANJA_IMAGE      = self.JANJA_IMAGE_DATA.get_rect()
				
					self.JANJA_ID_IMAGE   = glGenTextures(1)
	
					glBindTexture(GL_TEXTURE_2D, self.JANJA_ID_IMAGE)
					glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
					glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
		
					glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.JANJA_IMAGE.w, self.JANJA_IMAGE.h, 0, GL_RGBA, GL_UNSIGNED_BYTE, self.JANJA_DATA_IMAGE)
					glBindTexture(GL_TEXTURE_2D, 0)
					
					self.create()
		except:
			raise
		return None

	def setTag(Name):
		try:
			self.JANJA_TAG_IMAGE=Name
		except:
			raise
		return None

	def renderImage(self):
		try:
			self.JANJA_IMAGE_RENDERING = True
			self.JANJA_IMAGE_RENDERED  = True

			if self.JANJA_IMAGE_RENDERING:
				self.create()
		except:
			raise
		return None

	def removeImage(self):
		try:
			self.JANJA_IMAGE_RENDERING               = False
			self.JANJA_IMAGE_RENDERING_SET_POS       = False
			self.JANJA_IMAGE_RENDERING_SET_X         = False
			self.JANJA_IMAGE_RENDERING_SET_Y         = False
			self.JANJA_IMAGE_RENDERING_SET_SIZE      = False
			self.JANJA_IMAGE_RENDERING_SET_COLOR     = False
			self.JANJA_IMAGE_RENDERING_SET_NEW_IMAGE = False
			self.JANJA_IMAGE_RENDERED                = False
		except:
			raise
		return None

	def create(self):
		try:
			glLoadIdentity()

			glColor(self.JANJA_COLOR_IMAGE_R, self.JANJA_COLOR_IMAGE_G, self.JANJA_COLOR_IMAGE_B, self.JANJA_COLOR_IMAGE_A)
			glEnable(GL_BLEND)
			glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
			glBindTexture(GL_TEXTURE_2D, self.JANJA_ID_IMAGE)
			glBegin(GL_QUADS)
			glTexCoord(0, 0); glVertex(self.JANJA_IMAGE.x, self.JANJA_IMAGE.y, 0)
			glTexCoord(0, 1); glVertex(self.JANJA_IMAGE.x, self.JANJA_IMAGE.y + self.JANJA_IMAGE.h, 0)
			glTexCoord(1, 1); glVertex(self.JANJA_IMAGE.x + self.JANJA_IMAGE.w, self.JANJA_IMAGE.y + self.JANJA_IMAGE.h, 0)
			glTexCoord(1, 0); glVertex(self.JANJA_IMAGE.x + self.JANJA_IMAGE.w, self.JANJA_IMAGE.y, 0)
			glEnd(); glBindTexture(GL_TEXTURE_2D, 0)
		
		except:
			raise
		return None

class game_object(object):
	def __init__(self, tag = None, path = None):
		try:
			self.tag   = tag
			self.path  = path

			self.check = 0

			self.create()

		except:
			raise
		return None

	def create(self):
		try:
			self.image = loadImage(self.path)
		except:
			raise
		return None

	def render_to(self, window):
		try:
			self.image.renderImage()
		except:
			raise
		return None

class entity(object):
	def __init__(self, tag, x, y, w, h, color):
		try:
			self.rect  = MYengine.rect.Rect(x, y, w, h)

			self.color = color

			self.tag = tag
		except:
			raise
		return None

	def move_keyboard(self, right = None, left = None, up = None, down = None):
		if right:
			pass		

	def spawn_to(self, window):
		try:
			MYengine.draw.rect(window, self.color, self.rect)
		except:
			raise
		return None