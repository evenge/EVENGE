import webapp2
from google.appengine.ext import ndb

class EventoPonente(ndb.Model):
	idOrganizacion = ndb.StringProperty()
	idUsuario = ndb.StringProperty()
