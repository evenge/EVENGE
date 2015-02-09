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

from google.appengine.api import users
from google.appengine.ext import ndb
from _oo.classes.evento import Evento
from datetime import datetime

def GetEventoById(idEvento):
    result = Evento.get_by_id(int(idEvento))
    return result

def SetEvento(nombre, tipo, privado, idCreador, hora, fecha, lugar, lat, lon, descripcion, asistencia):
    evento = Evento()
    evento.nombre = nombre
    evento.tipo = int(tipo)
    if privado == 'True':
      privado = True
    else:
      privado = False
    evento.privado = privado
    evento.idCreador = idCreador
    evento.hora = datetime.strptime(hora,"%H:%M").time()
    evento.fecha = datetime.strptime(fecha, "%Y-%m-%d")
    evento.lugar = lugar
    evento.coordenadas = ndb.GeoPt(lat, lon)
    evento.descripcion = descripcion
    if privado == 'True':
        asistencia = True
    else:
        asistencia = False
    evento.asistencia = asistencia

    return evento.put().id()

def getEventosAsociados(idUsuario):
    eventos = Evento.query(Evento.idCreador == str(idUsuario));
    return eventos;

def getEventosAsociadosCount(idUsuario):
    return getEventosAsociados(idUsuario).count()

def DeleteEvento(idEvento):
    evento = GetEventoById(int(idEvento))
    evento.key.delete()
    return True
