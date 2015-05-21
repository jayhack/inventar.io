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

	def process(self, email):
		#=====[ Step 1: get summary	]=====
		try:
			summary = wikipedia.summary(mail.subject.strip())
		except:
			summary = 'Disambiguation Error'

		#=====[ Step 2: send results	]=====
		self.email_client.send_message(
										self.from_email, 
										email.user, 
										'Wikipedia Resultados', 
										summary
										)
