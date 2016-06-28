from ..appbase import EmailAppBase
import stackexchange, re
from googleapiclient.discovery import build

# secret keys
GOOGLE_API_KEY = None
GOOGLE_CSE_KEY = None
SE_KEY = None

class App(EmailAppBase):
	"""
	App: StackExchange
	=========
	Returns top hit result for StackOverflow query
	"""

	#=====[ Metadata	]=====
	dependencies = ['stackexchange','googleapiclient','re']
	from_email = 'stackoverflow@ivioapp.com'

	def get_search(self, email):
		"""returns formatted search"""
		#=====[ Step 1: get search results	]=====
		try:
            # Query Google CSE to get the top hit SE question
            service = build("customsearch","v1",developerKey=GOOGLE_API_KEY)
            links = service.cse().list(q=email.subject.strip(),cx=GOOGLE_CSE_KEY)
            question_id = re.split('/',results['items'][0]['link'])[4]

            # Query StackExchange for data on top hit SE question
            site = stackexchange.Site(stackexchange.StackOverflow, app_key=SE_KEY)
            site.be_inclusive()

            question = site.question(question_id)
            answer = question.answers[0]

            op = question.owner
            rp = site.users(answer.owner_id) # answer.owner is broken

            # Prepare data for output
            result = '%s\n' % question.title
            result += '%s\n' % links[0] # must include for SE licensing reasons (also for names/links below)
            result += '%s\n' % question.body
            result += '%s\n' % op.display_name
            result += 'http://%s/users/%s\n' % (site.root_domain,op.id)
            result += '-'*10
            result += '%s\n' % answer.body
            result += '%s\n' % rp.display_name
            result += 'http://%s/users/%s\n' % (site.root_domain),rp.id)

		except:
			result = u'Error buscando '+ unicode(email.subject.strip())

		#=====[ Step 2: format	]=====
		return '''
Resultado de StackOverflow:
==================

%s
---
%s
''' % (unicode(email.subject.strip()),unicode(result))

	def process(self, email):
		#=====[ Step 1: get body	]=====
		body = self.get_search(email)

		#=====[ Step 2: send results	]=====
		self.email_client.send_message(
										self.from_email,
										email.user,
										'StackOverflow Resultado',
										body
										)
