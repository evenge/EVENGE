import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2

formularioAsistente = """\
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
formularioOrganizacion = """\
        <form action="/asistente" method="post">
            <div><label for="nombre">Nombre: </label><input type="text" id="nombre" name="nombre"/></div>
            <div><label for="email">Email: </label><input type="text" id="email" name="email"/></div>
            <div><label for="telefono">Telefono: </label><input type="text" id="telefono" name="telefono"/></div>
            <div><label for="twitter">Twitter: </label><input type="text" id="twitter" name="twitter"/></div>
            <div><label for="web">Web: </label><input type="text" id="web" name="web"/></div>
            <div><input type="submit" value="Guardar"></div>
        </form>
        """

formularioPonente = """\
        <form action="/asistente" method="post">
            <div><label for="nombre">Nombre: </label><input type="text" id="nombre" name="nombre"/></div>
            <div><label for="apellidos">Apellidos: </label><input type="text" id="apellidos" name="apellidos"/></div>
            <div><label for="email">Email: </label><input type="text" id="email" name="email"/></div>
            <div><label for="telefono">Telefono: </label><input type="text" id="telefono" name="telefono"/></div>
            <div><label for="twitter">Twitter: </label><input type="text" id="twitter" name="twitter"/></div>
            <div><label for="web">Web: </label><input type="text" id="web" name="web"/></div>
            <div><input type="submit" value="Guardar"></div>
        </form>
        """

formularioEvento = """\
            <form action="/evento" method="post">
            <div><label for="nombre">Nombre del evento: </label><input type="text" id="nombre" name="nombre"/></div>
            <div><label for="hora">Hora: </label><input type="time" id="hora" name="hora"/></div>
            <div><label for="fecha">Fecha: </label><input type="date" id="fecha" name="fecha"/></div>
            <div><label for="descripcion">Descripcion: </label><input type="textbox" id="descripcion" name="descripcion"/></div>
            <div><label for="lugar">Lugar: </label><input type="text" id="lugar" name="lugar"/></div>
            <div><label for="asistencia">Tendra control de asistencia: </label>
            <input type="radio" id="asistenciaSi" name="asistencia" value = "Si"/>Si
            <input type="radio" id="asistenciaNo" name="asistencia" value = "No"/>No
            </div>
            <div><input type="submit" value="Guardar"></div>
            </form>
            """
formularioUsuario = """\
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


class Index(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render(template_values))

class InsertarAsistente(webapp2.RequestHandler):
    def get(self):
        self.response.write(formularioAsistente)

class InsertarEvento(webapp2.RequestHandler):
    def get(self):
        self.response.write(formularioEvento)

class InsertarOrganizacion(webapp2.RequestHandler):
    def get(self):
        self.response.write(formularioOrganizacion)

class InsetarPonente(webapp2.RequestHandler):
    def get(self):
        self.response.write(formularioPonente)

class InsertarUsuario(webapp2.RequestHandler):
    def get(self):
        self.response.write(formulario_usuario)

application = webapp2.WSGIApplication([
    ('/', Index),
    ('/iAsistente', InsertarAsistente),
    ('/iEvento', InsertarEvento)
    ('/iOrganizacion', InsertarOrganizacion),
    ('/iPonente', InsertarPonente)
    ('/iOrganizacion', InsertarOrganizacion),
    ('/iPonente', InsertarPonente)
    ('/iUsuario', InsertarUsuario)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
