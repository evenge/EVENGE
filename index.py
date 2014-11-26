import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2

formulario = """\
            <form action="/asistente" method="post">
            <div><label for="evento">Id evento: </label><input type="text" id="evento" name="evento"/></div>
            <div><label for="nombre">Nombre: </label><input type="text" id="nombre" name="nombre"/></div>
            <div><label for="apellidos">Apellidos: </label><input type="text" id="apellidos" name="apellidos"/></div>
            <div><label for="email">Email: </label><input type="text" id="email" name="email"/></div>
            <div><label for="telefono">Telefono: </label><input type="text" id="telefono" name="telefono"/></div>
            <div><label for="twitter">Twitter: </label><input type="text" id="twitter" name="twitter"/></div>
            <div><label for="dni">Dni: </label><input type="text" id="dni" name="dni"/></div>
            <div><input type="submit" value="Guardar"></div>
            </form>
            """

formulario_usuario = """\
            <form action="/usuario" method="post">
            <div><label for="nombre">Nombre: </label><input type="text" id="nombre" name="nombre"/></div>
            <div><label for="apellidos">Apellidos: </label><input type="text" id="apellidos" name="apellidos"/></div>
            <div><label for="email">Email: </label><input type="text" id="email" name="email"/></div>
            <div><label for="password">Password: </label><input type="text" id="password" name="password"/></div>
            <div><label for="telefono">Telefono: </label><input type="text" id="telefono" name="telefono"/></div>
            <div><label for="twitter">Twitter: </label><input type="text" id="twitter" name="twitter"/></div>
            <div><label for="web">Web: </label><input type="text" id="web" name="web"/></div>
            <div><input type="submit" value="Guardar"></div>
            </form>
            """


class index(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))

class insertar_asistente(webapp2.RequestHandler):
    def get(self):
        self.response.write(formulario)

class insertar_usuario(webapp2.RequestHandler):
    def get(self):
        self.response.write(formulario_usuario)


application = webapp2.WSGIApplication([
    ('/', index),
    ('/iAsistente', insertar_asistente),
    ('/iUsuario', insertar_usuario)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
