"""
Test: test_ivio_email
=====================
tests class ivio_email for its parsing capabilities
"""
import unittest
import nose
import datetime
import sys
from ivio_email import IvioEmail

class Test_IvioEmail(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_tengo(self):

		user = 'jhack@stanford.edu'
		subject = '<no subject>'
		body = """
		@2019 day st.

		*glasses $10 #5 *comment
		*shirt # 2 $ 5
		*socks #1 $2
		---
		Jay Hack
		CS 2015
		jhack@stanford.edu
		----
		"""
		date = str(datetime.datetime.now())

		ivio_email = IvioEmail(user, subject, body, date)

		#=====[ Step 1: global checks	]=====
		self.assertEqual(len(ivio_email.items), 3)
		for item in ivio_email.items:
			self.assertEqual(item['address'], '2019 day st.')
			self.assertEqual(item['user'], 'jhack@stanford.edu')

		#=====[ Step 2: itemwise checks	]=====
		item0 = ivio_email.items[0]
		self.assertEqual(item0['name'], 'glasses')
		self.assertEqual(item0['price'], 10.0)
		self.assertEqual(item0['qty'], 5)

		item1 = ivio_email.items[1]
		self.assertEqual(item1['name'], 'shirt')
		self.assertEqual(item1['price'], 5.0)
		self.assertEqual(item1['qty'], 2)

		item2 = ivio_email.items[2]
		self.assertEqual(item2['name'], 'socks')
		self.assertEqual(item2['price'], 2.0)
		self.assertEqual(item2['qty'], 1)


	def test_quiero(self):
		user = "jhack@stanford.edu"
		subject = "<no subject>"
		body ="""
		*shirt
		---
		Jay Hack
		CS 2015
		jhack@stanford.edu
		----
		"""
		date = str(datetime.datetime.now())
		ivio_email = IvioEmail(user, subject, body, date)

		self.assertEqual(len(ivio_email.items), 1)
		item = ivio_email.items[0]
		self.assertEqual(item['name'], 'shirt')
		self.assertEqual(item['user'], 'jhack@stanford.edu')
		# self.assertTrue(not 'address' in item)









