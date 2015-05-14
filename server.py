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
from ivio_email import IvioEmail

#=====[ Setup	]=====
app = Flask(__name__)
inventario = Inventario()

@app.route('/')
def index():
	return 'Hello, world! Welcome to inventar.io'

def request_to_content(r):
	"""flask.Request -> sender, subject, body, date"""
	d = json.loads(r.form['mandrill_events'])[0]
	date = str(d['ts'])
	msg = d['msg']
	return msg['from_email'], msg['subject'], msg['text'], date

@app.route('/quiero', methods=['POST'])
def quiero():
	"""Handles 'quiero' submissions"""
	#=====[ Step 1: grab email	]=====
	user, subject, body, date = request_to_content(request)
	email = IvioEmail(user, subject, body, date)
	print '\n(Quiero)'
	print email

	#=====[ Step 2: insert each item into db	]=====
	inventario.insert_quieros(email.items)
	return ''

@app.route('/tengo', methods=['POST'])
def tengo():
	"""Handles 'tengo' submissions"""
	#=====[ Step 1: catch submission	]=====
	user, subject, body, date = request_to_content(request)
	email = IvioEmail(user, subject, body, date)
	print '\n(Tengo)'
	print email

	#=====[ Step 2: insert into db	]=====
	inventario.insert_tengos(email.items)
	return ''


if __name__ == '__main__':
	app.run()