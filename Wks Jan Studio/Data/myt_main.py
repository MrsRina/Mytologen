from define import *

from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *

import pygame as MYengine # I used pygame as myengine for not having code conflicts

import json
import math
import sys
import os

class level_procedural(object):
	def __init__(self, floor_top = None, floor_bottom = None):
		try:
			
		except:
			raise
		return None

class Aplication_Game:
	def __init__(self):
		try:
			MYengine.init()

			self.Myt_Game_Window = MYengine.display.set_mode((int(config.get("Resolution Width")), int(config.get("Resolution Height"))),
								   MYengine.DOUBLEBUF | MYengine.FULLSCREEN | MYengine.OPENGLBLIT)

			MYengine.display.set_caption(config.get("Title"))

			self.Myt_Game_Window_Runing = True

			self.opengl_init()

			# events:
			self.scene_construct()

			self.tps_manager = MYengine.time.Clock()

			while (self.Myt_Game_Window_Runing):				
				for Myt_Game_Window_Cache_Event in MYengine.event.get():
					self.Myt_Game_Window_Event = load_event(Myt_Game_Window_Cache_Event, self.Myt_Game_Window, int(config.get("Resolution Width")), int(config.get("Resolution Height")))

					self.Myt_Game_Window_Event.quit(self.Myt_Game_Window_Runing)

				self.tps_manager.tick(int(config.get("TPS")))
				
				glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
				glClearColor(190/255, 190/255, 190/255, 0)

				# Scene constructor spawn:
				self.Myt_Game_Floor_Object.render_to(self.Myt_Game_Window)

				MYengine.display.flip()
		except:
			raise
		return None

	def scene_construct(self):
		try:
			self.Myt_Game_Floor_Object = game_object("Floor-0", path = scenes_objects["floor_0"])
			
		except:
			raise
		return None

	def opengl_init(self):
		try:
			glEnable(GL_TEXTURE_2D)
			glMatrixMode(GL_PROJECTION)
			glOrtho(0, int(config.get("Resolution Width")), int(config.get("Resolution Height")), 0, -1, 1)
			glMatrixMode(GL_MODELVIEW)
			glLoadIdentity()
		except:
			raise
		return None

if __name__ == "__main__":
	Aplication_Game()