import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2

class Usuario(ndb.Model):
  nombre = ndb.StringProperty()
  apellidos = ndb.StringProperty()
  email = ndb.StringProperty()
  password = ndb.StringProperty()
  telefono = ndb.StringProperty()
  twitter = ndb.StringProperty()
  web = ndb.StringProperty()

class index(webapp2.RequestHandler):
    def post(self):
        usuario = Usuario()
        usuario.nombre = self.request.get('nombre')
        usuario.apellidos = self.request.get('apellidos')
        usuario.email = self.request.get('email')
        usuario.password = self.request.get('password')
        usuario.telefono = self.request.get('telefono')
        usuario.twitter = self.request.get('twitter')
        usuario.web = self.request.get('web')

        usuario.put()

        self.response.write('Guardado correctamente.')

application = webapp2.WSGIApplication([
    ('/usuario', index)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
