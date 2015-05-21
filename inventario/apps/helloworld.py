from ..app_base import EmailAppBase

class App(EmailAppBase):
	"""
	App: HelloWorld
	===============
	Hello world tutorial app
	"""

	#=====[ Metadata	]=====
	# dependencies: this is a list of strings of your dependencies, as you
	#               would import them in python. for example, the wiki app 
	# 				has ['wikipedia'] since it needs to 'import wikipedia'. 
	dependencies = []

	def process(self, email):
		"""
		Method: process
		===============

		'email' is of type inventario.messaging.Email, containing the
		following fields:

			email.user 		#email of sender
			email.subject 	#subject line 
			email.body 		#email body
			email.date 		#timestamp it was sent at

		You have the following class members at your disposal:

			- self.email_client: inventario.messaging.EmailClient, allows
			                     you to send messages
			- self.db_client: inventario.storage.DBClient, allows you to 
			                  store and retrieve data from a NoSQL database

		Check out the example usage below!
		"""
		#=====[ Step 1: store email's subject line in DB	]=====
		# self.db_client.put(my_collection, my_dict) will place the python dict
		# 'my_dict' into the NoSQL collection 'my_collection' and return it's
		# unique id in the database. Let's put the received email's subject
		# line in the database.
		db_collection = 'helloworld'
		item = {'subject':email.subject}
		item_id = self.db_client.put(db_collection, item)

		#=====[ Step 2: retrieve our item	]=====
		# self.db_client.find(collection, id) allows you to retrieve an item
		# by its id. self.db_client.list(collection) will return all items in
		# the named collection as a list. Let's grab our most recent item back.
		retrieved_item = self.db_client.find(db_collection, item_id)

		#=====[ Step 3: send back an email	]=====
		# We can send emails back using self.email_client.send_message, which 
		# takes arguments in the following order: 
		# 	from_email (@ivioapp.com), to_email, subject, body
		# Let's send the user back their subject line in the email's body.
		from_email = 'helloworld@ivioapp.com'
		to_email = email.user
		subject = 'Hello, world!'
		body = 'Your previous email subject: %s' % retrieved_item['subject']
		self.email_client.send_message(from_email, to_email, subject, body)
