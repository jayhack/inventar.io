from ..app_base import EmailAppBase
import forecastio

class App(EmailAppBase):
	"""
	App: Clima
	==========
	Returns weather forecast for next 3 hours
	"""

	#=====[ Metadata	]=====
	dependencies = ['forecastio']
	API_KEY = '1f5afb17bcb9c1b1a63b2349866a89a8'
	from_email = 'clima@ivioapp.com'
	header = 'Prognostico del Tiempo%s======================'


	def make_response(self, forecast):
		"""forecastio forecast -> response"""
		return """
Prognostico del Tiempo
======================

Current:
--------
%s

Hourly:
-------
%s

Daily:
------
%s
""" 	% (	
			forecast.currently().summary, 
			forecast.hourly().summary, 
			forecast.daily().summary
			)




	def process(self, mail):
		#=====[ Step 1: get forecast	]=====
		forecast = forecastio.load_forecast(self.API_KEY, 23.1333, 82.3833)

		#=====[ Step 2: send result	]=====
		body = self.make_response(forecast)
		self.email_client.send_message(	
										self.from_email,
										mail.user, 
										'Prognostico del Tiempo', 
										body
									)
