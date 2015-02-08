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

def nuevoRegistroUsuario(nombre,apellidos,email,telefono,twitter,web,password):
    usuario = Usuario()
    usuario.nombre = nombre
    usuario.apellidos = apellidos
    usuario.email = email
    usuario.telefono = telefono
    usuario.twitter = twitter
    usuario.web = web
    usuario.password = password
    #Devuelve la key
    return usuario.put()

def loginCorrecto(email,password):
    usuario = Usuario.query(Usuario.email == email)

    if usuario.count():
        if(usuario.get().password == password):
            return usuario
        else:
            return 0
    else:
        return 0

def GetUsuarioById(idUsuario):
    return Usuario().get_by_id(idUsuario)
