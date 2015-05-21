from mandrill_client import MandrillClient
from secrets import BULKSMS_PASSWORD

class BulkSMSClient(MandrillClient):
	"""
	Class: BulkSMSClient
	====================
	Client for accessing SMS functionality via BulkSMS

	Usage:
	------
	In [1]: sms_client = BulkSMSClient()
	In [2]: sms_client.send_message(to_number, text)
	"""

	#=====[ Metadata	]=====
	send_email = 'sms@ivioapp.com' 
	send_pwd = BULKSMS_PASSWORD
	limit_chars = 140

	def __init__(self):
		super(MandrillClient, self).__init__()

	def send_message(self, to_number, text):
		"""
		Method: send_message
		--------------------
		Sends an sms from [self.send_email] to to_number 

		Args:
		-----
		- to_number: number to send to
		- text: content of message to send. Limited to self.max_chars
		"""
		#=====[ Step 1: get to_email	]=====
		if not type(to_number) in [str, unicode]:
			to_number = str(to_number)
		to_email = '%s@usa.bulksms.com'

		#=====[ Step 2: send message	]=====
		text = text[:self.limit_chars]
		return self.send(self.send_email, self.to_email, self.send_pwd, text)

