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
		go = Goslate()

		#=====[ Step 1: get translation	]=====
		lang = email.subject.strip().lower().capitalize()
		if lang in go.get_languages().values():
			try:
				translation = go.translate(email.body, lang)
			except:
				translation = "Translation error."
		else:
			translation = u'%s no esta soportado intente con es/en/fr' % lang

		#=====[ Step 2: format	]=====
		return """
Traduccion para:
================

%s
---

%s
""" % (email.subject.strip().encode('ascii'), translation.encode('ascii'))



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