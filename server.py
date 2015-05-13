"""
Module: server
==============

Contains main flask application
"""
from flask import Flask
from inventario import Inventario

app = Flask(__name__)


@app.route('/')
def index():
	return 'Hello, world! Welcome to inventar.io'

@app.route('/quiero')
def quiero():
	return "... quiero ..."
