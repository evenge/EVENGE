import webapp2
from google.appengine.ext import ndb

class Usuario(ndb.Model):
  nombre = ndb.StringProperty()
  apellidos = ndb.StringProperty()
  email = ndb.StringProperty()
  password = ndb.StringProperty()
  telefono = ndb.IntegerProperty()
  twitter = ndb.StringProperty()
  web = ndb.StringProperty()
