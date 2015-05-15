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
		"""puts list of items in specified collection on orchestrate"""
		for item in items:
			item['unique_id'] = str(uuid.uuid4())
			self.orc_client.put(collection, itme['unique_id'], item) 

	def page_to_item(self, page):
		"""converts NoSQL pages to the items that were inserted"""
		return page['value']

	def search(self, collection, key, value):
		"""searches 'collection' for items with specified key/value pair"""
		search = porc.Search().query('value.%s:%s' % (key, value))
		pages = self.orc_client.search(collection, search)
		return [self.page_to_item(p) for p in pages.all()]

	def list(self, collection):
		"""returns all items in the collection"""
		pages = self.orc_client.list(collection)
		return [self.page_to_item(p) for p in pages.all()]

