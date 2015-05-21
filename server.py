"""
Module: server
==============
Contains main flask application
"""
import os

#=====[ webapp2	]=====
import webapp2
import webapp2_static
from inventario import AppManager

#=====[ Apps setup	]=====
base_dir = os.path.dirname(os.path.realpath(__file__))
app_manager = AppManager(base_dir, 'inventario.apps')
apps = app_manager.get_apps()
# apps += [('/', LandingPageApp)]
app = webapp2.WSGIApplication(apps)
