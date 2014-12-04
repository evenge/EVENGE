import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2
from google.appengine.ext import ndb
from datetime import datetime
import time


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
        print (self.request.get('asistencia'))
        evento.lugar = self.request.get('lugar')
        #evento.coordenadas = self.request.get('coordenadas')
        evento.descripcion = self.request.get('descripcion')
        evento.asistencia = (self.request.get('asistencia') == 'true')
        
        evento.put()

        self.response.write('El evento se ha creado correctamente')

application = webapp2.WSGIApplication([
    ('/evento', index)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
