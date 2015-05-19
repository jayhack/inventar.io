"""
Module: server
==============
Contains main flask application
"""
import os
import sys
import json
from flask import Flask
from flask import request
from flask import send_from_directory
from mail import IvioMail, IvioMailClient
from dbclient import DBClient
from inventory import InventoryEmail

#=====[ Setup	]=====
base_dir = os.path.split(os.path.realpath(__file__))[0]
static_dir = os.path.join(base_dir, 'static')
assets_dir = os.path.join(static_dir, 'assets')
apps_dir = os.path.join(base_dir, 'apps')
app = Flask(__name__, static_folder=assets_dir)
db_client = DBClient()
mail_client = IvioMailClient()

from yapsy.PluginManager import PluginManager

def main():   
	# Load the plugins from the plugin directory.
	manager = PluginManager()
	manager.setPluginPlaces(["plugins"])
	manager.collectPlugins()

	# Loop round the plugins and print their names.
	for plugin in manager.getAllPlugins():
		print plugin
		# plugin.plugin_object.print_name()

if __name__ == "__main__":
	main()

# for importer, app_name, ispkg in pkgutil.iter_modules([apps_dir]):

# 	full_app_name = 'apps.%s' % (app_name)
# 	app = __import__(full_app_name)
# 	print full_app_name
# 	for name, obj in inspect.getmembers(app):
# 		if inspect.isclass(obj):
# 			print name
# 	print



	# if full_app_name not in sys.modules:
		# module = importer.find_module(app_name).load_module(full_app_name)
		# print module


################################################################################
####################[ LANDING PAGE ]############################################
################################################################################

# @app.route('/')
# def index():
# 	"""
# 	Hook: index
# 	===========
# 	Returns landing page
# 	"""
# 	return send_from_directory(static_dir, 'index.html')






################################################################################
##############################[ Q PAZA ]########################################
################################################################################

# @app.route('/qpaza', methods=['POST'])
# def qpaza():
# 	"""
# 	Hook: qpaza
# 	==========
# 	returns a newsletter on social events
# 	"""
# 	#=====[ Step 1: grab email	]=====
# 	mail = mail_client.request_to_mail(request)
# 	if mail is None:
# 		return ''

# 	#=====[ Step 2: THE GUTS	]=====
# 	events = filter(lambda l: l.strip().startswith('@'), email.body.split('\n'))

# 	for eventDescription in events:
# 		eventToAdd = { 'event':eventDescription }
# 		dbclient.put('events', eventToAdd)

# 	newsLetterEvents = dbclient.list('events')

# 	result = ""
# 	for event in newsLetterEvents:
# 		result = result + event['event'] + '\n\n'

# 	#=====[ Step 3: mail back the message	]=====
# 	mail_client.send_message(
# 								mail.user,
# 								'Event Newsletter',
# 								pprint.pformat(result)								
# 							)
# 	return ''




################################################################################
########################[ YIK YAK FEED ]########################################
################################################################################

# @app.route('/yikyakpost', methods=['POST'])
# def yikyakpost():
# 	"""
# 	Hook: yikyakpost
# 	==========
# 	posts to yikyak post
# 	"""
# 	#=====[ Step 1: grab email	]=====
# 	mail = mail_client.request_to_mail(request)
# 	if mail is None:
# 		return ''
# 	postings = YikYakEmail(mail)

# 	#=====[ Step 2: post to yikyak and upvote	]=====
# 	post = postings.post
# 	if(post):
# 		dbclient.put('yikyak', [post])
# 	votes = postings.votes
# 	posts = dbclient.list("yikyak")
	

# 	#=====[ Step 3: configure update votes	]=====


# 	result = ""
	
	
# 	# for vote in votes:
# 	# 	post_id = re.findall(r'@([a-zA-Z0-9-]+)', vote)
# 	# 	if(len(post_id) == 0):
# 	# 		continue
# 	# 	post_id = post_id[0]
# 	# 	print("post id after retrieving" + str(post_id))
# 	# 	post = dbclient.search('yikyak','unique_id',post_id)
# 	# 	print("result of post: " + pprint.pformat(post))

# 	# 	change = 0;
# 	# 	if "+1" in vote:
# 	# 		change = 1
# 	# 	elif "-1" in vote:
# 	# 		change = -1
# 	# 	post['votes'] = post['votes'] + change
# 	# 	dbclient.update('yikyak',post['unique_id'],post)

# 		# result = result + "ID: " + post_id + '\n' + "Change by: " + str(change) + '\n\n'

# 	#=====[ Step 4: configure posts	]=====


# 	for post in posts:
# 		result = result + "ID: " + post['unique_id'] + '\n' + "Post: " + json.dumps(post['post'].strip('"').strip('-')) + '\n' + "Votes: " + json.dumps(post['votes']) + '\n\n'

# 	#=====[ Step 5: mail back the posts	]=====


# 	mail_client.send_message(
# 								mail.user,
# 								'post',
# 								result								
# 							)

# 	return ''



################################################################################
####################[ INVENTORY SEARCH ]########################################
################################################################################

# @app.route('/quiero', methods=['POST'])
# def quiero():
# 	"""
# 	Hook: quiero
# 	============

# 	Allows users to post items they *want* to 'quiero' collection
# 	in database and returns results if there are any
# 	"""
# 	#=====[ Step 1: grab email	]=====
# 	mail = mail_client.request_to_mail(request)
# 	if mail is None:
# 		return ''
# 	quiero = InventoryEmail(mail)

# 	#=====[ Step 2: insert items into 'quiero' collection	]=====
# 	dbclient.put('quiero', quiero.items)

# 	#=====[ Step 3: find matches and mail back	]=====
# 	matches = {x['name']:dbclient.search('tengo', 'name', x['name']) for x in quiero.items}

# 	#=====[ Step 4: mail back	]=====
# 	mail_client.send_message(
# 								mail.user,
# 								'resultados',
# 								pprint.pformat(matches)
# 							)
# 	return ''

# @app.route('/tengo', methods=['POST'])
# def tengo():
# 	"""Handles 'tengo' submissions"""
# 	#=====[ Step 1: grab email	]=====
# 	mail = mail_client.request_to_mail(request)
# 	if mail is None:
# 		return ''
# 	tengo = InventoryEmail(mail)

# 	#=====[ Step 2: insert items into db	]=====
# 	dbclient.put('tengo', tengo.items)

# 	#=====[ Step 3: find/send matches	]=====
# 	for item in tengo.items:
# 		matches = dbclient.search('quiero', 'name', item['name'])
# 		for match in matches:
# 			mail_client.send_message(
# 										match['user'],
# 										'resultados',
# 										pprint.pformat(item)
# 									)
# 	return ''


# if __name__ == '__main__':
	# app.run(debug=True)
