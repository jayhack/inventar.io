import uuid
import porc
from secrets import ORCHESTRATE_API_KEY

class DBClient(object):
	"""
	Class: DBClient
	===============
	Manages access to Orchestrate DB

	Usage:
	------
	In [1]: client = DBClient()
	In [2]: client.put('my_collection', {'new':'item'})
	In [3]: items = client.list('my_collection')
	In [4]: item = client.find('my_collection', my_key)
	"""

	def __init__(self):
		self.orc_client = porc.Client(ORCHESTRATE_API_KEY, async=False)

	def put(self, collection, item):
		"""puts list of items in specified collection on orchestrate"""
		item['unique_id'] = str(uuid.uuid4())
		self.orc_client.put(collection, item['unique_id'], item)
		return item['unique_id']

	def update(self, collection, key, item):
		"""updates a particular item in specified collection on orchestrate"""
		self.orc_client.put(collection, key, item)

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

	def find(self, collection, key):
		"""searches 'collection' for specific item with given key"""
		page = self.orc_client.search(collection, key)
		return self.page_to_item(page.next())

