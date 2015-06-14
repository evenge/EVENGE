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
"""Modulo de control de Eventos.Gestiona las operaciones realcionadas con los eventos.
   :author: Carlos Campos Fuentes | Francisco Javier Exposito Cruz | Ivan Ortega Alba | Victor Coronas Lara
   :version: 0.1"""
from google.appengine.ext import ndb
from _oo.classes.evento import Evento
from _oo.classes.asistente import Asistente
from datetime import datetime

"""
Este metodo devuelve un evento obtenido por su id
  :idEvento = id del evento que queremos
"""
def GetEventoById(idEvento):
    result = Evento.get_by_id(int(idEvento))
    return result

"""
Almacena un evento en el datastore
  :nombre = nombre del evento
  :tipo = tio del evento
  :privado = booleano True si el evento es privado, False si es publico
  :idCreador = id del creador del evento
  :hora = hora del evento
  :fecha = fecha del evento
  :lugar = lugar del evento
  :lat = latitud de la localizacion del evento
  :lon = longitud de la localizacion del evento
  :descripcion = descripcion del evento
  :asistencia = True si hay control de asistencia, False si no hay control de asistencia
"""
def SetEvento(nombre, tipo, privado, idCreador, hora, fecha, lugar, lat, lon, descripcion, asistencia):
    evento = Evento()
    evento.nombre = nombre
    evento.tipo = tipo
    evento.idCreador = str(idCreador)
    if privado == 'True':
        privado = True
    else:
        privado = False
    evento.privado = privado
    evento.hora = datetime.strptime(hora, "%H:%M").time()
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

"""
Edita un evento en el datastore
  :idE = ID del Evento a editar
  :nombre = Nuevo nombre
  :tipo = tipo del evento
  :privado = booleano True si el evento es privado, False si es publico
  :idCreador = id del creador del evento
  :hora = hora del evento
  :fecha = fecha del evento
  :lugar = lugar del evento
  :lat = latitud de la localizacion del evento
  :lon = longitud de la localizacion del evento
  :descripcion = descripcion del evento
  :asistencia = True si hay control de asistencia, False si no hay control de asistencia
"""
def updateEvento(idE, nombre, tipo, idCreador, privado, hora, fecha, lugar, coordenadas, descripcion, asistencia):
    evento = Evento().get_by_id(str(idE))
    evento.nombre = nombre
    evento.tipo = tipo
    evento.idCreador = str(idCreador)
    if privado == 'True':
        privado = True
    else:
        privado = False
    evento.privado = privado
    evento.hora = datetime.strptime(hora, "%H:%M").time()
    evento.fecha = datetime.strptime(fecha, "%Y-%m-%d")
    evento.lugar = lugar
    evento.coordenadas = coordenadas
    evento.descripcion = descripcion
    if privado == 'True':
        asistencia = True
    else:
        asistencia = False
    evento.asistencia = asistencia

    evento.put()

"""
Introduce un Asistente en un Evento
  :idEvento = id del evento donde queremos guardar el asistente
  :nom = nombre del asistente
  :ape = apellidos del asistente
  :tel = telefono del asistente
  :twi = twitter del asistente
  :dn = dni del asistente
"""
def setAsistente(idEvento, nom, ape, ema, tel, twi, dn):
    ev = Evento.get_by_id(int(idEvento))
    asistente = Asistente(nombre = nom, apellidos = ape, email = ema, telefono = tel, twitter = twi, dni = dn)
    ev.asistentes.append(asistente)
    ev.put()

"""
Devuelve los últimos eventos creados
  :num = Número de eventos a devolver
"""
def getUltimosEventos(num):
    eventos = Evento.query(Evento.fecha > datetime.now()).fetch(int(num))
    return eventos

"""
Devolver Asistentes de un evento.
  :idEvento = ID del evento
"""
def getAsistentesEvento(idEvento):
    asistentes = Asistente.query(Asistente.idEvento == str(idEvento))
    return asistentes

"""
Eliminar evento del datastore
  :idEvento = ID del evento
"""
def DeleteEvento(idEvento):
    evento = GetEventoById(int(idEvento))
    evento.key.delete()
    return True

"""
Agregar ponente a un evento.
  :idP = ID del ponente
  :idE = ID del evento
"""
def setPonente(idP, idE):
    evento = GetEventoById(int(idE))
    evento.ponentes.append(str(idP))
    evento.put()
