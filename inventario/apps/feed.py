# -*- coding: utf-8 -*-
from ..app_base import EmailAppBase
from bs4 import BeautifulSoup
from urllib import urlopen
import feedparser


class App(EmailAppBase):
    """
    App: Feed
    =========
    Returns the feed's data of a certain url
    """

    #=====[ Metadata	]=====
    dependencies = ['BeautifulSoup','feedparser']
    from_email = 'feed@ivioapp.com'

    def get_feeds(self, url, rss=True, atom=False):
        html_doc = urlopen(url).read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        for link in soup.find_all('link'):
            if (rss and link.get('type') == "application/rss+xml") or (atom and link.get('type') == "application/atom+xml"):
                if link.get('href').startswith('http'):
                    yield link.get('href')
                else:
                    yield url+link.get('href')
                    
                
    def get_feed_text(self, url):
        r = ''
        for feed_url in get_feeds(url,rss=True,atom=True):
            r += '--------------------------------\n'
            r += '+'+feed_url+'\n'
            r += '--------------------------------\n'
            data = feedparser.parse(feed_url)
            r += 'This Feed\'s data:\n'
            for key, value in data.feed.iteritems():
                if key != 'entries' :
                    try:
                        r += key+': '+value+"\n"
                    except:
                        pass
            r += '--------------------------------\n\n'
            r += 'This Feed\'s elements:\n'
            
            for item in data.entries:
                r += '+++++++++++++++++++++++++++++\n'
                r += 'Title: '+ item.title+'\n'
                r += 'Link: '+ item.link+'\n'
                r += 'Description: '+ item.description+'\n'
                r += '+++++++++++++++++++++++++++++\n'
        if r == '':
            r = 'No data found for this URL :(\n'
        return r

    def process(self, email):
        #=====[ Step 1: get body	]=====
        body = self.get_feed_text(email.subject.strip())

        #=====[ Step 2: send results	]=====
        self.email_client.send_message(
                                        self.from_email, 
                                        email.user, 
                                        'Feed Data for '+email.subject.strip(), 
                                        body
                                        )
