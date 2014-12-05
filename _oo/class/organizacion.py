import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2
from google.appengine.ext import ndb
from datetime import datetime

class Organizacion(ndb.Model):
  nombre = ndb.StringProperty()
  email = ndb.StringProperty()
  telefono = ndb.StringProperty()
  twitter = ndb.StringProperty()
  web = ndb.StringProperty()

class index(webapp2.RequestHandler):
    def post(self):
        organizacion = Organizacion()
        organizacion.nombre = self.request.get('nombre')
        organizacion.email = self.request.get('email')
        organizacion.telefono = self.request.get('telefono')
        organizacion.twitter = self.request.get('twitter')
        organizacion.web = self.request.get('web')

        organizacion.put()

        self.response.write('La organizacion se ha creado correctamente')

class ListarOrganizaciones(webapp2.RequestHandler):
    def get(self):
        result = Organizacion.query()
        organizaciones = []
        for organizacion in result:
            organizaciones.append(organizacion)
        template_values = {'organizaciones':organizaciones}
        template = JINJA_ENVIRONMENT.get_template('/templates/mostrarOrganizaciones.html')
        self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([
    ('/organizacion', index),
    ('/listarOrganizaciones', ListarOrganizaciones)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
