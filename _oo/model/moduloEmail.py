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
################################################################
"""Modulo para funciones de envio de email. Contiene funciones para envio automático de emails
       :author: Carlos Campos Fuentes | Francisco Javier Exposito Cruz | Ivan Ortega Alba | Victor Coronas Lara
       :version: 0.1 - 15/03/2015"""

from google.appengine.api import mail


def enviarConfirmacionLogin(usuario):
    message = mail.EmailMessage(sender="Evenge <evenge-2014@appspot.gserviceaccount.com>",
                                subject="Tu registro en Evenge ha sido satisfactorio")

    message.to = usuario.nombre + " " + usuario.apellidos + "<" + str(usuario.email) + ">"
    message.html = """
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="utf-8">
</head>

<body>
    <header><img src="https://evenge-2014.appspot.com/_dt/img/logo_white_50.png" alt="logo"><a href="evenge-2014.appspot.com" id="cabecera">EVENGE</a>
    </header>
    <div id="contain">
        <div id="cuerpo-texto">
            <strong>""" + usuario.nombre + " " + usuario.apellidos + """</strong>:

            <p> Su registro ha sido satisfactorio, ya puede acceder a su usuario: """ + str(usuario.email) + """</p>

            <p> Si necesitas cambiar algun dato, puedes hacerlo desde <strong>Mi cuenta</strong>.

                <p> Gracias por confiar en nosotros</p>
                <p><strong> Equipo Evenge</strong>
                </p>
        </div>
    </div>
    <style>
        header {
            width: 100%;
            background-color: #C11F23;
            height: 60px;
            font-size: 20px;
        }

        header img {
            margin-top: 10px;
            height: 40px;
            margin-left: 10px;
            margin-bottom: -10px;
        }

        header a {
            color: white;
            text-decoration: none;
        }

        #contain {
            background: white;
            height: 100%;
        }
        #cuerpo-texto{
            padding-left: 20px;
            padding: 20px;
        }
        body {
            font-family: verdana;
            font-size: 12px;
            background-color: #eee;
        }
    </style>
</body>

</html>
        """

    return message.send()
