"""
Module: wiki
============

Contains app Wiki, which provides access to Wikipedia summaries
"""
from yapsy.IPlugin import IPlugin

class WikiApp(IPlugin):

	# def __init__(self, x):
		# pass

    def print_name(self):
        print "This is WikiApp"

    hook = '/wiki'
    """
    TEST
    """

        # """

# from app_base import AppBase
# import wikipedia
# from yapsy.IPlugin import IPlugin

# class WikiApp(IPlugin):
# 	"""
# 	App: Wiki
# 	=========

# 	Returns wikipedia summary of concept named in subject line
# 	"""
# 	#=====[ metadata ]=====
# 	name = 'wiki'
# 	hook = '/wiki'

# 	def __init__(self, db_client, mail_client):
# 		super(InventarioAppBase, self).__init__(db_client, mail_client)

# 	def process(self, mail):
# 		summary = wikipedia.summary(mail.subject.strip())
# 		mail.client.send_message(mail.user, 'resultados', summary)

# 	def print_name(self):
# 		print 'HELLO< WORLD'

# from yappsy.IPlugin import IPlugin

# class WikiApp(IPlugin):
# 	def print_name(self):
# 		print "This is WikiApp"

