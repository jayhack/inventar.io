"""
Module: inventario
==================

Contains class inventario, which manages all interactions with
the database
"""
import uuid
import porc

class Inventario(object):

	orchestrate_key = '073ea3b8-7425-43f3-a603-450967822c6a'
	quieros = 'quiero_submissions'
	tengos = 'tengo_submissions'

	def __init__(self):
		"""connnects to Orchestrate"""
		self.orc_client = porc.Client(self.orchestrate_key, async=False)

	def insert_quiero(self, quiero_sub):
		"""inserts a quiero_sub into db"""
		for item in quiero_sub.items:
			self.orc_client.put(self.quieros, str(uuid.uuid4()), item)

	def insert_tengo(self, tengo_sub):
		"""inserts tengo sub into db"""
		for item in tengo_sub.items:
			self.orc_client.put(self.tengos, str(uuid.uuid4()), item)

	@classmethod
	def page_to_dict(self, page):
		"""converts orchestrate NoSQL pages to readable dicts"""
		return page['value']

	def find_tengo_subs(self, item):
		"""returns a list of tengos for the given quiero"""
		search = porc.Search().query('value.item:%s' % item)
		pages = self.orc_client.search(self.tengos, search)
		return [self.page_to_dict(p) for p in pages.all()]

	def find_quiero_subs(self, item):
		"""returns a list of quieros matching given tengo"""
		search = porc.Search().query('value.item:%s' % item)
		pages = self.orc_client.search(self.quieros, search)
		return [self.page_to_dict(p) for p in pages.all()]



