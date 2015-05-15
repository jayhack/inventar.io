"""
Module: server
==============
Contains main flask application
"""
import os
import json
import pprint
import re
from flask import Flask
from flask import request
from flask import send_from_directory
from mail import IvioMail, IvioMailClient
from dbclient import DBClient
from inventory import InventoryEmail
from yikyak import YikYakEmail
import wikipedia

#=====[ Setup	]=====
base_dir = os.path.split(os.path.realpath(__file__))[0]
static_dir = os.path.join(base_dir, 'static')
assets_dir = os.path.join(static_dir, 'assets')
app = Flask(__name__, static_folder=assets_dir)
dbclient = DBClient()
mail_client = IvioMailClient()


################################################################################
####################[ LANDING PAGE ]############################################
################################################################################

@app.route('/')
def index():
	"""
	Hook: index
	===========
	Returns landing page
	"""
	return send_from_directory(static_dir, 'index.html')




################################################################################
####################[ WIKIPEDIA ACCESS ]########################################
################################################################################

@app.route('/wiki', methods=['POST'])
def wiki():
	"""
	Hook: wiki
	==========
	returns top wikipedia search from subject line
	"""
	#=====[ Step 1: grab email	]=====
	mail = mail_client.request_to_mail(request)
	if mail is None:
		return ''

	#=====[ Step 2: search wikipedia	]=====
	result = wikipedia.summary(mail.subject.strip())

	#=====[ Step 3: mail back the message	]=====
	mail_client.send_message(
								mail.user,
								'resultados',
								pprint.pformat(result)								
							)
	return ''



################################################################################
########################[ YIK YAK FEED ]########################################
################################################################################

@app.route('/yikyakfeed', methods=['POST'])
def yikyakfeed():
	"""
	Hook: yikyakfeed
	==========
	returns yikyakfeed
	"""
	#=====[ Step 1: grab email	]=====
	mail = mail_client.request_to_mail(request)
	if mail is None:
		return ''

	#=====[ Step 2: get all posts from yikyak collection	]=====
	posts = dbclient.list("yikyak")

	#=====[ Step 3: Configure posts	]=====


	result = ""
	for post in posts:
		result = result + "ID: " + post['unique_id'] + '\n' + "Post: " + json.dumps(post['post'].strip('"').strip('-')) + '\n' + "Votes: " + json.dumps(post['votes']) + '\n\n'

	#=====[ Step 4: mail back the posts	]=====

	mail_client.send_message(
								mail.user,
								'post',
								result								
							)

	return ''


################################################################################
########################[ YIK YAK FEED ]########################################
################################################################################

@app.route('/yikyakpost', methods=['POST'])
def yikyakpost():
	"""
	Hook: yikyakpost
	==========
	posts to yikyak post
	"""
	#=====[ Step 1: grab email	]=====
	mail = mail_client.request_to_mail(request)
	if mail is None:
		return ''
	postings = YikYakEmail(mail)

	#=====[ Step 2: post to yikyak and upvote	]=====
	post = postings.post
	if(post):
		dbclient.put('yikyak', [post])
	votes = postings.votes
	posts = dbclient.list("yikyak")
	

	#=====[ Step 3: configure posts and votes	]=====


	result = ""
	for post in posts:
		result = result + "ID: " + post['unique_id'] + '\n' + "Post: " + json.dumps(post['post'].strip('"').strip('-')) + '\n' + "Votes: " + json.dumps(post['votes']) + '\n\n'
	
	for vote in votes:
		post_id = re.findall(r'@(\d+)', vote)[0]
		change = 0;
		if "+1" in vote:
			change = 1
		elif "-1" in vote:
			change = -1
		result = result + "ID: " + post_id + '\n' + "Change by: " + str(change) + '\n\n'


	#=====[ Step 4: mail back the posts	]=====


	mail_client.send_message(
								mail.user,
								'post',
								result								
							)

	return ''



################################################################################
####################[ INVENTORY SEARCH ]########################################
################################################################################

@app.route('/quiero', methods=['POST'])
def quiero():
	"""
	Hook: quiero
	============

	Allows users to post items they *want* to 'quiero' collection
	in database and returns results if there are any
	"""
	#=====[ Step 1: grab email	]=====
	mail = mail_client.request_to_mail(request)
	if mail is None:
		return ''
	quiero = InventoryEmail(mail)

	#=====[ Step 2: insert items into 'quiero' collection	]=====
	dbclient.put('quiero', quiero.items)

	#=====[ Step 3: find matches and mail back	]=====
	matches = {x['name']:dbclient.search('tengo', 'name', x['name']) for x in quiero.items}

	#=====[ Step 4: mail back	]=====
	mail_client.send_message(
								mail.user,
								'resultados',
								pprint.pformat(matches)
							)
	return ''

@app.route('/tengo', methods=['POST'])
def tengo():
	"""Handles 'tengo' submissions"""
	#=====[ Step 1: grab email	]=====
	mail = mail_client.request_to_mail(request)
	if mail is None:
		return ''
	tengo = InventoryEmail(mail)

	#=====[ Step 2: insert items into db	]=====
	dbclient.put('tengo', tengo.items)

	#=====[ Step 3: find/send matches	]=====
	for item in tengo.items:
		matches = dbclient.search('quiero', 'name', item['name'])
		for match in matches:
			mail_client.send_message(
										match['user'],
										'resultados',
										pprint.pformat(item)
									)
	return ''


if __name__ == '__main__':
	app.run(debug=True)
