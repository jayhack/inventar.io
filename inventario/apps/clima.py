from ..app_base import EmailAppBase
import forecastio
import pygeocoder

class App(EmailAppBase):
	"""
	App: Clima
	==========
	Returns weather forecast for next 3 hours
	"""


	#=====[ Metadata	]=====
	dependencies = ['forecastio', 'pygeocoder']
	API_KEY = '1f5afb17bcb9c1b1a63b2349866a89a8'
	from_email = 'clima@ivioapp.com'
	header = 'Prognostico del Tiempo%s======================'
	havana_gps = (23.1333, 82.3833)


	def get_gps(self, mail):
		"""mail -> (lat, long) gps coords to be used"""
		if len(mail.subject().strip()) > 3:
			try:
				result = pygeocoder.Geocoder.geocode(mail.subject())
				return result[0].coordinates, mail.subject().strip()
			except:
				return self.havana_gps, 'La Habana'
		else:
			return self.havana_gps, 'La Habana'


	def make_response(self, location, forecast):
		"""forecastio forecast -> response"""
		return """
Prognostico del Tiempo
======================
Tiempo en %s

Current:
--------
%s

Hourly:
-------
%s

Daily:
------
%s
""" 	% (	location,
			forecast.currently().summary, 
			forecast.hourly().summary, 
			forecast.daily().summary
			)

	def process(self, mail):
		#=====[ Step 1: get lat/long	]=====
		gps, location = self.get_gps(mail)

		#=====[ Step 1: get forecast	]=====
		forecast = forecastio.load_forecast(self.API_KEY, gps[0], gps[1])

		#=====[ Step 2: send result	]=====
		body = self.make_response(location, forecast)
		self.email_client.send_message(	
										self.from_email,
										mail.user, 
										'Prognostico del Tiempo', 
										body
									)
