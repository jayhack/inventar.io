"""
Module: clima
=============

Contains app Clima, which returns a weather report 
to the user
"""
from app_base import AppBase
import forecastio

class App(AppBase):
	"""
	App: ClimaApp
	=============

	Returns current weather in Havana
	"""
	#=====[ metadata ]=====
	name = 'clima'
	hook = '/clima'
	API_KEY = '1f5afb17bcb9c1b1a63b2349866a89a8'

	def __init__(self, db_client, mail_client):
		super(App, self).__init__(db_client, mail_client)

	def process(self, mail):
		tiempo = forecastio.load_forecast(self.API_KEY, 23.1333, 82.3833)
		self.mail_client.send_message(mail.user, 'clima prognostico', 
										str(tiempo.hourly()))
