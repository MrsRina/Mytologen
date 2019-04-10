import pygame as MYengine

import json
import math
import sys
import os

import logging

logging.basicConfig()
logging.basicConfig(level = logging.DEBUG)

def replace_folder(remove, place):
	try:
		cache      = os.path.realpath(__file__)
		cahce_path = cache.replace("\\", "/")
		
		path = cahce_path.replace(remove, place)
		
		return path
	except:
		raise
	return None

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

			self.open_file_json.seek(0)

			json.dump(self.file_json, self.open_file_json)

			self.open_file_json.truncate()
		except:
			raise
		return None

global config

config = _json(replace_folder("/data/define.py", "/config.json"))

from myt_raw import *

# // Initalize system settings
system_initalize(config)

from myt_dat import *