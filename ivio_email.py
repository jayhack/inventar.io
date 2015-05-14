"""
Module: submission
==================

Contains abstract class IvioEmail, which implements abstract parsing
the contents away and just fills self.items
"""
import pprint
from datetime import datetime

class IvioEmail(object):

	def __init__(self, user, subject, body, date):
		"""
		Args:
		-----
		- user: email address of sender
		- subject: subject of email
		- body: body (text) of email
		- date: date of email
		"""
		address = self.extract_address(body)
		item_lines = self.get_item_lines(body)
		self.items = [self.get_item(l, user, address) for l in item_lines]

	def extract_address(body):
		matches = re.findall(r'@(.*)[$#*\n]', body)
		if len(matches) == 0:
			return None
		return matches[0]

	def get_item_lines(body):
		return filter(lambda l: l.startswith('*'), body.split('\n'))

	def extract_sym(self, line, sym):
		matches = re.findall('%s(.*?)(\$|\#|\*|$)' % sym, line)
		if len(matches) > 0:
			return matches[0][0]
		return None

	def get_item(self, line, user, address):
		return {
				'user':user,
				'name':self.extract_sym(line, '\*'),
				'price':self.extract_sym(line, '\$'),
				'qty':self.extract_sym(line, '\#'),
				'address':address,
				'date':date
				}

	def __str__(self):
		return '=====[IvioEmail]=====\n%s' % pprint.pformat(self.items)



