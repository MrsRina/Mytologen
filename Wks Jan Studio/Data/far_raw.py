import ctypes

command = ctypes.windll.user32

GetSystemMetrics = command.GetSystemMetrics

class system_initalize(object):
	def __init__(self, json_init):
		try:
			self.title = "Farmafia" 

			self.resolution_width  = GetSystemMetrics(0)
			self.resolution_height = GetSystemMetrics(1)

			# set Width _ Height
			json_init.new("Resolution Width",  str(self.resolution_width))
			json_init.new("Resolution Height", str(self.resolution_height))

		except:
			raise
		return None