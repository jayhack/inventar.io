"""
Module: landing_page
====================
Contains definiton of landing page app
"""
import os
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), './static')),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class LandingPageApp(webapp2.RequestHandler):
	"""
	Page: LandingPage
	=================
	Just contains landing page
	"""
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render())