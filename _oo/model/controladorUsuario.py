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
from _oo.classes.usuario import Usuario
from _oo.model import moduloEmail


def getKey(usuario):
    return usuario.key.id()


def nuevoRegistroUsuario(nombre,apellidos,email,telefono,twitter,web,password):
    usuario = Usuario()
    usuario.nombre = nombre
    usuario.apellidos = apellidos
    usuario.email = email
    usuario.telefono = telefono
    usuario.twitter = twitter
    usuario.web = web
    usuario.password = password
    print str(moduloEmail.enviarConfirmacionLogin(usuario))
    return usuario.put()

def loginCorrecto(email,password):
    usuario = Usuario.query(Usuario.email == email)

    if usuario.count():
        if(usuario.get().password == password):
            return usuario
        else:
            return False
    else:
        return False

def GetUsuarioById(idUsuario):
    return Usuario().get_by_id(idUsuario)

def getUsuarioLogeado(handler):
    if handler.request.cookies.get("logged") == "true":
        key = handler.request.cookies.get("key")
        usuario = GetUsuarioById(int(key))
        return usuario;
    else:
        return False

def listarUsuarios(self):
    result = Usuario.query()
    usuarios = []
    for usuario in result:
        usuarios.append(usuario)
    return usuarios
