"""
Module: inventory
=================

Contains abstract class InventoryEmail, which parses IvioMail to get contents
of inventory request
"""
import re
import pprint
from datetime import datetime
from mail import IvioMail

class InventoryEmail(object):

	def __init__(self, mail):
		"""
		Args:
		-----
		- mail: IvioMail object
		"""
		address = self.extract_address(mail.body)
		item_lines = self.get_item_lines(mail.body)
		self.items = [self.get_item(l, mail.user, address, mail.date) for l in item_lines]

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



