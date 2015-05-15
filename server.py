"""
Module: server
==============

Contains main flask application
"""
import os
import json
import pprint
from flask import Flask
from flask import request
from flask import send_from_directory
from inventario import Inventario
from email_client import EmailClient
from ivio_email import IvioEmail

#=====[ Setup	]=====
base_dir = os.path.split(os.path.realpath(__file__))[0]
static_dir = os.path.join(base_dir, 'static')
assets_dir = os.path.join(static_dir, 'assets')
app = Flask(__name__, static_folder=assets_dir)
ivio = Inventario()
email_client = EmailClient()

@app.route('/')
def index():
	"""
	Hook: index
	===========
	Returns landing page
	"""
	return send_from_directory(static_dir, 'index.html')

@app.route('/wiki', methods=['POST'])
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
	app.run(debug=True)