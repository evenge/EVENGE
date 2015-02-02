# -*- coding: utf-8 -*-
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
from datetime import datetime

class Usuario(ndb.Model):
  nombre = ndb.StringProperty()
  apellidos = ndb.StringProperty()
  email = ndb.StringProperty()
  password = ndb.StringProperty()
  telefono = ndb.StringProperty()
  twitter = ndb.StringProperty()
  web = ndb.StringProperty()

class index(webapp2.RequestHandler):
    def post(self):
        usuario = Usuario()
        usuario.nombre = self.request.get('nombre')
        usuario.apellidos = self.request.get('apellidos')
        usuario.email = self.request.get('email')
        usuario.telefono = self.request.get('telefono')
        usuario.twitter = self.request.get('twitter')
        usuario.web = self.request.get('web')
        usuario.password = self.request.get('password')

        usuario.put()

        self.response.write('El usuario se ha creado correctamente.')

class ListarUsuarios(webapp2.RequestHandler):
    def get(self):
        result = Usuario.query()
        usuarios = []
        for usuario in result:
            usuarios.append(usuario)
        template_values = {'usuarios':usuarios}
        template = JINJA_ENVIRONMENT.get_template('/templates/templateUser.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/usuario', index),
    ('/listarUsuarios', ListarUsuarios)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
