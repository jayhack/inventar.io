import requests

class SMSConCubaClient(object):
	"""
	Class: SMSConCubaClient
	=======================
	Client for accessing SMS functionality via SMS con Cuba

	Usage:
	------
	In [1]: sms_client = SMSConCubaClient()
	In [2]: sms_client.send_message(from_number, to_number, message)
	"""

	#=====[ Metadata	]=====
	send_url = 'http://www.smsconcuba.com/api/send_message'
	from_number = ''
	supported_request_types = ['send_message']

	def __init__(self, username, password):
		self.username = username 
		self.password = password
		raise NotImplementedError

	def do_request(self, request_type, post_values):
		"""performs named request on smsconcuba, returning result"""
		#=====[ Step 1: fill out params	]=====
		url = self.api_url + request_type
		post_values['username'] = self.username
		post_values['password'] = self.password

		#=====[ Step 3: perform request	]=====
		r = requests.post(url, params=post_values)
		return r


	def send_message(self, from_number, to_number, message):
		"""send sms via specified numbers"""
		#=====[ Step 2: construct/send request	]=====s
		post_values = {
						'from_number':from_number,
						'delivery_number':to_number,
						'message':message
					}
		r = self.do_request('send_message', post_values)
		return r

