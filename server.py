"""
Module: server
==============

Contains main flask application
"""
from flask import Flask
from inventario import Inventario

#=====[ Step 1: setup	]=====
app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, world! Welcome to inventar.io'

@app.route('/quiero')
def quiero():
	return "... quiero ..."

@app.route('/tengo')
def tengo():
	return "... tengo ..."

if __name__ == '__main__':
	app.run()