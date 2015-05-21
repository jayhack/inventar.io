import webapp2

class AppBase(webapp2.RequestHandler):
	"""
	Class: AppBase
	==============
	Abstract class forming base for all other app bases

	Inheritors should specify self.request_extractor and fill out
	process(self, msg)
	"""

	#=====[ extract_msg	]=====
	# flask.request -> desired message format
	exract_msg = None

	def __init__(self, request=None, response=None):
		self.initialize(request, response)

	def post(self):
		"""calls self.process with results of request extraction"""
		msg = self.extract_msg(self.request)
		if not msg is None:
			self.process(msg)
		self.response.write('')

	def process(self, msg):
		"""override"""
		raise NotImplementedError

