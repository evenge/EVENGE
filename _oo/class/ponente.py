import webapp2
from google.appengine.ext import ndb

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

        self.response.write('Ponente guardado correctamente')

application = webapp2.WSGIApplication([
    ('/ponente', index)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
