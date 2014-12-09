import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2

class Index(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))

class InsertarAsistente(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/formAsistente.html')
        self.response.write(template.render(template_values))

class InsertarOrganizacion(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/formOrganizacion.html')
        self.response.write(template.render(template_values))

class InsertarEvento(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/formularioEvento.html')
        self.response.write(template.render(template_values))

class InsertarPonente(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/formPonente.html')
        self.response.write(template.render(template_values))

class InsertarUsuario(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/formUsuario.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', Index),
    ('/iAsistente', InsertarAsistente),
    ('/iEvento', InsertarEvento),
    ('/iOrganizacion', InsertarOrganizacion),
    ('/iPonente', InsertarPonente),
    ('/iUsuario', InsertarUsuario)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
