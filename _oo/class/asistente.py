import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2
from google.appengine.ext import ndb

class Asistente(ndb.Model):
    idEvento = ndb.StringProperty()
    nombre = ndb.StringProperty()
    apellidos = ndb.StringProperty()
    email = ndb.StringProperty()
    telefono = ndb.StringProperty()
    twitter = ndb.StringProperty()
    dni = ndb.StringProperty()
    asistido = ndb.BooleanProperty()

class index(webapp2.RequestHandler):
    def post(self):
        asistente = Asistente()
        asistente.idEvento = self.request.get('evento')
        asistente.nombre = self.request.get('nombre')
        asistente.apellidos = self.request.get('apellidos')
        asistente.email = self.request.get('email')
        asistente.telefono = self.request.get('telefono')
        asistente.twitter = self.request.get('twitter')
        asistente.dni = self.request.get('dni')
        asistente.asistido = False

        asistente.put()

        self.response.write('Guardado correctamente :)')

application = webapp2.WSGIApplication([
    ('/asistente', index)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
