"""
Module: inventario
==================

Contains class inventario, which manages all interactions with
the database
"""
from gmail import GmailClient
from request import Request
from submission import Submission
from database import DBClient

class Inventario(object):

	def __init__(self, gmail_username, gmail_password, dbname):
		"""connnects go Gmail, Sqlite"""
		self.gmail_client = GmailClient(gmail_username, gmail_password)
		self.db_client = DBClient(dbname)

	def is_request(self, email):
		"""returns true if the email is a request"""
		return email.subject.lower().startswith('request')

	def is_submission(self, email):
		"""returns True if email contains a submission"""
		return email.subject.lower().startswith('submission')

	def update(self):
		"""updates requests and submissions"""
		for email in self.gmail_client.iter_emails():

			if self.is_request(email):
				request = Request.from_email(email)
				self.db_client.insert_request(request)

			elif self.is_submission(email):
				submission = Submission.from_email(email)
				self.db_client.insert_submission(submission)


	def service_request(self, request):
		"""services passed request"""
		item_name = request.item_name
		


	def get_requests(self):
		"""returns a list of all requests"""
		return self.db_client.get_requests()

	def get_submissions(self):
		"""returns a list of all submissions"""
		return self.db_client.get_submissions()

