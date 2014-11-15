import webapp2
from google.appengine.ext import ndb

class EventoPonente(ndb.Model):
	idEvento = ndb.StringProperty()
	idPonente = ndb.StringProperty()
