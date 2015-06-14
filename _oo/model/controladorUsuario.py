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

import os
import urllib
import webapp2
from google.appengine.ext import ndb
from google.appengine.api import images
from _oo.classes.usuario import Usuario
from _oo.model import moduloEmail
import logging
import md5


def getKey(usuario):
    return usuario.key.id()


def nuevoRegistroUsuario(nombre, apellidos, email, telefono, twitter, web, password, ciudad):
    usuario = Usuario()
    usuario.nombre = nombre
    usuario.apellidos = apellidos
    usuario.email = email
    usuario.telefono = telefono
    usuario.ciudad = ciudad
    usuario.twitter = twitter
    usuario.web = web
    usuario.password = md5.new(password).hexdigest()
    print str(moduloEmail.enviarConfirmacionLogin(usuario))
    return usuario.put()


def loginCorrecto(email,password):
    usuario = Usuario.query(Usuario.email == email)

    if usuario.count():
        if(usuario.get().password == md5.new(password).hexdigest()):
            return usuario
        else:
            return False
    else:
        return False


def getUsuarioById(idUsuario):
    return Usuario().get_by_id(int(idUsuario))


def getUsuarioLogeado(handler):
    if handler.request.cookies.get("logged") == "true":
        key = handler.request.cookies.get("key")
        usuario = getUsuarioById(int(key))
        return usuario;
    else:
        return False

def listarUsuarios(self):
    result = Usuario.query()
    usuarios = []
    for usuario in result:
        usuarios.append(usuario)
    return usuarios


def getEventosAsociados(idUsuario):
    eventos = getUsuarioById(idUsuario).eventos
    return eventos


def getEventosAsociadosCount(idUsuario):
    cont = len(getEventosAsociados(idUsuario))
    if cont == False:
        return 0
    return cont

def setEventoId(idEvento, idU):
    u = getUsuarioById(int(idU))
    u.eventos.append(str(idEvento))
    u.put()

def setPonenteId(idU, idP):
    u = getUsuarioById(int(idU))
    u.ponentes.append(str(idP))
    u.put()

def getPonentesAsociadosCount(idU):
    cont = len(getPonentes(idU))
    if cont == False:
        return 0
    return cont

def getPonentes(idU):
    u = getUsuarioById(int(idU))
    return u.ponentes

def setOrganizacion(idO, idU):
    u = getUsuarioById(int(idU))
    u.organizacion = str(idO)
    u.put()

def getOrganizacion(idU):
    u = getUsuarioById(int(idU))
    logging.getLogger().setLevel(logging.DEBUG)
    if not u:
        logging.error(len(u.organizacion))
        return False

    return u.organizacion


def setImage(img, idU):
    u = getUsuarioById(int(idU))
    img = images.resize(img, 150, 150)
    u.avatar = img
    u.put()

def modificarUsuario(nombre, apellidos, telefono, twitter, web, ciudad, idU):
    u = getUsuarioById(int(idU))
    u.nombre = nombre
    u.apellidos = apellidos
    u.telefono = telefono
    u.ciudad = ciudad
    u.twitter = twitter
    u.web = web
    u.put()
