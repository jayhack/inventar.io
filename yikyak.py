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
		self.post = self.extract_post(mail.body)
		# address = self.extract_address(mail.body)
		# item_lines = self.get_item_lines(mail.body)
		# self.items = [self.get_item(l, mail.user, address, mail.date) for l in item_lines]

	def extract_post(self, body):
		matches = re.findall(r'--.*--', body)
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



