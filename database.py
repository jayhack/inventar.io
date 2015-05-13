"""
Module: database
================

contains DBClient, which maintains all connection with the 
database

DB format:

Table requests:
	id INT
	sender TEXT
	item TEXT
	date TEXT

Table submissions:
	id INT
	sender TEXT
	item TEXT
	date TEXT
	price FLOAT
"""
import sqlite3
import datetime
from request import Request
from submission import Submission

class DBClient(object):

	def __init__(self, dbname):
		"""connects to the database"""
		self.conn = sqlite3.connect(dbname)	

	################################################################################
	####################[ REQUESTS ]################################################
	################################################################################

	def insert_request(self, request):
		"""inserts a request into the DB"""
		cur = self.conn.cursor()
		cur.execute("INSERT INTO requests(sender, item) VALUES (?,?)", (request.sender, request.item_name))
		self.conn.commit()

	def get_requests(self):
		"""iterates over all requests"""
		cur = self.conn.cursor()
		cur.execute("SELECT * FROM requests")
		for row in cur.fetchall():
			id, sender, item, date = row
			yield Request(sender, item)


	################################################################################
	####################[ SUBMISSIONS ]#############################################
	################################################################################

	def insert_submission(self, submission):
		"""inserts a submission into the DB"""
		cur = self.conn.cursor()
		cur.execute("INSERT INTO submissions(sender, item) VALUES (?,?)", (submission.sender, submission.item_name))
		self.conn.commit()

	def get_submissions(self):
		"""iterates over all submissions"""
		cur = self.conn.cursor()
		cur.execute("SELECT * FROM submissions")
		for row in cur.fetchall():
			id, sender, item, date, price = row
			yield Submission(sender, item)

