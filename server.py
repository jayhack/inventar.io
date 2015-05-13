"""
Module: server
==============

Contains main flask application
"""
from inventario import Inventario

if __name__ == '__main__':

	inventario = Inventario('ivio.app@gmail.com', 'only the present', 'inventario.db')
	inventario.update()

	print '=====[ REQUESTS ]====='
	for request in inventario.get_requests():
		print '%s | %s' % (request.sender, request.item_name)
	print

	print '=====[ SUBMISSIONS ]====='
	for submission in inventario.get_submissions():
		print '%s | %s' % (submission.sender, submission.item_name)
	print


