"""
Module: server
==============

Contains main flask application
"""
import json
from flask import Flask
from flask import request
from quiero import QuieroSub
from tengo import TengoSub
app = Flask(__name__)

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
	sender, subject, body, date = request_to_content(request)
	quiero_sub = QuieroSub(sender, subject, body, date)
	print 'RECEIVED quiero: %s | %s | %s' % (sender, subject, date)
	return ''

@app.route('/tengo', methods=['POST'])
def tengo():
	"""Handles 'tengo' submissions"""
	sender, subject, body, date = request_to_content(request)
	tengo_sub = TengoSub(sender, subject, body, date)
	print 'RECEIVED tengo: %s | %s | %s' % (sender, subject, date)
	return ''


if __name__ == '__main__':
	app.run()