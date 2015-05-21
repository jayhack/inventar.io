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
		self.db_client.put(db_collection, item)

		#=====[ Step 2: retrieve our item	]=====
		# self.db_client.search(collection, key, value) allows you to retrieve
		# all items from the database where key == value. Let's grab the same 
		# email back by subject
		matches = self.db_client.search(db_collection, 'subject', email.subject)
		retrieved = matches[-1] #grab the most recent one.

		#=====[ Step 3: send back an email	]=====
		# We can send emails back using self.email_client.send_message, which 
		# takes arguments in the following order: 
		# 	from_email (@ivioapp.com), to_email, subject, body
		# Let's send the user back their subject line in the email's body.
		from_email = 'helloworld@ivioapp.com'
		to_email = email.user
		subject = 'Hello, world!'
		body = 'Your previous email subject: %s' % retrieved['subject']
		self.email_client.send_message(from_email, to_email, subject, body)

		#=====[ Step 4: deployment	]=====
		# That's basically it! Now, next time the project is deployed, this app
		# will be deployed at www.ivioapp.com/helloworld (taken from the
		# filename) and it will start to receive emails from
		# helloworld@ivioapp.com. Try it out! (It is currently deployed)

		#=====[ Step 5: make your own	]=====
		# Using the ingredients listed here, make your own valuable service for 
		# those without affordable access to the internet at large. Check out 
		# our 'App Wish List' on github to get some ideas, or come up with your
		# own! Once you have finished, make a pull request or email me at 
		# jhack@stanford.edu and, pending it won't take the entire server down,
		# I'll make sure it gets deployed. Good luck!!