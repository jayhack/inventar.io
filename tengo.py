"""
Module: tengo
=============

contains class TengoSub, representing submission about an item the sender
has on hand

Fields:
-------
- sender: sender's email
- item: name of requested item
- price: asking price of item
- qty: number in stock
- date: time it was sent (GMT)

Format:
-------
subject: ...
body:
	item: [ITEM NAME 1] / [PRICE] / [QTY]
	...
	item: [ITEM NAME N] / [PRICE] / [QTY]
"""
from submission import Submission

class TengoSub(Submission):

	def __init__(self, sender, subject, body, date=None):
		super(TengoSub, self).__init__(sender, subject, body, date)

	@classmethod
	def is_item_line(self, s):
		"""returns true if string s is an item line"""
		return len(s.split('/')) == 3

	@classmethod
	def extract_item_line(self, s):
		"""item line -> item, price, qty"""
		splits = s.split('/')
		item = splits[0].strip().lower()
		price = float(splits[1].strip())
		qty = float(splits[2].strip())
		return item, price, qty

	def parse_body(self):
		"""parses email subject/body to get self.items"""
		self.items = []
		lines = self.body.split('\n')
		for l in lines:
			if self.is_item_line(l):
				item, price, qty = self.extract_item_line(l)
				self.items.append({	
									'sender':self.sender,
									'item':item, 
									'price':price, 
									'qty':qty,
									'date':self.date
								})


