import webapp2
from messaging import SMSClient
from storage import DBClient
from messaging.mandrill_utils import flask_request_to_sms

class SMSAppBase(webapp2.RequestHandler):
	"""
	Class: SMSAppBase
	=================
	Base class for apps that communicate with users via mail; send mail via 
	self.mail_client, store content via self.db_client
	"""

	def __init__(self, request=None, response=None):
		self.initialize(request, response)
		self.sms_client = SMSClient()
		self.db_client = DBClient()

	def post(self):
		"""deals with post requests"""
		sms = flask_request_to_sms(self.request)
		if not sms is None:
			self.process(sms)
		self.response.write('')

	def process(self):
		"""override"""
		raise NotImplementedError