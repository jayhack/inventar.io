"""
Module: wiki
============

Contains app Wiki, which provides access to Wikipedia summaries
"""
import sys
sys.path.append('../')
from app_base import AppBase
import wikipedia

class App(AppBase):
	"""
	App: Wiki
	=========
	Returns Wikipedia summary of concept named in subject line
	"""
	def process(self, mail):
		try:
			summary = wikipedia.summary(mail.subject.strip())
		except:
			summary = 'Disambiguation Error'
		self.mail_client.send_message(mail.user, 'Wikipedia Resultados', summary)
