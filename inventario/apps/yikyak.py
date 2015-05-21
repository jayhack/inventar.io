from ..app_base import EmailAppBase

class App(EmailAppBase):
	"""
	App: YikYak
	===========

	Allows users to post to and view an anonymous feed. 
	"""
	#=====[ metadata ]=====
	dependencies = []
	from_email = 'yikyak@ivioapp.com'
	db_collection = 'yikyak'
	char_limit = 140
	feed_header = """YIKYAK FEED:\n============\n\n"""

	def post_to_str(self, post):
		"""post -> string"""
		if not 'post' in post:
			print post
		return "%s\n----------\n" % post['post']

	def get_feed(self):
		"""returns current feed as string"""
		posts = self.db_client.list(self.db_collection)
		post_strs = [self.post_to_str(p) for p in reversed(posts)][:20]
		return self.feed_header + '\n'.join(post_strs)

	def submit_yak(self, mail):
		"""processes yikyak posts; limit 140 characters"""
		post = mail.subject.strip()[:self.char_limit]
		self.db_client.put(self.db_collection, {'post':post, 'user':mail.user})

	def process(self, mail):
		#=====[ Step 1: submit post	]=====
		if len(mail.subject.strip()) > 3:
			self.submit_yak(mail)

		#=====[ Step 2: send results	]=====
		from_email = self.from_email
		to_email = mail.user
		subject = 'yikyak feed'
		body = self.get_feed()
		self.email_client.send_message(from_email, to_email, subject, body)
