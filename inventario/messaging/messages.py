"""
Module: messages
================
Defines classes Email and SMS
"""

class Email(object):
	"""
	Class: Email
	============
	Represents a single email
	"""
	def __init__(self, sender, subject, body, date):
		self.user = sender
		self.subject = subject
		self.body = body
		self.date = date


class SMS(object):
	"""
	Class: SMS
	==========
	Represents a single sms message
	"""
	def __init__(self, sender, text, date):
		self.user = sender
		self.text = text
		self.date = date
