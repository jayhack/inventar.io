"""
Module: app_base
================

Contains base class for apps; developers should subclass this 
in order to make an app that will run live on the server
"""
class AppBase(object):

	def __init__(self, db_client, mail_client):
		self.db_client = db_client
		self.mail_client = mail_client

	def process_mail(self, mail):
		raise NotImplementedError