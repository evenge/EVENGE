from google.appengine.api import mail


class emailEvenge(mail):
    sender = "Evenge <evenge-2014@appspot.gserviceaccount.com>"
    subject = " "

    contain = " "
    extra_css = " "
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
    def __init__():
        super().__init__()
