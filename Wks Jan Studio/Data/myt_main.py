from define import *

import pygame as MYengine

import json
import math
import sys
import os

class Aplication_Game:
	def __init__(self):
		try:
			MYengine.init()

			self.Myt_Game_Window = MYengine.display.set_mode((int(config.get("Resolution Width")), int(config.get("Resolution Height"))), MYengine.DOUBLEBUF)

			MYengine.display.set_caption(config.get("Title"))

			self.Myt_Game_Window_Runing = True

			while (self.Myt_Game_Window_Runing):
				for Myt_Game_Window_Cache_Event in MYengine.event.get():
					self.Myt_Game_Window_Event = load_event(Myt_Game_Window_Cache_Event, self.Myt_Game_Window, int(config.get("Resolution Width")), int(config.get("Resolution Height")))

					self.Myt_Game_Window_Event.quit(self.Myt_Game_Window_Runing)

				MYengine.display.flip()

		except:
			raise
		return None

if __name__ == "__main__":
	Aplication_Game()