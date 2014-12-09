import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2
from google.appengine.ext import ndb
from datetime import datetime

class Usuario(ndb.Model):
  nombre = ndb.StringProperty()
  apellidos = ndb.StringProperty()
  email = ndb.StringProperty()
  telefono = ndb.StringProperty()
  twitter = ndb.StringProperty()
  web = ndb.StringProperty()
  password = ndb.StringProperty()

class index(webapp2.RequestHandler):
    def post(self):
        usuario = Usuario()
        usuario.nombre = self.request.get('nombre')
        usuario.apellidos = self.request.get('apellidos')
        usuario.email = self.request.get('email')
        usuario.telefono = self.request.get('telefono')
        usuario.twitter = self.request.get('twitter')
        usuario.web = self.request.get('web')
        usuario.password = self.request.get('password')

        usuario.put()

        self.response.write('El usuario se ha creado correctamente.')

class ListarUsuarios(webapp2.RequestHandler):
    def get(self):
        result = Usuario.query()
        usuarios = []
        for usuario in result:
            usuarios.append(usuario)
        template_values = {'usuarios':usuarios}
        template = JINJA_ENVIRONMENT.get_template('/templates/mostrarUsuarios.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/usuario', index),
    ('/listarUsuarios', ListarUsuarios)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
