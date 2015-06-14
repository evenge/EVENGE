# -*- coding: utf-8 -*-

# Evenge - gestor de eventos (events management)
# Copyright (C) 2014 - desarrollo.evenge@gmail.com
# Carlos Campos Fuentes | Francisco Javier Exposito Cruz | Ivan Ortega Alba | Victor Coronas Lara
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
################################################################
"""Modulo de inicio.Básicamente maneja las URL, renderiza la plantilla
correspondiente y pása los parametros a dicha plantilla. Cada clase corresponde
a una URL. Ver clase par más información.
   :author: Carlos Campos Fuentes | Francisco Javier Exposito Cruz | Ivan Ortega Alba | Victor Coronas Lara
   :version: 0.1"""

import os
import urllib
from google.appengine.ext import ndb
from _oo.classes.evento import Evento
from _oo.model import controladorEvento
from _oo.model import controladorUsuario
from _oo.model import controladorPonente
from _oo.model import controladorOrganizacion
from _oo.model import moduloEmail
import jinja2
import webapp2
import hashlib
import json
from datetime import datetime

"""Método utilizado para recabar la información del usuario
  :gravatar: utilizado el menu lateral
  :userLogin: utilizado para saber si accede un usuario logueado o un visitante
  :numeroEventos: numero de eventos del usuario logueado"""
def getInfo(self):
    #obtenemos el usuario logueado si lo esta
    user = controladorUsuario.getUsuarioLogeado(self)
    #creamos el diccionaro para las variables. Las inicializamos a False que serán su valor predeterminado
    info = {
      'gravatar': False,
      'userLogin': False,
      'numeroEventos': False,
      'numeroPonetes': False
    }
    #Comprobamos si el usuario está logueado o es False
    if user:
        info['numeroEventos'] = controladorUsuario.getEventosAsociadosCount(controladorUsuario.getKey(user))
        info['numeroPonentes'] = controladorUsuario.getPonentesAsociadosCount(controladorUsuario.getKey(user))
        info['userLogin'] = True
        info['gravatar'] = user.nombre[0:1] + user.apellidos[0:1]

    return info



class Index(webapp2.RequestHandler):
    """Es llamada por /"""
    def get(self):
        """
        Devuelve el index en función del logueo del usuario.
        Si está logueado devuelve la plantilla con todos sus eventos
        Si no está logueado devuelve un landpage de presentación
        """
        info = getInfo(self)
        usuario = controladorUsuario.getUsuarioLogeado(self)
        organizacion = False
        organizacionEventos = []

        if usuario:
            eventos = []
            evs = controladorUsuario.getEventosAsociados(usuario.key.id())
            for ev in evs:
                eventos.append(controladorEvento.GetEventoById(ev))
            for e in eventos:
                if len(e.descripcion) > 200:
                    sec = [e.descripcion[:200], '...']
                    e.descripcion = ''.join(sec)

            if usuario.organizacion:
                organizacion = True
                org = controladorOrganizacion.getOrganizacion(usuario.organizacion)
                for evo in org.eventos:
                    organizacionEventos.append(controladorEvento.GetEventoById(evo))
                for e in organizacionEventos:
                    if len(e.descripcion) > 200:
                        sec = [e.descripcion[:200], '...']
                        e.descripcion = ''.join(sec)

            template_values = {
              'eventos': eventos,
              'usuario': usuario,
              'info': info,
              'organizacion': organizacion,
              'eventosOrg': organizacionEventos
            }

            template = JINJA_ENVIRONMENT.get_template('templates/templateMyEvents.html')
            self.response.write(template.render(template_values))
        else:
            #Obtenemos los tres proximos eventos a partir de la fecha actual
            eventos = controladorEvento.getUltimosEventos(3)
            #Acortamos descripcion, titulo y lugar para ajustar los contenedores a la misma altura de manera elegante.
            for e in eventos:
                if len(e.descripcion) > 200:
                    sec = [e.descripcion[:200], '...']
                    e.descripcion = ''.join(sec)
                if len(e.nombre) > 35:
                    sec = [e.nombre[:35], '...']
                    e.nombre = ''.join(sec)
                if len(e.lugar) > 45:
                    sec = [e.lugar[:45], '...']
                    e.lugar = ''.join(sec)
            template_values = {'eventos': eventos}
            template = JINJA_ENVIRONMENT.get_template('templates/land.html')
            self.response.write(template.render(template_values))

