#!/usr/bin/env python
#
# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import urllib

from google.appengine.ext import ndb
from google.appengine.api import users
from google.appengine.ext.webapp import template
import webapp2


# Global variables
API_KEY = "your-api-key"
PROJECT_ID = "your-numeric-project-id"

# Set up the Prediction API service
# TODO: Fill in


def get_service():
    return None


def predict_language(message):
    return True


def get_sentiment(message):
    return True


def guestbook_key(guestbook_name=None):
    """Constructs an ndb key for a Guestbook entity with guestbook_name."""
    return ndb.Key('Guestbook', guestbook_name or 'default_guestbook')


class Author(ndb.Model):
    """A model representing an author."""
    identity = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)


class Greeting(ndb.Model):
    """A model representing an individual Guestbook entry.

    The model has an author, content, and date.
    """
    author = ndb.StructuredProperty(Author)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)


class TrainModel(webapp2.RequestHandler):
    def get(self):
        self.response.out.write('Not implemented!')


class CheckModel(webapp2.RequestHandler):
    def get(self):
        # checks if a model is trained
        self.response.out.write("Not implemented!")


class MainPage(webapp2.RequestHandler):
    def get(self):
        guestbook_name = self.request.get('guestbook_name')
        greetings_query = Greeting.query(
            ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
        greetings = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'
        template_values = {
            'greetings': greetings,
            'url': url,
            'url_linktext': url_linktext
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))


class Guestbook(webapp2.RequestHandler):
    def post(self):
        guestbook_name = self.request.get('guestbook_name')
        greeting = Greeting(parent=guestbook_key(guestbook_name))

        if users.get_current_user():
            greeting.author = Author(
                identity=users.get_current_user().user_id(),
                email=users.get_current_user().email())
        greeting.content = self.request.get('content')
        greeting.put()
        self.redirect('/?' +
                      urllib.urlencode({'guestbook_name': guestbook_name}))


APPLICATION = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook),
    ('/trainmodel', TrainModel),
    ('/checkmodel', CheckModel)
], debug=True)
