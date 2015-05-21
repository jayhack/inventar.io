from app_base import AppBase
from ..messaging import SMSClient
from ..messaging import flask_request_to_sms
from ..storage import DBClient

class SMSAppBase(AppBase):
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

	def extract_msg(self, request):
		return flask_request_to_sms

	def process(self, sms):
		"""override"""
		raise NotImplementedError