class InsertarEvento(webapp2.RequestHandler):
    """Es llamada por /iEvento. """
    def get(self):
        """
        Desde llamada Get:
        Si el usuario está logueado se devuelve la plantilla con el formulario para crear el evento
        Si el usuario no está logueado se le redirige a /login
        """
        info = getInfo(self)
        user = controladorUsuario.getUsuarioLogeado(self)
        if user == False:
            self.redirect('/login')
        else:
            #Comprueba si el usuario pertenece a alguna organización
            orgId = controladorUsuario.getOrganizacion(str(controladorUsuario.getKey(user)))
            org = []
            if orgId:
                org = controladorOrganizacion.getOrganizacion(orgId)

            template_values = {
              'usuario': user,
              'organizacion': org,
              'info': info
            }
            template = JINJA_ENVIRONMENT.get_template('templates/templateNewEvent.html')
            self.response.write(template.render(template_values))

    def post(self):
        """
        Por POST recoge los datos del formulario del nuevo evento, y inserta en BD.
        """
        user = controladorUsuario.getUsuarioLogeado(self)
        idLogueado = str(controladorUsuario.getKey(user))
        nombre = self.request.get('nombre')
        hora = self.request.get('hora')
        fecha = self.request.get('fecha')
        descripcion = self.request.get('descripcion').strip()
        lugar = self.request.get('lugar')
        asistencia = self.request.get('asistencia')
        lat = self.request.get('latitud')
        lon = self.request.get('longitud')
        privado = self.request.get('privado')
        idCreador = self.request.get('idUser')
        userT = self.request.get('userT')

        ret = controladorEvento.SetEvento(nombre, userT, privado, idCreador, hora, fecha, lugar, lat, lon, descripcion, asistencia)

        if userT == '1':
            controladorUsuario.setEventoId(ret, idLogueado)
        else:
            controladorOrganizacion.setEventoId(ret, idCreador)

        # Aquí se avisaría por email
        resp = {'response': True, 'idEvento': ret}
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(resp))


class InsertarPonente(webapp2.RequestHandler):
    """Es llamada por /iPonente. """

    def get(self):
        """
        Desde llamada Get:
        Si el usuario está logueado se devuelve la plantilla con el formulario para crear un ponente
        Si el usuario no está logueado se le redirige a /login
        """
        info = getInfo(self)
        user = controladorUsuario.getUsuarioLogeado(self)
        if user is False:
            self.redirect('/login')
        else:

            template_values = {
              'info': info,
              'usuario': user
            }
            template = JINJA_ENVIRONMENT.get_template('templates/templatesNewPonente.html')
            self.response.write(template.render(template_values))

    def post(self):
        """Inserta un nuevo ponente con los datos recogidos"""
        user = controladorUsuario.getUsuarioLogeado(self)
        nombre = self.request.get("nombre").strip()
        apellidos = self.request.get("apellidos").strip()
        email = self.request.get("email").strip()
        telefono = self.request.get("tlf").strip()
        twitter = self.request.get("twitter").strip()
        web = self.request.get("web").strip()
        descripcion = self.request.get("descripcion").strip()
        guardar = self.request.get("guardar").strip()
        idNuevoPonente = controladorPonente.setPonente(nombre, apellidos, email, telefono, twitter, web, descripcion)
        controladorUsuario.setPonenteId(str(controladorUsuario.getKey(user)), idNuevoPonente)
        if str(guardar) == '1':
            controladorEvento.setPonente(idNuevoPonente, self.request.get("idEvento").strip())
        resp = {'response': True}
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(resp))



