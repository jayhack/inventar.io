"""
Module: mandrill_utils
======================

Contains utilities for working with Mandrill
"""
import json
from email.utils import parseaddr
import mandrill
from messages import Email
from messages import SMS


def validate_email_addr(email_addr):
	"""returns True if email_addr is valid"""
	parsed = parseaddr(email_addr)
	if len(parsed[1]) == 0:
		return False
	return True


def flask_request_to_email(request):
	"""flask.request -> Mail object"""
	if type (request.get('mandrill_events')) in [str, unicode]:
		j = json.loads(request.get('mandrill_events'))
	else:
		j = request.get('mandrill_events')
	if len(j) == 0:
		return None

	d = j[0]
	msg = d['msg']
	return Email(msg['from_email'], msg['subject'], msg['text'], str(d['ts']))


def flask_request_to_sms(request):
	"""flask.request -> SMS object"""
	mail = flask_request_to_email(request)
	if mail is None:
		return None
	return SMS(mail.user, mail.text, mail.date)


def make_message(from_email, to_email, subject, body):
	"""returns message in Mandrill.send_message()'s desired format"""
	if not validate_email_addr(from_email) and validate_email_addr(to_email):
		raise Exception("Invalid email address")
	return 	{
				'from_email':from_email,
				'to': [{'email':to_email, 'type': 'to'}],
				'subject':subject,
				'text':body,
			}