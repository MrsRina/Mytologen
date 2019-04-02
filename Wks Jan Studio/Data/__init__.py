##########
# Pygame #
################################################
import pygame as FEngine # pygame like FEngine #
################################################

import json
import math
import sys
import os

class _json(object):
	def __init__(self, path):
		try:
			self.path           = path		
			self.open_file_json = open(self.path, "r+")
			self.file_json      = json.load(self.open_file_json)
		except:
			raise
		return None

	def get(self, value):
		try:
			return self.file_json[value]
		except:
			raise
		return None

	def new(self, value, value_end):
		try:
			self.file_json[value] = value_end

			self.path.seek(0)

			json.dump(self.file_json, self.path)

			self.path.truncate()
		except:
			raise
		return None


global config

config = _json("config.json")

from far_raw import *

# // Initalize system settings
system_initalize(config.file_json)