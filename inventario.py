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

	mandrill_key = 'lpCk0T9_xDl5XMWS0CZ9iA'
	orchestrate_key = '073ea3b8-7425-43f3-a603-450967822c6a'
	quieros_collection = 'quiero_submissions'
	tengos_collection = 'tengo_submissions'

	def __init__(self):
		"""connnects to Orchestrate"""
		self.man_client = mandrill.Mandrill(self.mandrill_key)
		self.orc_client = porc.Client(self.orchestrate_key, async=False)

	def put(self, items, collection):
		for item in items:
			self.orc_client.put(collection, str(uuid.uuid4()), item)

	def put_quieros(self, items):
		return self.put(items, self.quieros_collection)

	def put_tengos(self, items):
		return self.put(items, self.tengos_collection)

	def page_to_item(self, page):
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

	def handle_quiero_sub(self, quiero_sub):
		"""finds relevant tengo submissions and mails back"""
		if len(quiero_sub.items) < 1:
			return

		matches = {item['item']:self.find_tengo_subs(item['item']) for item in quiero_sub.items}

		message = {
					'from_email':'resultados@ivioapp.com',
					'to': [{
							'email':quiero_sub.items[0]['sender'],
							'type': 'to'
							}],
					'subject':'resultados',
					'text':pprint.pformat(matches),
				}
		result = self.man_client.messages.send(	message=message, 
												async=False, 
												ip_pool='Main Pool')
		return result