# class Evenge(webapp2.RequestHandler):
#     def hazElCuadrado(self, numero):
#         return numero*numero
#
#     def testPonente(self, ponente):
#         ponente.put()
#         query = Ponente.query(Ponente.email == 'pepito@jemail.com')
#         email = query.email
#         query.delete
#         return email
#
#     def testInsertarEvento(self, evento):
#         evt = evento
#         evt.put()
#         return True
#
#     def testInsertarUsuario(self, usuario):
#         u = usuario
#         u.put()
#         return True


class MostrarEvento(webapp2.RequestHandler):
    """Es llamada por /miseventos."""

    def get(self):
        """Pasa a plantilla un evento del usuario identificado por un id,
            recibido por GET en la variable idEvento.
            La información a la plantilla es:
            - objeto Evento
            - Usuario logueado : true o false
            - Usuario Creador
            - id del evento
            - numero de eventos del usuario
            - objeto Usuario (logeado en este momento)
            - asistentes : Vector de objetos Asistente, correspondiente al evento

        """
        info = getInfo(self)
        user = controladorUsuario.getUsuarioLogeado(self)
        idEvento = self.request.get('id')
        evento = controladorEvento.GetEventoById(idEvento)
        org = []
        organizadorNombre = []
        userCreador = False
        ponentes = []

        for p in evento.ponentes:
            ponentes.append(controladorPonente.getPonenteById(p))

        if user:
            if str(controladorUsuario.getKey(user)) == str(evento.idCreador):
                userCreador = True
            elif str(user.organizacion) == str(evento.idCreador):
                userCreador = True

        if evento.tipo == "1":
            organizador = controladorUsuario.getUsuarioById(evento.idCreador)
            organizadorNombre = organizador.nombre + ' ' + organizador.apellidos
        else:
            organizador = controladorOrganizacion.getOrganizacion(evento.idCreador)
            organizadorNombre = organizador.nombre

        template_values = {
          'evento': evento,
          'descripcion': evento.descripcion.replace("\n", "<br />"),
          'organizador': org,
          'organizadorNombre': organizadorNombre,
          'userCreador': userCreador,
          'usuario': user,
          'info': info,
          'ponentes': ponentes
        }

        template = JINJA_ENVIRONMENT.get_template('templates/templateEvents.html')
        self.response.write(template.render(template_values))


class MostrarInforme(webapp2.RequestHandler):
    """Es llamada por /misinformes."""

    def get(self):
        """
        Muestra la plantilla, por ahora sin datos, de la generación de informes.
        """
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/templateReports.html')
        self.response.write(template.render(template_values))


class MostrarMiCuenta(webapp2.RequestHandler):
    """Es llamada por /micuenta"""

    def get(self):
        """
        Devuelve la plantilla con los datos de usuario.
        Se pasan los datos:
            - objeto Usuario : usuario logueado
            - numeroEventos : numero de eventos activos de este usuario
        """
        info = getInfo(self)
        #Obtenemos si el usuario está logeado. En caso de no estarlo se redirección a otra
        usuario = controladorUsuario.getUsuarioLogeado(self)
        if usuario == False:
            self.redirect("/login")

        else:
            userLogin = True
            numeroEventos = controladorUsuario.getEventosAsociadosCount(controladorUsuario.getKey(usuario))
            #Obtenemos su organización en caso de pertenecer a una
            orgId = controladorUsuario.getOrganizacion(str(controladorUsuario.getKey(usuario)))
            org = []
            if orgId:
                org = controladorOrganizacion.getOrganizacion(orgId)

            template_values = {
              'usuario': usuario,
              'organizacion': org,
              'info': info
            }
            template = JINJA_ENVIRONMENT.get_template('templates/templateUser.html')
            self.response.write(template.render(template_values))


