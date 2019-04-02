from __init__ import config, FEngine, config, sys

class Aplication_Game:
	def __init__(self):
		try:
			self.Far_Game_Window_Width  = int(config.get("Resolution Width"))
			self.Far_Game_Window_Height = int(config.get("Resolution Height"))

			FEngine.init()

			FEngine.display.set_mode((self.Far_Game_Window_Width, self.Far_Game_Window_Height), FEngine.DOUBLEBUF)

			FEngine.display.set_caption(config.get("Title"))

			self.Far_Game_Window_Runing = True

			while (self.Far_Game_Window_Runing):
				# Sync default settings
				self.sync_event_quit()

				FEngine.display.flip()

		except:
			raise
		return None

	def sync_event_quit(self):
		try:
			for event in FEngine.event.get():
				if event.type == FEngine.QUIT:
					self.Far_Game_Window_Runing = False
					sys.exit()
		except:
			raise
		return None


# Run
Aplication_Game()