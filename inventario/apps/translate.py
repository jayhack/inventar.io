# -*- coding: utf-8 -*-
from ..app_base import EmailAppBase
from goslate import Goslate

class App(EmailAppBase):
	"""
	App: Translate
	=========
	Returns translation for the body of the message on the language specified in subject
	"""

	#=====[ Metadata	]=====
	dependencies = ['goslate']
	from_email = 'translate@ivioapp.com'

	def get_translation(self, email):
		"""returns translation"""
		#=====[ Step 1: get translation	]=====
		translation = ""
		try:
			lang = email.subject.strip()
			if lang in Goslate().get_languages():
				go = Goslate()
				translation = go.translate(email.body,lang)
			else:
				translation = lang + u' no está soportado intente con es/en/fr'
		except:
			translation = u'Error durante la traducción!'

		#=====[ Step 2: format	]=====
		return u"""
Traducción para:
==================

%s
---

%s
""" % (unicode(email.subject.strip()), unicode(translation))



	def process(self, email):
		#=====[ Step 1: get body	]=====
		body = self.get_translation(email)

		#=====[ Step 2: send results	]=====
		self.email_client.send_message(
										self.from_email, 
										email.user, 
										'Resultados Traductor', 
										body
										)