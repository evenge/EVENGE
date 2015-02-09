# -*- coding: utf-8 -*-

#Evenge - gestor de eventos (events management)
#Copyright (C) 2014 - desarrollo.evenge@gmail.com
#Carlos Campos Fuentes | Francisco Javier Exposito Cruz | Ivan Ortega Alba | Victor Coronas Lara
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
from _oo.classes.evento import Evento
from _oo.model import controladorEvento
from _oo.model import controladorUsuario
import jinja2
import webapp2
import hashlib
import json

class Index(webapp2.RequestHandler):
    def get(self):
        usuario = controladorUsuario.getUsuarioLogeado(self)
        if usuario :
            template_values = {'usuario':usuario}
            template = JINJA_ENVIRONMENT.get_template('templates/templateMyEvents.html')
            self.response.write(template.render(template_values))
        else:
            template_values = {}
            template = JINJA_ENVIRONMENT.get_template('templates/indexVisitante.html')
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
        template = JINJA_ENVIRONMENT.get_template('templates/templateNewEvent.html')
        self.response.write(template.render(template_values))

    def post(self):
        nombre = self.request.get('nombre')
        hora = self.request.get('hora')
        fecha = self.request.get('fecha')
        ca = self.request.get('cantidadAsistentes')
        descripcion = self.request.get('descripcion')
        lugar = self.request.get('lugar')
        asistencia = self.request.get('asistencia')
        lat = self.request.get('latitud')
        lon = self.request.get('longitud')
        privado = self.request.get('privado')
        ret = controladorEvento.SetEvento(nombre, 1, privado, '1111', hora, fecha, lugar, lat, lon, descripcion, asistencia);
        resp = {'response': ret}
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(resp))


class InsertarPonente(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/formPonente.html')
        self.response.write(template.render(template_values))

class Evenge(webapp2.RequestHandler):
    def hazElCuadrado(self, numero):
        return numero*numero

    def testPonente(self, ponente):
        ponente.put()
        query = Ponente.query(Ponente.email == 'pepito@jemail.com')
        email = query.email
        query.delete
        return email

    def testInsertarEvento(self, evento):
        evt = evento
        evt.put()
        return True

    def testInsertarUsuario(self, usuario):
        u = usuario
        u.put()
        return True

class MostrarEvento(webapp2.RequestHandler):
    def get(self):
        idEvento = self.request.get('id')
        evento = controladorEvento.GetEventoById(idEvento)
        template_values = {'evento':evento}
        template = JINJA_ENVIRONMENT.get_template('templates/templateEvents.html')
        self.response.write(template.render(template_values))

class MostrarInforme(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/templateReports.html')
        self.response.write(template.render(template_values))

class MostrarMiCuenta(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/templateUser.html')
        self.response.write(template.render(template_values))

class MostrarMisEventos(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/templateMyEvents.html')
        self.response.write(template.render(template_values))

class MostrarError(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/templateError.html')
        self.response.write(template.render(template_values))

class NuevoUsuario(webapp2.RequestHandler):

    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/templatesNewUser.html')
        self.response.write(template.render(template_values))
    def post(self):
        nombre = self.request.get("nombre").strip()
        apellidos = self.request.get("apellidos").strip()
        email = self.request.get("email").strip()
        telefono = self.request.get("telefono").strip()
        twitter = self.request.get("twitter").strip()
        web = self.request.get("web").strip()
        password = self.request.get("contrasena").strip()
        idNuevoUsuario = controladorUsuario.nuevoRegistroUsuario(
            nombre,apellidos,
            email,telefono,
            twitter,web,
            password)
        self.redirect('/')

class Login(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/templateLogin.html')
        self.response.write(template.render(template_values))
    def post(self):
        contrasena = self.request.get("contrasena").strip()
        logeado = controladorUsuario.loginCorrecto(self.request.get("email").strip(),contrasena)

        if logeado != 0:
            logeado = logeado.get()
            self.response.headers.add_header('Set-Cookie',"logged=true")
            self.response.headers.add_header('Set-Cookie',"email="+str(logeado.email))
            self.response.headers.add_header('Set-Cookie',"key="+str(logeado.key.id()))
            self.redirect("/")
        else:
            self.redirect("/login")

class Logout(webapp2.RequestHandler):
    def get(self):
        if self.request.cookies.get("logged") == "true":
            self.response.headers.add_header('Set-Cookie',"logged=; Expires=Thu, 01-Jan-1970 00:00:00 GMT")
            self.response.headers.add_header('Set-Cookie',"email=; Expires=Thu, 01-Jan-1970 00:00:00 GMT")
            self.response.headers.add_header('Set-Cookie',"key=; Expires=Thu, 01-Jan-1970 00:00:00 GMT")

        self.redirect("/")

application = webapp2.WSGIApplication([
    ('/', Index),
    ('/iAsistente', InsertarAsistente),
    ('/iEvento', InsertarEvento),
    ('/iOrganizacion', InsertarOrganizacion),
    ('/iPonente', InsertarPonente),
    ('/miseventos', MostrarMisEventos),
    ('/eventos*', MostrarEvento),
    ('/misinformes', MostrarInforme),
    ('/micuenta', MostrarMiCuenta),
    ('/registrate', NuevoUsuario),
    ('/login', Login),
    ('/logout', Logout),
    ('/error', MostrarError)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
