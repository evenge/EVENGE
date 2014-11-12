import webapp2
from google.appengine.ext import ndb

class Organizacion(ndb.Model):
  nombre = ndb.StringProperty()
  email = ndb.StringProperty()
  telefono = ndb.StringProperty()
  twitter = ndb.StringProperty()
  web = ndb.StringProperty()
