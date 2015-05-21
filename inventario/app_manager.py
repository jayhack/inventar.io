"""
Module: app_manager
===================

Defines class AppManager, responsible for managing all apps included in app 
directory
"""
import os
import sys
import inspect
from app_base import AppBase

class AppManager(object):
	"""
	Class: AppManager
	=================
	Manages all apps in app folder
	"""

	#=====[ non_apps	]=====
	# ignores these files from apps directory
	non_apps = ['__init__.py', 'app_base.py', 'yikyak.py']

	def __init__(self, server_dir, apps_mod):
		"""
		Args:
		-----
		- server_dir: directory that server is located in
		- apps_mod: mod that server would import apps from
		"""
		self.server_dir = server_dir
		self.apps_mod = apps_mod
		apps_relpath = self.apps_mod.replace('.', '/')
		self.apps_dir = os.path.join(self.server_dir, apps_relpath)
		print self.apps_dir

	def get_app_names(self):
		"""returns list of app names"""
		py_files = [x for x in os.listdir(self.apps_dir) if x.endswith('.py')]
		app_files = [x for x in py_files if not x in self.non_apps]
		app_names = [x.split('.')[0].lower() for x in app_files]
		return app_names

	def import_app(self, app_name):
		"""imports App class from app named app_name"""
		app_mod_name = '%s.%s' % (self.apps_mod, app_name)
		app_mod = __import__(app_mod_name, fromlist=['App'])
		for dependency in app_mod.App.dependencies:
			__import__(dependency)
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