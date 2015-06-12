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


"""Crea el HTML del cuerpo del email usando como plantilla el correo estandar Evenge
  :contain: Contenido del mensaje excluyendo la cabecera y el estilo contenido en la plantilla.
  :extra_css: Css correspondiente al contenido del mensaje.
  """
def makeCuerpo(contain,extra_css):
    esqueleto = """<!DOCTYPE html>
    <html lang="es">

    <head>
        <meta charset="utf-8">
    </head>

    <body>
        <header><img src="https://evenge-2014.appspot.com/_dt/img/logo_white_50.png" alt="logo"><a href="evenge-2014.appspot.com" id="cabecera">EVENGE</a>
        </header>
        <div id="contain">
            <div id="cuerpo-texto">
                    """ + contain + """
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
            """ + extra_css + """
        </style>
    </body>

    </html>
            """
    return esqueleto


"""Envio de Emails con Evenge como sender
  :to: "Alias <email>". Nombre del receptor e email.
  :subject: Asunto del mensaje
  :contain: HTML del cuerpo del mensaje
  :extra_css: css correspondiente al cuerpo del mensaje
  """
def enviarEmail(to,subject,contain,extra_css=""):
    message = mail.EmailMessage(sender="Evenge <evenge-2014@appspot.gserviceaccount.com>",
                                subject=subject)
    message.to = to
    message.html = makeCuerpo(contain,extra_css)
    return message.send()


"""Envio de confirmación de registro por email
  :usuario: objeto Usuario con los datos del usuario al que se va a enviar el email
  """
def enviarConfirmacionLogin(usuario):
    subject="Tu registro en Evenge ha sido satisfactorio"
    to = usuario.nombre + " " + usuario.apellidos + "<" + str(usuario.email) + ">"
    message = """
    <strong>""" + usuario.nombre + " " + usuario.apellidos + """</strong>:

    <p> Su registro ha sido satisfactorio, ya puede acceder a su usuario: """ + str(usuario.email) + """</p>

    <p> Si necesitas cambiar algun dato, puedes hacerlo desde <strong>Mi cuenta</strong>.
    """

    return enviarEmail(to,subject,message)
