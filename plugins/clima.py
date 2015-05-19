"""
Module: clima
=============

Contains app Clima, which returns a weather report 
to the user
"""
from yapsy.IPlugin import IPlugin
from app_base import AppInterface
import forecastio

class ClimaApp(IPlugin):
	"""
	App: ClimaApp
	=============

	Returns current weather in Havana
	"""
	#=====[ metadata ]=====
	implements = (AppInterface,)
	name = 'clima'
	hook = '/clima'
	API_KEY = '1f5afb17bcb9c1b1a63b2349866a89a8'

	def __init__(self, db_client, mail_client):
		super(InventarioAppBase, self).__init__(db_client, mail_client)

	def process(self, mail):
		tiempo = forecastio.load_forecast(self.API_KEY, 23.1333, 82.3833)
		mail.client.send_message(mail.user, 'tiempo', str(tiempo.hourly()))
