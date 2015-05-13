"""
Module: submission
==================

Contains abstract class Submission
Inheritors should implement parse_subject and parse_body
"""
from datetime import datetime
class Submission(object):

	def __init__(self, sender, subject, body, date=None):
		"""
		Args:
		-----
		- sender: email of submitter
		- subject: subject of submitted message
		- body: body of submitted message
		- date: date message was submitted on 
		"""
		#=====[ Step 1: set all	]=====
		self.sender = sender
		self.subject = subject 
		self.body = body
		self.date = date
		if self.date is None:
			self.date = self.get_date()
		self.items = []

		#=====[ Step 2: parse ]=====
		self.parse_subject()
		self.parse_body()

	def __str__(self):
		print '=====[ %s: %s ]=====' % (str(self.__class__), self.date)
		print 'sender: %s' % self.sender
		print 'items: '
		for item in self.items:
			print item
		print


	@classmethod
	def get_date(self):
		"""returns current date as a string"""
		return str(datetime.now())

	def parse_subject(self):
		"""parses email subject line"""
		raise NotImplementedError

	def parse_body(self):
		"""parses email body"""
		raise NotImplementedError


