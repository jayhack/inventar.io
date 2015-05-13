"""
Module: gmail
=============

Functionality for interacting with Gmail

Components taken from https://gist.github.com/baali/2633554
"""
import email
import getpass
import imaplib
import os
import sys
import datetime as dt

class GmailEmail(object):
    """class for representing an email"""

    def __init__(self, message_parts):
        msg = email.message_from_string(message_parts[0][1])
        self.sender = msg['from']
        self.subject = msg['subject']


class GmailClient(object):
    """interface to gmail"""

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.connected = False
        self.session = None
        self.connect()

    def __del__(self):
        self.disconnect()

    def connect(self):
        """connects to gmail"""
        if not self.connected:
            try:
                self.imap_session = imaplib.IMAP4_SSL('imap.gmail.com')
                typ, account_details = self.imap_session.login(self.username, self.password)
                if typ != 'OK':
                    raise Exception("Unable to log in! (incorrect credentials?)")
                self.connected = True
            except:
                raise Exception("Unable to log in! (incorrect credentials?)")

    def disconnect(self):
        """disconnects from gmail"""
        self.imap_session.close()
        self.imap_session.logout()
        self.connected = False


    def iter_emails(self):
        """iterates over all emails in inbox"""
        #=====[ Step 1: select appropriate mail ]=====
        self.imap_session.select('INBOX')
        searchString = "ALL"
        typ, data = self.imap_session.search(None, searchString)
        if typ != 'OK':
            raise Exception("Error searching inbox ")
        
        #======[ Step 2: iterate over emails ]=====
        for msgId in data[0].split():
            typ, message_parts = self.imap_session.fetch(msgId, '(RFC822)')
            if typ != 'OK':
                raise Exception("Error fetching mail")

            yield GmailEmail(message_parts)