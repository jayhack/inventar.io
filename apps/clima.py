from inventario import MailAppBase
import forecastio

class App(MailAppBase):
	"""
	App: Clima
	==========
	Returns current weather in Havana
	"""

	#=====[ Metadata	]=====
	dependencies = ['forecastio']
	API_KEY = '1f5afb17bcb9c1b1a63b2349866a89a8'

	def process(self, mail):
		tiempo = forecastio.load_forecast(self.API_KEY, 23.1333, 82.3833)
		self.email_client.send_message(mail.user, 'prognostico del tiempo', 
										str(tiempo.hourly()))
