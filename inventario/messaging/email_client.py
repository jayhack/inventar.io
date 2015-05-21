from mandrill_client import MandrillClient

class EmailClient(MandrillClient):
	"""
	Class: EmailClient
	==================
	Client for accessing Email functionality

	Usage:
	------
	In [1]: email_client = EmailClient()
	In [2]: email_client.send_message(from_email, to_email, subject, body)
	"""

	def __init__(self):
		super(MandrillClient, self).__init__()

	def send_message(self, from_email, to_email, subject, body):
		"""
		Method: send_message:
		---------------------
		Sends an email from from_email to to_email with desired stats

		Args:
		-----
		- to_number: number to send to
		- text: content of message to send. Limited to self.max_chars
		"""
		return self.send(self.from_email, self.to_email, subject, body)

