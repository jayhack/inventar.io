import webapp2
from messaging import EmailClient
from storage import DBClient
from messaging.mandrill_utils import flask_request_to_email

class EmailAppBase(webapp2.RequestHandler):
	"""
	Class: EmailAppBase
	==================
	Base class for apps that communicate with users via mail; send mail via 
	self.mail_client, store content via self.db_client
	"""

	def __init__(self, request=None, response=None):
		self.initialize(request, response)
		self.email_client = EmailClient()
		self.db_client = DBClient()

	def post(self):
		"""deals with post requests"""
		email = flask_request_to_email(self.request)
		if not email is None:
			self.process(email)
		self.response.write('')

	def process(self):
		"""override"""
		raise NotImplementedError