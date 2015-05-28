from ..app_base import EmailAppBase
import google
import BeautifulSoup
import urllib2

class App(EmailAppBase):
	"""
	App: Google
	=========
	Returns first 10 google results for the subject
	"""

	#=====[ Metadata	]=====
	dependencies = ['google','BeautifulSoup','urllib2']
	from_email = 'google@ivioapp.com'

	def get_search(self, email):
		"""returns formatted search"""
		#=====[ Step 1: get search results	]=====
		try:
			search = ""
			c = 0
			for url in google.search(email.subject.strip(),lang='es'):
				if c == 10:
					break
				c+=1
				try:
					data = urllib2.urlopen(url).read()
					search += BeautifulSoup.BeautifulSoup(data).html.head.title.contents
				except:
					search += 'No se puede obtener titulo para esta direccion'
					pass
				search += url + "\n"

		except:
			search = 'Error buscando '+email.subject.strip()

		#=====[ Step 2: format	]=====
		return '''
Resultados de Google:
==================

%s
---

%s
''' % (email.subject.strip(), search)



	def process(self, email):
		#=====[ Step 1: get body	]=====
		body = self.get_search(email)

		#=====[ Step 2: send results	]=====
		self.email_client.send_message(
										self.from_email, 
										email.user, 
										'Google Resultados', 
										body
										)
