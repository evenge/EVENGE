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
from _oo.classes.organizacion import Organizacion
import logging

def getKeyOrg(organizacion):
    return organizacion.getKey()
  
def SetOrganizacion(nombre, email, telefono, twitter, web):
    organizacion = Organizacion()
    organizacion.nombre = nombre
    organizacion.email = email
    organizacion.telefono = telefono
    organizacion.twitter = twitter
    organizacion.web = web

    return organizacion.put().id()
  
  
def SetUsuarioOrganizacion(idO, idU):
    uo = Organizacion().get_by_id(int(idO))
    uo.usuarios.append(idU)
    uo.put()
    
    return True


def GetOrganizacionUsuario(idUsuario):
    #logging.getLogger().setLevel(logging.DEBUG)
    orgs = Organizacion.query(ndb.AND(Organizacion.usuarios == idUsuario)).fetch(1)
    #logging.error(orgs)
    for o in orgs:
        return orgs

    return False
