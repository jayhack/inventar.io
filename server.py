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

@app.route('/')
def index():
	return 'Hello, world! Welcome to inventar.io'

@app.route('/wiki', methods=['POST'])
def wiki():
	"""returns wikipedia article"""
	print "GOT A WIKIPEDIA REQUEST"
	return ''

@app.route('/quiero', methods=['POST'])
def quiero():
	"""Handles 'quiero' submissions"""
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