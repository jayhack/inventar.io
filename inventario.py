"""
Module: inventario
==================

Contains class inventario, which manages all interactions with
the database
"""
import uuid
import pprint
import mandrill
import porc

class Inventario(object):

	orchestrate_key = '073ea3b8-7425-43f3-a603-450967822c6a'

	def __init__(self):
		"""connnects to Orchestrate"""
		self.orc_client = porc.Client(self.orchestrate_key, async=False)

	def put(self, items, collection):
		"""puts specified item in specified collection on orchestrate"""
		for item in items:
			self.orc_client.put(collection, str(uuid.uuid4()), item)

	def put_quieros(self, items):
		return self.put(items, 'quero')

	def put_tengos(self, items):
		return self.put(items, 'tengo')

	def page_to_item(self, page):
		return page['value']

	def find_matching_items(self, name, collection):
		"""finds items in orchestrate collection 'collection' of name 'name'"""
		search = porc.Search().query('value.name:%s' % name)
		pages = self.orc_client.search(collection, search)
		items = [self.page_to_item(p) for p in pages.all()]
		return items

	def find_tengos(self, name):
		return self.find_matching_items(name, 'tengo')

	def find_quieros(self, name):
		return self.find_matching_items(name, 'quiero')



