from define import *

import pygame as FEngine

import json
import math
import sys
import os

class Aplication_Game:
	def __init__(self):
		try:
			self.Far_Game_Window_Width  = int(config.get("Resolution Width"))
			self.Far_Game_Window_Height = int(config.get("Resolution Height"))

			FEngine.init()

			self.Far_Game_Window = FEngine.display.set_mode((self.Far_Game_Window_Width, self.Far_Game_Window_Height), FEngine.DOUBLEBUF)

			FEngine.display.set_caption(config.get("Title"))

			self.Far_Game_Window_Runing = True

			while (self.Far_Game_Window_Runing):
				for Far_Game_Window_Cache_Event in FEngine.event.get():
					self.Far_Game_Window_Event = load_event(Far_Game_Window_Cache_Event, self.Far_Game_Window, self.Far_Game_Window_Width, self.Far_Game_Window_Height)

					self.Far_Game_Window_Event.quit(self.Far_Game_Window_Runing)

				FEngine.display.flip()

		except:
			raise
		return None

if __name__ == "__main__":
	Aplication_Game()