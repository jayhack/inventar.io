from ..app_base import EmailAppBase
import praw


class App(EmailAppBase):
	"""
	App: Reddit
	=========
	Returns Returns Hot topics on the reddit main page or a sub reddit depends on the subject line
	"""

	#=====[ Metadata	]=====
	dependencies = ['praw']
	from_email = 'reddit@ivioapp.com'
	user_agent = 'Avioapp scrapper 1.0 by /u/ED_Os'
	post_limit = 20

	def posts_to_summary(self, posts):
		"""posts generator -> unicode"""
		return u'\n'.join([unicode(p) for p in posts])

	def get_summary(self, email):
		"""returns formatted summary"""
		#=====[ Step 1: connect	]=====
		r = praw.Reddit(user_agent=self.user_agent)

		#=====[ Step 2: get summary	]=====
		subreddit = unicode(email.subject.strip())
		if len(subreddit) == 0:
			posts = r.get_front_page(limit=self.post_limit)
			summary = self.posts_to_summary(posts)
		else:
			try:
				posts = r.get_subreddit(subreddit, limit=self.post_limit)
				summary = self.posts_to_summary(posts)
			except:
				summary = u'Could not find subreddit: %s' % subreddit

		print 'subreddit type: ', type(subreddit)
		print 'summary type: ', type(summary)
		print 'len of summary: ', len(summary)
		#=====[ Step 3: format	]=====
		return u'''
Subreddit Summary: %s
=============================

%s
''' % (subreddit, summary)


	def process(self, email):
		#=====[ Step 1: get body	]=====
		body = self.get_summary(email)
		print 'body type: ', type(body)

		#=====[ Step 2: send results	]=====
		self.email_client.send_message(
										self.from_email, 
										email.user, 
										u'Resultados de Reddit', 
										body
										)