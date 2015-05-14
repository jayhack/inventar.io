"""
Module: quiero
==============

contains class QuieroEmail, representing submission asking for an item

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
from submission import Submission
class QuieroEmail(Submission):

	def __init__(self, sender, subject, body, date=None):
		super(QuieroSub, self).__init__(sender, subject, body, date)

	def parse_subject(self):
		pass

	@classmethod
	def extract_item_line(self, s):
		"""item line -> item"""
		return ' '.join(s.strip().lower().split(':')[1:]).strip()

	def parse_body(self):
		"""parses email subject/body to get self.item"""
		self.items = []
		for l in self.body.split('\n'):
			if self.is_item_line(l):
				item = self.extract_item_line(l)
				self.items.append({
									'sender':self.sender,
									'item':item,
									'date':self.date
								})