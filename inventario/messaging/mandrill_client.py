from mandrill import Mandrill
from mandrill_utils import make_message
from secrets import MANDRILL_API_KEY

class MandrillClient(object):
	"""
	Class: MandrillClient
	=====================
	Abstract class implementing patterns that both EmailClient and SMSClient
	will be using
	"""

	def __init__(self):
		self.client = Mandrill(MANDRILL_API_KEY)

	def send(self, from_email, to_email, subject, body):
		"""sends email with specified details, returning result"""
		msg = make_message(from_email, to_email, subject, body)
		return self.client.messages.send(msg, async=False, ip_pool='Main Pool')



