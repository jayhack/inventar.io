"""
Module: mail
============

Contains classes Mail, containing info on single emails, and 
MailClient, providing access to email infrastructure
"""
import json
import mandrill
from secrets import MANDRILL_API_KEY

class Mail(object):

	def __init__(self, sender, subject, body, date):
		self.user = sender
		self.subject = subject
		self.body = body
		self.date = date


class MailClient(object):

	def __init__(self):
		self.man_client = mandrill.Mandrill(MANDRILL_API_KEY)

	################################################################################
	####################[ GETTING EMAIL  ]##########################################
	################################################################################

	@classmethod
	def request_to_mail(self, request):
		"""flask.Request -> Mail"""
		#=====[ Step 1: Filter for mandrill	]=====
		print '=====[ HERE ]====='
		print request.get('mandrill_events')
		print type(request.get('mandrill_events'))
		print '=====[ END HERE ]===='

		#=====[ Step 2: extract content	]=====
		if type (request.get('mandrill_events')) in [str, unicode]:
			j = json.loads(request.get('mandrill_events'))
		else:
			j = request.get('mandrill_events')

		if len(j) == 0:
			return None
		d = j[0]
		msg = d['msg']
		return Mail(msg['from_email'], msg['subject'], msg['text'], str(d['ts']))


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

