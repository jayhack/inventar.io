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

	def insert_quiero(self, quiero_sub):
		"""inserts a quiero_sub into db"""
		self.db_client.insert_quiero(quiero_sub)

	def insert_tengo(self, tengo_sub):
		"""inserts tengo sub"""
		self.db_client.insert_tengo(tengo_sub)

	def get_requests(self):
		"""returns a list of all requests"""
		return self.db_client.get_requests()

	def get_submissions(self):
		"""returns a list of all submissions"""
		return self.db_client.get_submissions()

