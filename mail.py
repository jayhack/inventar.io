"""
Module: mail
============

Contains classes IvioMail, containing info on single emails, and 
IvioMailClient, providing access to email infrastructure
"""
import json
import mandrill
from secrets import MANDRILL_API_KEY

class IvioMail(object):

	def __init__(self, sender, subject, body, date):
		self.user = sender
		self.subject = subject
		self.body = body
		self.date = date


class IvioMailClient(object):

	def __init__(self):
		self.man_client = mandrill.Mandrill(MANDRILL_API_KEY)

	################################################################################
	####################[ GETTING EMAIL  ]##########################################
	################################################################################

	@classmethod
	def request_to_mail(self, request):
		"""flask.Request -> Mail"""
		#=====[ Step 1: Filter for mandrill	]=====
		if not 'mandrill_events' in request.form:
			return None
		elif len(request.form['mandrill_events']) == 0:
			return None

		#=====[ Step 2: extract content	]=====
		d = json.loads(request.form['mandrill_events'])[0]
		msg = d['msg']
		return IvioMail(msg['from_email'], msg['subject'], msg['text'], str(d['ts']))


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

