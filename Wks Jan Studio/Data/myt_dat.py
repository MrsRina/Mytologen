import pygame as MYengine

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

class player(object):
	def __init__(self):
		try:
			pass
		except:
			raise
		return None