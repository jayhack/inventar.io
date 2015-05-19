"""
Module: wiki
============

Contains app Wiki, which provides access to Wikipedia summaries
"""

from app_base import AppBase
import wikipedia

class App(AppBase):
	"""
	App: Wiki
	=========
	Returns Wikipedia summary of concept named in subject line
	"""
	#=====[ metadata ]=====
	name = 'wiki'
	hook = '/wiki'

	def __init__(self, db_client, mail_client):
		super(App, self).__init__(db_client, mail_client)

	def process(self, mail):
		summary = wikipedia.summary(mail.subject.strip())
		self.mail_client.send_message(mail.user, 'Wikipedia Resultados', summary)
