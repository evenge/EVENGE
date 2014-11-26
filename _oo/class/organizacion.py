import webapp2
from google.appengine.ext import ndb

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

        self.response.write('Organización guardada correctamente')

application = webapp2.WSGIApplication([
    ('/organizacion', index)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
