import webapp2
from google.appengine.ext import ndb

class Asistente(ndb.Model):
    idAsistente = ndb.StringProperty()
    idEvento = ndb.StringProperty()
    nombre = ndb.StringProperty()
    apellidos = ndb.StringProperty()
    email = ndb.StringProperty()
    telefono = ndb.StringProperty()
    twitter = ndb.StringProperty()
    dni = ndb.StringProperty()
    asistido = BooleanProperty()
