"""
Module: dbclient
================

Contains class DBClient, which manages access to storage
"""
import uuid
import pprint
import mandrill
import porc
from secrets import ORCHESTRATE_API_KEY

class DBClient(object):

	def __init__(self):
		self.orc_client = porc.Client(ORCHESTRATE_API_KEY, async=False)

	def put(self, collection, items):
		"""puts specified item in specified collection on orchestrate"""
		for item in items:
			self.orc_client.put(collection, str(uuid.uuid4()), item)

	def search(self, collection, key, value):
		"""searches 'collection' for items with specified key/value pair"""
		search = porc.Search().query('value.%s:%s' % (key, value))
		pages = self.orc_client.search(collection, search)
		return [p['value'] for p in pages.all()]


