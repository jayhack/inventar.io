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


"""
Module: yikyak
=================

Contains abstract class YikYakEmail

"""
import re
import pprint
from datetime import datetime
from mail import IvioMail

class YikYakEmail(object):

	def __init__(self, mail):
		"""
		Args:
		-----
		- mail: IvioMail object
		"""

		self.votes = self.get_vote_lines(mail.body)
		self.post = self.extract_post(mail)
		# address = self.extract_address(mail.body)
		# item_lines = self.get_item_lines(mail.body)
		# self.items = [self.get_item(l, mail.user, address, mail.date) for l in item_lines]

	def extract_post(self, mail):
		matches = re.findall(r'--.*--', mail.body)
		if len(matches) == 0:
			return None
		return {
				'post':matches[0],
				'user':mail.user,
				'date':mail.date,
				'votes':0
				}

	def get_vote_lines(self, body):
		return filter(lambda l: l.strip().startswith('@'), body.split('\n'))

	def __str__(self):
		return '=====[IvioEmail]=====\n%s' % pprint.pformat(self.items)


