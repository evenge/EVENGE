import webapp2
from google.appengine.ext import ndb

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
