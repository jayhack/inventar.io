"""
Module: server
==============

Contains main flask application
"""
from flask import Flask
from flask import request
from inventario import Inventario
import json

#=====[ Step 1: setup	]=====
app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, world! Welcome to inventar.io'

def get_msg(request):
	"""flask.Request -> Mandrill message"""
	return json.loads(request.form['mandrill_events'])[0]['msg']

@app.route('/quiero', methods=['POST'])
def quiero():
	msg = get_msg(request)
	from_email = msg['from_email']
	subject = msg['subject']
	print 'RECEIVED quiero: %s | %s' % (from_email, subject)
	return ''


@app.route('/tengo', methods=['POST'])
def tengo():
	msg = get_msg(request)
	from_email = msg['from_email']
	subject = msg['subject']
	print 'RECEIVED tengo: %s | %s' % (from_email, subject)
	return ''


if __name__ == '__main__':
	app.run()