"""
Module: server
==============

Contains main flask application
"""
import json
import pprint
from flask import Flask
from flask import request
from inventario import Inventario
from email_client import EmailClient
from ivio_email import IvioEmail

#=====[ Setup	]=====
app = Flask(__name__)
ivio = Inventario()
email_client = EmailClient()

def catches_email(f, *args, **kwargs):
	"""
	Decorator: catch_email
	----------------------
	sets variable 'email' to an ivio_email
	"""
	def g():
		email = email_client.request_to_email(request)
		return f(email, *args, **kwargs)
	return g

@app.route('/')
def index():
	"""
	Hook: index
	===========
	Returns landing page
	"""
	return """\n
Inventario Landing Page
=======================
Version: 0.1
"""

@app.route('/wiki', methods=['POST'])
@catches_email
def wiki(email):
	"""
	Hook: wiki
	==========
	Returns text of requested wikipedia article
	"""
	print "GOT A WIKIPEDIA REQUEST (not supported yet.)"
	print "email.address"
	return ''

@app.route('/quiero', methods=['POST'])
def quiero():
	"""
	Hook: quiero
	============

	Allows users to post items they *want* to 'quiero' collection
	in database and returns results if there are any
	"""
	#=====[ Step 1: grab email	]=====
	email = email_client.request_to_email(request)

	#=====[ Step 2: insert items into db	]=====
	if len(email.items) < 1:
		return ''
	ivio.put_quieros(email.items)

	#=====[ Step 3: find matches and mail back	]=====
	matches = {x['name']:ivio.find_tengos(x['name']) for x in email.items}
	user = email.items[0]['user']
	subject = 'resultados'
	body = pprint.pformat(matches)
	email_client.send_message(user, subject, body)

	return ''

@app.route('/tengo', methods=['POST'])
def tengo():
	"""Handles 'tengo' submissions"""
	#=====[ Step 1: catch submission	]=====
	email = email_client.request_to_email(request)

	#=====[ Step 2: insert items into db	]=====
	ivio.put_tengos(email.items)
	return ''


if __name__ == '__main__':
	app.run()