"""
Module: yikyak
==============

Contains app YikYak, which provides a wall for users to post to and view an 
anonymous feed
"""
import sys
sys.path.append('../')
from app_base import AppBase

import pprint

class App(AppBase):
	"""
	App: YikYak
	===========

	Allows users to post to and view an anonymous feed
	"""
	#=====[ metadata ]=====
	name = 'wiki'
	hook = '/wiki'
	db_collection = 'yikyak'
	char_limit = 140

	def get_feed(self, mail):
		"""returns current feed as string"""
		return pprint.pformat(self.db_client.list(self.db_collection))

	def process_feed(self, mail):
		"""processes yikyak reads"""
		feed = self.get_feed(mail)
		self.mail_client.send_message(mail.user, 'YikYak Feed', feed)

	def process_post(self, mail):
		"""processes yikyak posts; limit 140 characters"""
		post = mail.subject.strip()[:self.char_limit]
		self.db_client.put(self.db_collection, {'text':post, 'user':mail.user})
		feed = self.get_feed(mail)
		self.mail_client.send_message(mail.user, 'YikYak Feed', feed)

	def process(self, mail):
		if len(mail.subject.strip()) == 0:
			self.process_feed(mail)
		else:
			self.process_post(mail)