class MostrarMisEventos(webapp2.RequestHandler):
    """Es llamada por /miseventos"""

    def get(self):
        """
        Muestra TODOS los eventos asociados al usuario logueado en este momento.
        Se pasan los datos:
            - vector Eventos : Colección de todos los objeto Evento del usuario
        """
        info = getInfo(self)
        user = controladorUsuario.getUsuarioLogeado(self)
        organizacion = False
        organizacionEventos = []

        if user:
            eventos = controladorUsuario.getEventosAsociados(user.key.id())
            for e in eventos:
                if len(e.descripcion) > 200:
                    sec = [e.descripcion[:200], '...']
                    e.descripcion = ''.join(sec)

            if user.organizacion:
                organizacion = True
                org = controladorOrganizacion.getOrganizacion(user.organizacion)
                for evo in org.eventos:
                    organizacionEventos.append(controladorEvento.getEventoById(evo))

            template_values = {
              'eventos': eventos,
              'usuario': user,
              'info': info,
              'organizacion': organizacion,
              'eventosOrg': organizacionEventos
            }

            template = JINJA_ENVIRONMENT.get_template('templates/templateMyEvents.html')
            self.response.write(template.render(template_values))

        else:
            template = JINJA_ENVIRONMENT.get_template('templates/templateLogin.html')
            self.response.write(template.render(template_values))


class MostrarMisPonentes(webapp2.RequestHandler):

    def get(self):
        info = getInfo(self)
        user = controladorUsuario.getUsuarioLogeado(self)
        if user is False:
            self.redirect('/login')
        else:
            ponentesList = controladorUsuario.getPonentes(controladorUsuario.getKey(user))
            ponentes = []
            for p in ponentesList:
                ponentes.append(controladorPonente.getPonenteById(p))

            template_values = {
              'ponentes': ponentes,
              'info': info,
              'usuario': user
            }
            template = JINJA_ENVIRONMENT.get_template('templates/templatePonentes.html')
            self.response.write(template.render(template_values))


class MostrarError(webapp2.RequestHandler):
    """
    Es llamada por /miseventos
    """
    def get(self):
        """
        Muestra la página de error
        """
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/templateError.html')
        self.response.write(template.render(template_values))


class NuevoUsuario(webapp2.RequestHandler):
    """Es llamada por /registrate"""
    def get(self):
        """
        Muestra el formulario de registro de nuevo usuario
        """
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/templatesNewUser.html')
        self.response.write(template.render(template_values))

    def post(self):
        nombre = self.request.get("nombre").strip()
        apellidos = self.request.get("apellidos").strip()
        email = self.request.get("email").strip()
        telefono = self.request.get("telefono").strip()
        twitter = self.request.get("twitter").strip()
        ciudad = self.request.get("ciudad").strip()
        web = self.request.get("web").strip()
        password = self.request.get("contrasena").strip()
        idNuevoUsuario = controladorUsuario.nuevoRegistroUsuario(nombre, apellidos, email, telefono, twitter, web, password, ciudad)
        self.redirect('/')


class Login(webapp2.RequestHandler):
    """ Es llamada por /login"""

    def get(self):
        """
        Muestra el formulario de login
        """
        if (self.request.get("login")):
            template_values = {'error':True}
        else:
            template_values = {}
        template = JINJA_ENVIRONMENT.get_template('templates/templateLogin.html')
        self.response.write(template.render(template_values))

    def post(self):
        """
        Recibe el usuario y contraseña y comprueba que el login es correcto
        Si lo es, añade las cookies y queda iniciada la sesión
        """
        contrasena = self.request.get("contrasena").strip()
        logeado = controladorUsuario.loginCorrecto(self.request.get("email").strip(), contrasena)

        if logeado is not False:
            logeado = logeado.get()
            self.response.headers.add_header('Set-Cookie', "logged=true")
            self.response.headers.add_header('Set-Cookie', "email=" + str(logeado.email))
            self.response.headers.add_header('Set-Cookie', "key=" + str(logeado.key.id()))
            self.redirect("/")
        else:
            self.redirect("/login?login=error")


