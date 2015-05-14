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
from quiero import QuieroSub
from tengo import TengoSub

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
	#=====[ Step 1: catch submission	]=====
	sender, subject, body, date = request_to_content(request)
	quiero_sub = QuieroSub(sender, subject, body, date)
	print 'RECEIVED quiero: %s | %s | %s' % (sender, subject, date)
	print quiero_sub

	#=====[ Step 2: insert into db	]=====
	inventario.insert_quiero(quiero_sub)

	#=====[ Step 3: get relevant submissions	]=====
	for item in quiero_sub.items:
		tengo_subs = inventario.find_tengo_subs(item['item'])

		#=====[ Step 4: print them out	]=====
		print '=====[ RELEVANT TENGOS ]====='
		for t in tengo_subs:
			print t

		return ''

@app.route('/tengo', methods=['POST'])
def tengo():
	"""Handles 'tengo' submissions"""
	#=====[ Step 1: catch submission	]=====
	sender, subject, body, date = request_to_content(request)
	tengo_sub = TengoSub(sender, subject, body, date)
	print 'RECEIVED tengo: %s | %s | %s' % (sender, subject, date)
	print tengo_sub

	#=====[ Step 2: insert into db	]=====
	inventario.insert_tengo(tengo_sub)
	return ''


if __name__ == '__main__':
	app.run()