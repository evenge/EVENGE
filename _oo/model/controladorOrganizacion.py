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

from google.appengine.ext import ndb
from google.appengine.api import images
from _oo.classes.organizacion import Organizacion
from _oo.classes.invitacion import Invitacion
import logging

def getKeyOrg(organizacion):
    return organizacion.getKey()
  
def setOrganizacion(nombre, email, telefono, twitter, web):
    organizacion = Organizacion()
    organizacion.nombre = nombre
    organizacion.email = email
    organizacion.telefono = telefono
    organizacion.twitter = twitter
    organizacion.web = web

    return organizacion.put().id()
  
  
def setUsuarioOrganizacion(idO, idU):
    uo = Organizacion().get_by_id(int(idO))
    uo.usuarios.append(str(idU))
    uo.put()


def getOrganizacion(idO):
    #logging.getLogger().setLevel(logging.DEBUG)
    org = Organizacion.get_by_id(int(idO))
    #logging.error(orgs)
    return org

def setEventoId(idE, idO):
    o = Organizacion().get_by_id(int(idO))
    o.eventos.append(str(idE))
    o.put()

def createInvitacion(idO, ema):
    o = Organizacion().get_by_id(int(idO))
    o.invitaciones.append(Invitacion(email=ema))
    o.put()
    return o.invitaciones[-1].fecha

def deleteInvitacion(idO, ema):
    o = Organizacion().get_by_id(int(idO))
    for inv in o.invitaciones:
        if inv.email == ema:
            o.invitaciones.remove(inv)

def setImage(img, idO):
    o = Organizacion().get_by_id(int(idO))
    img = images.resize(img, 150, 150)
    o.avatar = img
    o.put()

