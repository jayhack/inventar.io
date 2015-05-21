from ..app_base import EmailAppBase
import wikipedia

class App(EmailAppBase):
	"""
	App: Wiki
	=========
	Returns Wikipedia summary of concept named in subject line
	"""

	#=====[ Metadata	]=====
	dependencies = ['wikipedia']
	from_email = 'wiki@ivioapp.com'

	def get_summary(self, email):
		"""returns formatted summary"""
		#=====[ Step 1: get summary	]=====
		try:
			summary = wikipedia.summary(email.subject.strip())
		except:
			summary = 'Disambiguation Error. Try English!'

		#=====[ Step 2: format	]=====
		return """
Wikipedia Summary:
==================

%s
---

%s
""" % (mail.subject.strip(), summary)



	def process(self, email):
		#=====[ Step 1: get body	]=====
		body = self.get_summary(email)

		#=====[ Step 2: send results	]=====
		self.email_client.send_message(
										self.from_email, 
										email.user, 
										'Wikipedia Resultados', 
										summary
										)
