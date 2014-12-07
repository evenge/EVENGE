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

import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2
from google.appengine.ext import ndb
from datetime import datetime

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

        self.response.write('El ponente se ha creado correctamente')

class ListarPonentes(webapp2.RequestHandler):
    def get(self):
        result = Ponente.query()
        ponentes = []
        for ponente in result:
            ponentes.append(ponente)
        template_values = {'ponentes':ponentes}
        template = JINJA_ENVIRONMENT.get_template('/templates/mostrarPonentes.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/ponente', index),
    ('/listarPonentes', ListarPonentes)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
