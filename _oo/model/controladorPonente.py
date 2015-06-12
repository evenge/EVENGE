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
from google.appengine.ext import ndb
from _oo.classes.ponente import Ponente


def getKey(ponente):
    return ponente.key.id()

def setPonente(nombre, apellidos, email, telefono, twitter, web, descripcion):
    ponente = Ponente()
    ponente.nombre = nombre
    ponente.apellidos = apellidos
    ponente.email = email
    ponente.telefono = telefono
    ponente.twitter = twitter
    ponente.web = web
    ponente.descripcion = descripcion
    #Devuelve la key
    return ponente.put().id()

def getPonenteById(idPonente):
    return Ponente().get_by_id(int(idPonente))

def listarPonentes(self):
    result = Ponente.query()
    ponentes = []
    for ponente in result:
        ponentes.append(ponente)
    return ponentes
