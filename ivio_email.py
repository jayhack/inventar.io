"""
Module: ivio_email
==================

Contains abstract class IvioEmail, which implements abstract parsing
the contents away and just fills self.items
"""
import re
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
		self.items = [self.get_item(l, user, address, date) for l in item_lines]

	def extract_address(self, body):
		matches = re.findall(r'@(.*)[$#*\n]', body)
		if len(matches) == 0:
			return None
		return matches[0]

	def get_item_lines(self, body):
		return filter(lambda l: l.strip().startswith('*'), body.split('\n'))

	def extract_sym(self, line, sym, symtype):
		matches = re.findall('%s(.*?)(\$|\#|\*|$)' % sym, line)
		if len(matches) > 0:
			return symtype(matches[0][0].strip())
		return None

	def get_item(self, line, user, address, date):
		return {
				'user':user,
				'name':self.extract_sym(line, '\*', str),
				'price':self.extract_sym(line, '\$', float),
				'qty':self.extract_sym(line, '\#', int),
				'address':address,
				'date':date
				}

	def __str__(self):
		return '=====[IvioEmail]=====\n%s' % pprint.pformat(self.items)



