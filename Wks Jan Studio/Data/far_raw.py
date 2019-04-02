import ctypes

command = ctypes.windll.user32

GetSystemMetrics = command.GetSystemMetrics

class system_initalize(object):
	def __init__(self, json_init):
		try:
			self.title = "Farmafia" 

			self.resolution_width  = GetSystemMetrics(0)
			self.resolution_height = GetSystemMetrics(1)

			if json_init["Resolution Width"]  == self.resolution_width :
				return ("Resolution Width: {}".format(json_init["Resolution Width"]))
			else:
				json_init["Resolution Width"] = self.resolution_width

			if json_init["Resolution Height"] == self.resolution_height : return ("Resolution Height: {}".format(json_init["Resolution Height"]))
		except:
			raise
		return None