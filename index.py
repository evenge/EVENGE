#Evenge - gestor de eventos (events management)
#Copyright (C) 2014 - desarrollo.evenge@gmail.com
#Carlos Campos Fuentes | Francisco Javier Expósito Cruz | Iván Ortega Alba | Victor Coronas Lara
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
################################################################
import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2

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
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/formAsistente.html')
        self.response.write(template.render(template_values))

class InsertarOrganizacion(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/formOrganizacion.html')
        self.response.write(template.render(template_values))

class InsertarEvento(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/formularioEvento.html')
        self.response.write(template.render(template_values))

class InsertarPonente(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/formPonente.html')
        self.response.write(template.render(template_values))

class InsertarUsuario(webapp2.RequestHandler):
    def get(self):
        self.response.write(formulario_usuario)

application = webapp2.WSGIApplication([
    ('/', Index),
    ('/iAsistente', InsertarAsistente),
    ('/iEvento', InsertarEvento),
    ('/iOrganizacion', InsertarOrganizacion),
    ('/iPonente', InsertarPonente),
    ('/iUsuario', InsertarUsuario)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
