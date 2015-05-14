"""
Module: email_client
====================

Contains class EmailClient, which is in charge of getting 
emails and returning responses
"""
import mandrill
from ivio_email import IvioEmail

class EmailClient(object):

	mandrill_key = 'lpCk0T9_xDl5XMWS0CZ9iA'

	def __init__(self):
		self.man_client = mandrill.Mandrill(self.mandrill_key)

	################################################################################
	####################[ GETTING EMAIL  ]##########################################
	################################################################################

	@classmethod
	def request_to_content(self, request):
		"""flask.Request -> sender, subject, body, date"""
		d = json.loads(request.form['mandrill_events'])[0]
		date = str(d['ts'])
		msg = d['msg']
		return msg['from_email'], msg['subject'], msg['text'], date

	@classmethod 
	def request_to_email(self, request):
		"""flask.Request -> IvioEmail"""
		user, subject, body, date = self.request_to_content(request)
		ivio_email = IvioEmail(user, subject, body, date)
		return ivio_email


	################################################################################
	####################[ SENDING EMAIL ]###########################################
	################################################################################

	def send_message(self, to_email, subject, body):
		"""sends message via Mandrill API request"""
		message = {
				'from_email':'resultados@ivioapp.com',
				'to': [{'email':to_email, 'type': 'to'}],
				'subject':subject,
				'text':body,
			}
		result = self.man_client.messages.send(	
												message=message,
												async=False, 
												ip_pool='Main Pool'
												)
		return result

