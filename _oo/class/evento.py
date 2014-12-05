import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2
from google.appengine.ext import ndb
from datetime import datetime


class Evento(ndb.Model):
  nombre = ndb.StringProperty()
  tipo = ndb.IntegerProperty()
  idCreador = ndb.StringProperty()
  hora = ndb.TimeProperty()
  fecha = ndb.DateProperty()
  lugar = ndb.StringProperty()
  coordenadas = ndb.GeoPtProperty()
  descripcion = ndb.TextProperty()
  asistencia = ndb.BooleanProperty()

class index(webapp2.RequestHandler):
    def post(self):
        evento = Evento()
        evento.nombre = self.request.get('nombre')
        evento.tipo = 0 #Provisional, hasta que establezcamos politica de tipos
        evento.idCreador = "1" #Provisional, por ahora todos son admin
        evento.fecha = datetime.strptime(self.request.get('fecha'), "%Y-%m-%d")
        evento.hora = datetime.strptime(self.request.get('hora'),"%H:%M").time()
        evento.lugar = self.request.get('lugar')
        #evento.coordenadas = self.request.get('coordenadas')
        evento.descripcion = self.request.get('descripcion')
        evento.asistencia = (self.request.get('asistencia') == 'true')

        evento.put()

        self.response.write('El evento se ha creado correctamente')

class ListarEventos(webapp2.RequestHandler):
    def get(self):
        result = Evento.query()
        eventos = []
        for evento in result:
            eventos.append(evento)
        template_values = {'eventos':eventos}
        template = JINJA_ENVIRONMENT.get_template('/templates/mostrarEventos.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/evento', index),
    ('/listarEventos', ListarEventos)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