class Logout(webapp2.RequestHandler):
    """Es llamada por /logout"""

    def get(self):
        """
        Elimina las cookies relacionadas y queda cerrada la sesión
        """
        if self.request.cookies.get("logged") == "true":
            self.response.headers.add_header('Set-Cookie', "logged=; Expires=Thu, 01-Jan-1970 00:00:00 GMT")
            self.response.headers.add_header('Set-Cookie', "email=; Expires=Thu, 01-Jan-1970 00:00:00 GMT")
            self.response.headers.add_header('Set-Cookie', "key=; Expires=Thu, 01-Jan-1970 00:00:00 GMT")

        self.redirect("/")


class EliminarEvento(webapp2.RequestHandler):
    """Es llamada por /eliminarEvento"""

    def post(self):
        """
        Recibe el id del evento a borrar por post, y lo borra de la BD
        """
        user = controladorUsuario.getUsuarioLogeado(self)
        idEvento = self.request.get('id')
        if user is False:
            self.redirect("/")
        else:
            ret = controladorEvento.DeleteEvento(idEvento)
            resp = {'response': ret}
            self.response.headers['Content-Type'] = 'application/json'
            self.response.write(json.dumps(resp))


class CrearOrganizacion(webapp2.RequestHandler):
    """Es llamada por /iOrganización"""

    def post(self):
        """
        Recibe los datos de la nueva organización, la crea e inscribe al usuario.
        """
        user = controladorUsuario.getUsuarioLogeado(self)

        if user is False:
            self.response.write(json.dumps({'reponse': 'false'}))
        else:
            nombre = self.request.get('nombre').strip()
            mail = self.request.get('email').strip()
            twitter = self.request.get('twitter').strip()
            tel = self.request.get('telefono').strip()
            web = self.request.get('web').strip()
            idOrganizacion = controladorOrganizacion.setOrganizacion(nombre, mail, tel, twitter, web)
            controladorOrganizacion.setUsuarioOrganizacion(idOrganizacion, user.key.id())
            controladorUsuario.setOrganizacion(idOrganizacion, user.key.id())

            self.response.write(json.dumps({'reponse': 'true'}))

class InsertarAsistente(webapp2.RequestHandler):
    """Es llamada por /iAsistente"""
    def post(self):
        iEv = self.request.get('id').strip()
        nombre = self.request.get('nombre').strip()
        apellidos = self.request.get('apellidos').strip()
        email = self.request.get('email').strip()
        telefono = self.request.get('telefono').strip()
        twitter = self.request.get('twitter').strip()
        dni = self.request.get('dni').strip()

        controladorEvento.setAsistente(iEv, nombre, apellidos, email, telefono, twitter, dni)
        self.response.write(json.dumps({'reponse': 'true'}))

#Urls
class ModificarPonente(webapp2.RequestHandler):

    def get(self):
        info = getInfo(self)
        user = controladorUsuario.getUsuarioLogeado(self)
        idPonente = self.request.get('id')
        p = []

        if user == False:
            self.redirect('/login')

        else:
            if str(idPonente) in user.ponentes:
                p = controladorPonente.getPonenteById(idPonente)

            elif user.organizacion:
                o = controladorOrganizacion.getOrganizacion(user.organizacion)
                if str(idPonente) in o.ponentes:
                    p = controladorPonente.getPonenteById(idPonente)

            else:
                self.redirect('/')

            template_values = {
              'usuario': user,
              'info': info,
              'ponente': p
            }

            template = JINJA_ENVIRONMENT.get_template('templates/templateModificarPonente.html')
            self.response.write(template.render(template_values))

    def post(self):
        nombre = self.request.get("nombre").strip()
        apellidos = self.request.get("apellidos").strip()
        email = self.request.get("email").strip()
        telefono = self.request.get("tlf").strip()
        twitter = self.request.get("twitter").strip()
        web = self.request.get("web").strip()
        descripcion = self.request.get("descripcion").strip()
        idPonente = self.request.get("idPonente").strip()
        controladorPonente.updatePonente(nombre, apellidos, email, telefono, twitter, web, descripcion, idPonente)

        resp = {'response': True}
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(resp))


