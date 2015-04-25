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

class Asistente(ndb.Model):
    idEvento = ndb.StringProperty()
    nombre = ndb.StringProperty()
    apellidos = ndb.StringProperty()
    email = ndb.StringProperty()
    telefono = ndb.StringProperty()
    twitter = ndb.StringProperty()
    dni = ndb.StringProperty()
    asistido = ndb.BooleanProperty()

class index(webapp2.RequestHandler):
    def post(self):
        asistente = Asistente()
        asistente.idEvento = self.request.get("idEvento")
        asistente.nombre = self.request.get('nombre')
        asistente.apellidos = self.request.get('apellidos')
        asistente.email = self.request.get('email')
        asistente.telefono = self.request.get('telefono')
        asistente.twitter = self.request.get('twitter')
        asistente.dni = self.request.get('dni')
        asistente.asistido = False

        asistente.put()

        self.redirect("/eventos?id=" + str(asistente.idEvento))

class ListarAsistentes(webapp2.RequestHandler):
    def get(self):
        result = Asistente.query()
        asistentes = []
        for t in result:
            asistentes.append(t)
        template_values = {'asistentes':asistentes}
        template = JINJA_ENVIRONMENT.get_template('/templates/mostrarAsistentes.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/asistente', index),
    ('/listarAsistentes', ListarAsistentes)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
