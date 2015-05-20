"""
Module: clima
=============

Contains app Clima, which returns a weather report 
to the user
"""
import sys
sys.path.append('../')
from app_base import AppBase

import forecastio

class App(AppBase):
	"""
	App: Clima
	==========
	Returns current weather in Havana
	"""
	API_KEY = '1f5afb17bcb9c1b1a63b2349866a89a8'

	def process(self, mail):
		tiempo = forecastio.load_forecast(self.API_KEY, 23.1333, 82.3833)
		self.mail_client.send_message(mail.user, 'prognostico del tiempo', 
										str(tiempo.hourly()))
