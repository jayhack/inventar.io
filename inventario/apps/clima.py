from ..app_base import EmailAppBase
import forecastio

class App(EmailAppBase):
	"""
	App: Clima
	==========
	Returns current weather in Havana
	"""

	#=====[ Metadata	]=====
	dependencies = ['forecastio']
	API_KEY = '1f5afb17bcb9c1b1a63b2349866a89a8'
	from_email = 'clima@ivioapp.com'

	def process(self, mail):
		#=====[ Step 1: get forecast	]=====
		tiempo = forecastio.load_forecast(self.API_KEY, 23.1333, 82.3833)

		#=====[ Step 2: send result	]=====
		self.email_client.send_message(	
										self.from_email,
										mail.user, 
										'prognostico del tiempo', 
										str(tiempo.hourly())
									)
