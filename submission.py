"""
Module: submission
==================

Contains class Submission, which contains all details on emails submitting
items.
"""
class Submission(object):

	def __init__(self, sender, item_name):
		"""creates from an email"""
		self.sender = sender
		self.item_name = item_name

	@classmethod
	def get_item_name(self, email):
		"""returns name of requested item"""
		return email.subject.split(':')[1].lower().strip()

	@classmethod
	def get_sender(self, email):
		"""returns name of sender of request"""
		return email.sender

	@classmethod
	def from_email(cls, email):
		"""creates from a GmailEmail object"""
		sender = cls.get_sender(email)
		item_name = cls.get_item_name(email)
		return cls(sender, item_name)