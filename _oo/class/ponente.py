import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2
from google.appengine.ext import ndb
from datetime import datetime

class Ponente(ndb.Model):
  nombre = ndb.StringProperty()
  apellidos = ndb.StringProperty()
  email = ndb.StringProperty()
  telefono = ndb.StringProperty()
  twitter = ndb.StringProperty()
  web = ndb.StringProperty()

class index(webapp2.RequestHandler):
    def post(self):
        ponente = Ponente()
        ponente.nombre = self.request.get('nombre')
        ponente.apellidos = self.request.get('apellidos')
        ponente.email = self.request.get('email')
        ponente.telefono = self.request.get('telefono')
        ponente.twitter = self.request.get('twitter')
        ponente.web = self.request.get('web')

        ponente.put()

        self.response.write('El ponente se ha creado correctamente')

class ListarPonentes(webapp2.RequestHandler):
    def get(self):
        result = Ponente.query()
        ponentes = []
        for ponente in result:
            ponentes.append(ponente)
        template_values = {'ponentes':ponentes}
        template = JINJA_ENVIRONMENT.get_template('/templates/mostrarPonentes.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/ponente', index),
    ('/listarPonentes', ListarPonentes)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
