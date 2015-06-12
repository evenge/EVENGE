# -*- coding: utf-8 -*-
#Evenge - gestor de eventos (events management)
#Copyright (C) 2014 - desarrollo.evenge@gmail.com
#Carlos Campos Fuentes | Francisco Javier Expósito Cruz | Iván Ortega Alba | Victor Coronas Lara
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
from google.appengine.api import users
from google.appengine.ext import ndb
from datetime import datetime

class Usuario(ndb.Model):
    nombre = ndb.StringProperty()
    apellidos = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty(indexed=False)
    telefono = ndb.StringProperty(indexed=False)
    twitter = ndb.StringProperty(indexed=False)
    web = ndb.StringProperty(indexed=False)
    eventos = ndb.StringProperty(repeated=True)
    ponentes = ndb.StringProperty(repeated=True)
    organizacion = ndb.StringProperty()

    def getKey(self):
        return str(self.key.id())
