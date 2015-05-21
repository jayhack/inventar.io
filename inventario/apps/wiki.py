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

	def process(self, email):
		try:
			summary = wikipedia.summary(mail.subject.strip())
		except:
			summary = 'Disambiguation Error'
		self.email_client.send_message(email.user, 'Wikipedia Resultados', summary)
