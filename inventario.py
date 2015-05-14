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

	def __init__(self, dbname):
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

