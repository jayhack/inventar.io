"""
Module: database
================

contains DBClient, which maintains all connection with the 
database

DB format:
----------

Table quiero_submissions:
	id INT
	sender TEXT
	item TEXT
	date TEXT

Table tengo_submissions:
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
	####################[ QUIERO ]##################################################
	################################################################################

	def insert_quiero(self, quiero_sub):
		"""inserts a quiero submission into db"""
		cur = self.conn.cursor()
		for item in quiero_sub.items():
			cur.execute("""INSERT INTO quiero_submissions(sender, item, date) 
							VALUES (?,?,?)""", (item['sender'], item['item'], item['date']))
		self.conn.commit()

	def insert_tengo(self, tengo_sub):
		"""inserts a tengo submission into the db"""
		cur = self.conn.cursor()
		for item in tengo_sub.items():
			cur.execute("""INSERT INTO tengo_submissions(sender, item, qty, price, date) 
							VALUES (?,?,?,?,?)""", 
							(item['sender'], item['item'], item['qty'], item['price'], item['date']))
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



	def get_submissions(self):
		"""iterates over all submissions"""
		cur = self.conn.cursor()
		cur.execute("SELECT * FROM submissions")
		for row in cur.fetchall():
			id, sender, item, date, price = row
			yield Submission(sender, item)

