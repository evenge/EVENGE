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

        self.response.write('La organizacion se ha creado correctamente')

class ListarOrganizaciones(webapp2.RequestHandler):
    def get(self):
        result = Organizacion.query()
        organizaciones = []
        for organizacion in result:
            organizaciones.append(organizacion)
        template_values = {'organizaciones':organizaciones}
        template = JINJA_ENVIRONMENT.get_template('/templates/mostrarOrganizaciones.html')
        self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([
    ('/organizacion', index),
    ('/listarOrganizaciones', ListarOrganizaciones)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
