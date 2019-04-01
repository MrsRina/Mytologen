import pygame as FEngine

import json
import math
import sys
import os

def load_json(path):
	try:
		open_file_json = open(path, "r+")

		file_json = json.load(file)

		_json = json.dump(file_json)

		return _json
	except:
		raise
	return None

from .far_raw import 