class MostrarCuenta(webapp2.RequestHandler):
    def get(self):
        info = getInfo(self)
        user = controladorUsuario.getUsuarioLogeado(self)
        idCuenta = self.request.get('id')
        cuenta = controladorUsuario.getUsuarioById(idCuenta)
        o = []
        eventosU = []

        if cuenta == False:
            self.redirect('/login')
        else:
            for ide in cuenta.eventos:
                eventosU.append(controladorEvento.GetEventoById(ide))
            for e in eventosU:
                if len(e.descripcion) > 200:
                    sec = [e.descripcion[:200], '...']
                    e.descripcion = ''.join(sec)

            if cuenta.organizacion:
                o = controladorOrganizacion.getOrganizacion(cuenta.organizacion)

            template_values = {
              'usuario': user,
              'info': info,
              'cuenta': cuenta,
              'organizacion': o,
              'eventosU': eventosU,
            }

            template = JINJA_ENVIRONMENT.get_template('templates/templateCuenta.html')
            self.response.write(template.render(template_values))


class InvitacionOrganizacion(webapp2.RequestHandler):
    def get(self):
        idOrg = self.request.get('id')
        email = self.request.get('email')
        user = controladorUsuario.getUsuarioLogeado(self)

        if not user:
            self.redirect('/login')
        else:
            if str(user.email) != str(email):
                self.redirect('/error')
            else:
                controladorOrganizacion.deleteInvitacion(idOrg, email)
                controladorOrganizacion.setUsuarioOrganizacion(idOrg, user.getKey())
                controladorUsuario.setOrganizacion(idOrg, user.getKey())
                self.redirect('/micuenta')


    def post(self):
        idOrg = self.request.get('idOrg')
        email = self.request.get('email')
        fechaInv = controladorOrganizacion.createInvitacion(idOrg, email)

        o = controladorOrganizacion.getOrganizacion(idOrg)
        contain = "http://evenge-2014.appspot.com/invitacion?id="+idOrg+"?email="+email

        moduloEmail.enviarEmail("8macau8@gmail.com","Has sido invitado a unirte a una organización",contain)
        resp = {
          'response': 'true',
          'fecha': str(fechaInv)
        }
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(resp))

class SubirImagenUsuario(webapp2.RequestHandler):
    def post(self):
        user = controladorUsuario.getUsuarioLogeado(self)
        img = self.request.get("imgU")
        controladorUsuario.setImage(img, user.getKey())

class GetImagenUsuario(webapp2.RequestHandler):
    def get(self):
        idU = self.request.get('id')
        tipo = self.request.get('tipo')
        avatar = []
        if tipo == "1":
            avatar = controladorUsuario.getUsuarioById(idU).avatar
        elif tipo == "2":
            avatar = controladorOrganizacion.getOrganizacion(idU).avatar
        else:
            avatar = controladorPonente.getPonente(idU).avatar

        self.response.headers['Content-Type'] = "image/png"
        self.response.out.write(avatar)


application = webapp2.WSGIApplication([
    ('/', Index),
    ('/iEvento', InsertarEvento),
    ('/iPonente', InsertarPonente),
    ('/miseventos', Index),
    ('/eventos*', MostrarEvento),
    ('/misponentes', MostrarMisPonentes),
    ('/misinformes', MostrarInforme),
    ('/micuenta', MostrarMiCuenta),
    ('/registrate', NuevoUsuario),
    ('/login', Login),
    ('/logout', Logout),
    ('/eliminarEvento', EliminarEvento),
    ('/iOrganizacion', CrearOrganizacion),
    ('/iAsistente', InsertarAsistente),
    ('/mPonente*', ModificarPonente),
    ('/cuenta*', MostrarCuenta),
    ('/invitacion*', InvitacionOrganizacion),
    ('/uImagenUsuario', SubirImagenUsuario),
    ('/gImagenUsuario', GetImagenUsuario),
    ('/.*', MostrarError)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
