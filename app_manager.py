"""
Module: app_manager
===================

Defines class AppManager, responsible for managing all apps included in app 
directory
"""
import os
import sys
sys.path.append(os.path.dirname(__file__))
import inspect
from app_base import AppBase

class AppManager(object):
	"""
	Class: AppManager
	=================
	Manages all apps in app folder
	"""
	apps_dir = os.path.join(os.path.dirname(__file__), 'apps')
	non_apps = ['__init__.py', 'app_base.py', 'clima.py', 'yikyak.py']

	def get_app_names(self):
		"""returns list of app names"""
		py_files = [x for x in os.listdir(self.apps_dir) if x.endswith('.py')]
		app_files = [x for x in py_files if not x in self.non_apps]
		app_names = [x.split('.')[0].lower() for x in app_files]
		return app_names

	def import_app(self, app_name):
		"""imports App class from app named app_name"""
		app_mod = __import__('apps.%s' % (self.apps_dir, app_name), fromlist=['App'])
		return app_mod.App

	def verify_app(self, app):
		"""
		Returns True if app is verifiable

		Criterion:
		----------
		- is a subclass of apps.app_base.AppBase
		- implements 'process'
		"""
		#=====[ Step 1: subclass of apps.app_base.AppBase 	]=====
		if not issubclass(app, AppBase):
			return False
		
		#=====[ Step 2: implements 'process'	]=====
		methods = inspect.getmembers(app, predicate=inspect.ismethod)
		if not 'process' in [m[0] for m in methods]:
			return False

		return True

	def get_apps(self):
		"""returns iterable of (route, app_class) for all apps"""
		app_names = self.get_app_names()
		apps = {a:self.import_app(a) for a in app_names}
		apps = {k:v for k,v in apps.items() if self.verify_app(v)}
		return [('/%s' % k, v) for k, v in apps.items()]