"""
Module: quiero
==============

contains class QuieroSub, representing submission asking for an item

Fields:
-------
- sender: sender's email
- item: name of requested item
- date: time it was sent (GMT)

Format:
-------
subject: 
body:
	[ITEM NAME 1]
	...
	[ITEM NAME N]
"""
from submission import Submission
class QuieroSub(Submission):

	def __init__(self, sender, subject, body, date=None):
		super(QuieroSub, self).__init__(sender, subject, body, date)

	def parse_subject(self):
		pass

	@classmethod
	def is_item_line(self, s):
		"""returns true if string s is an item line"""
		return True

	@classmethod
	def extract_item_line(self, s):
		"""item line -> item"""
		return s.strip()

	def parse_body(self):
		"""parses email subject/body to get self.item"""
		self.items = []
		for l in self.body.split('\n'):
			if self.is_item_line(s):
				item = self.extract_item_line(s)
				items.append({'item':item})