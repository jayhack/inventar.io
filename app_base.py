"""
Module: app_base
================

Contains base class for apps; developers should subclass this 
in order to make an app that will run live on the server
"""
import webapp2
from mail import MailClient
from dbclient import DBClient

class AppBase(webapp2.RequestHandler):

	def __init__(self, request=None, response=None):
		self.initialize(request, response)
		self.mail_client = MailClient()
		self.db_client = DBClient()

	def post(self):
		"""deals with post requests"""
		mail = self.mail_client.request_to_mail(self.request)
		if not mail is None:
			self.process(self.request)
		self.response.write('')

	def process(self):
		"""override"""
		raise NotImplementedError