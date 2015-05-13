"""
Module: server
==============

Contains main flask application
"""
from flask import Flask
from flask import request
from inventario import Inventario

#=====[ Step 1: setup	]=====
app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, world! Welcome to inventar.io'

@app.route('/quiero', methods=['POST'])
def quiero():
	msg = request.json['msg']
	from_email = msg['from_email']
	subject = msg['subject']
	print 'RECEIVED quiero: %s | %s' % (from_email, subject)


@app.route('/tengo', methods=['POST'])
def tengo():
	msg = request.json['msg']
	from_email = msg['from_email']
	subject = msg['subject']
	print 'RECEIVED tengo: %s | %s' % (from_email, subject)


if __name__ == '__main__':
	app.run()