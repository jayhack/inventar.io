from app_base import AppBase
from ..messaging import EmailClient
from ..messaging import flask_request_to_email
from ..storage import DBClient

class EmailAppBase(AppBase):
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

	def extract_msg(self, request):
		return flask_request_to_email(request)

	def process(self, email):
		"""override"""
		raise NotImplementedError