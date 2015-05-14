"""
Module: quiero
==============

contains class QuieroEmail, representing submission asking for an item.
Construction fills out self.items, which are formatted as follows:

	{
		'name':<name of sought item>,
		'user':<user's email>
	}

Fields:
-------
- sender: sender's email
- item: name of requested item
- date: time it was sent (GMT)

Format:
-------
subject: 
body:
	*[ITEM NAME] $[PRICE] #[QUANTITY]
	...
	*[ITEM NAME] $[PRICE] #[QUANTITY]
"""
import re
from submission import Submission

class QuieroEmail(Submission):

	def __init__(self, user, subject, body, date=None):
		super(QuieroSub, self).__init__(user, subject, body, date)

	def extract_address(self, body):
		matches = re.findall(r'@(.*)[$#*\n]', body)
		if len(matches) == 0:
			return None
		return matches[0]

	def get_item_lines(self, body):
		return filter(lambda l: l.startswith('*'), body.split('\n'))

	def make_extractor(self, sym):
		match_str = '%s(.*?)(\$|\#|\*|$)' % sym
		return lambda x: re.findall(match_str, x)[0][0]
	extract_name = self.make_extractor('\*')
	extract_price = self.make_extractor('\$')
	extract_qty = self.make_extractor('\#')

	def extract_item(l, ser):
		return 	{
					'user':self.user,
					'name':self.extract_name(l),
				}

	def parse(self, body):
		"""body -> list of items"""
		address = self.extract_address(body)
		item_lines = self.get_item_lines(body)
		items = [self.extract_item(l, address) for l in item_lines]
		return items



