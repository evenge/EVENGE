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
from google.appengine.api import users
from google.appengine.ext import ndb
from _oo.classes.evento import Evento

def GetEventoById(idEvento):
    result = Evento.get_by_id(int(idEvento))
    return result

def SetEvento(nombre, tipo, privado, idCreador, hora, fecha, lugar, coordenadas, descripcion, asistencia):
    evento = Evento()
    evento.nombre = nombre
    evento.tipo = tipo
    evento.privado = privado
    evento.idCreador = idCreador
    evento.hora = hora
    evento.fecha = fecha
    evento.lugar = lugar
    evento.coordenadas = coordenadas
    evento.descripcion = descripcion
    evento.asistencia = asistencia
    evento.put()
    return True
