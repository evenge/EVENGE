<!--
Evenge - gestor de eventos (events management)
Copyright (C) 2014 - desarrollo.evenge@gmail.com
Carlos Campos Fuentes | Francisco Javier Expósito Cruz | Iván Ortega Alba | Victor Coronas Lara

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
-->

# EVENGE
###### Gestor de eventos

**Evenge** es un sistema de **gestión automática de eventos** con inclusión en diferentes blog (Wordpress, Blogspot), correo electrónico y redes sociales.  

Evenge dispone de las siguientes funcionalidades:  
* Calendario
* Creación de eventos
* Registro de ponentes
* Control de asistencia
* Generación de diplomas
* Registro del número de personas que han asistido
* Generación de informes sobre los eventos: lugar, asistencia.

#### Desarrolladores:

* [Carlos Campos Fuentes](http://github.com/ccamposfuentes)
* [Iván Ortega Alba](http://github.com/ivanortegaalba)
* [Francisco Javier Expósito Cruz](http://github.com/franexposito)
* [Victor Coronas Lara](http://github.com/VictorCoronas)

-------------------------
**Aplicación**: [evenge-2014.appspot.com](https://evenge-2014.appspot.com)  
**Email**: [desarrollo.evenge@gmail.com](mailto://desarrolo.evenge@gmail.com)  
**Blog**: [evenge.github.io](http://evenge.github.io)  
**Twitter**: [@grupoEvenge](https://twitter.com/grupoEvenge)  
**Entorno de desarrollo**: [Docker](https://registry.hub.docker.com/u/ivanortegaalba/evenge/)

-------------------------

# Documentación:

  - [Provisionamiento](https://github.com/evenge/EVENGE/blob/master/docs/dockerfile.md)
  - [Integración continua](https://github.com/evenge/EVENGE/blob/master/docs/integracion-continua.md)
  - [Testeo](https://github.com/evenge/EVENGE/blob/master/docs/Testeo.md)
  - [Despliegue de la aplicación](https://github.com/evenge/EVENGE/blob/master/docs/despliegue-aplicacion.md)

-------------------------
## Provisionamiento  
###Docker
[Docker](https://www.docker.com/) es un una plataforma para desarrolladores y administradores de sistema que te permite desarrollar, desplegar y ejecutar aplicaciones. Docker permite testear el codigo y desplegarlo en producción rápidamente.  

####Introducción
En Evenge hemos decidido automatizar el proceso de instalación del docker mediante [este](https://github.com/evenge/EVENGE/blob/master/despliegue/Dockerfile) script.

####Docker
######Explicando el script
En primer lugar tendremos que instalar las depencencias de python que necesitamos:

* Python
* Python setuptools
* [Pip](https://pypi.python.org/pypi/pip/)
* Python build-essential
* wget
* zip

```
RUN apt-get update && apt-get install -y python
RUN apt-get install -y python-setuptools
RUN easy_install pip
RUN apt-get install -y python-dev build-essential
RUN apt-get install -y wget
RUN apt-get install -y zip
```

Después tendremos que instalar los distintos frameworks que vamos a usar en el desarrollo de nuestra aplicación. En nuestro caso son dos:

* webapp2
* jinja

Los motivos de porque hemos usado estos frameworks están mejor detallados [aqui](http://evenge.github.io/general/2014/12/16/uso-de-webapp2-y-jinja2/).

```
RUN pip install webapp2
RUN pip install jinja2
```

El siguiente paso es descargar el SDK de GAE y descomprimirlo:

```
RUN wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.17.zip --no-check-certificate
RUN unzip google_appengine_1.9.17.zip
```

Tras descargar y descomprimir el SDK de GAE nos toca instalar el google-cloud-sdk y configurar el proyecto Evenge:

```
RUN curl -sSL https://sdk.cloud.google.com | bash
RUN gcloud auth login
RUN gcloud config set project <google-cloud-project-id>
```

El último paso es instalar git y clonar nuestro repostorio:

```
RUN apt-get install -y git
RUN git clone https://github.com/evenge/EVENGE.git
RUN cd EVENGE && git branch -b $USER
```

Una vez realizados todos los pasos tendremos desplegado nuestro entorno de desarrollo.


####Script de automatización de Docker
######Introducción
También hemos hecho un Script que automatiza el proceso de instalación de Docker. A continuación la explicación paso a paso.

######Explicación del script
En primer lugar, se instala Docker y las dependencias necesarias:

```
su -c 'apt-get update
apt-get install -y docker.io
source /etc/bash_completion.d/docker.io
[ -e /usr/lib/apt/methods/https ] || {
  apt-get update
  apt-get install -y apt-transport-https
}
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
sh -c "echo deb https://get.docker.com/ubuntu docker main\
> /etc/apt/sources.list.d/docker.list"
apt-get update
apt-get install -y lxc-docker
```

Tras esto nos descargamos la imagen producida con el Dockerfile y la ejecutamos:

```
docker pull ivanortegaalba/evenge
docker run -t -i ivanortegaalba/evenge /bin/bash'
```


-------------------------
## Integración continua  
Para provisionar nuestro proyecto con integración continua barajamos varias posibilidades.

1. La sincronización directa con GitHub que nos provee GAE.
Simplemente con añadir el repo donde tenemos el código, GAE sincroniza la app con el, y cuando se realice un push, se hará el despliegue automático.
Esto es factible, si y solo si tenemos unicamente el código de la aplicación el el repo.
Pero nosotros tenemos documentación, lista de tareas, etc. Por lo que no nos valía.

2. La segunda opción, y por la que nos decantamos finalmente, fue el despliegue por Shippable.
Este sistema de CI permite crear, provisionar, testear y desplegar nuestra app en una máquina virtual, en el servidor que queramos.
Además trabaja con IaaS y PaaS como Heroku, Amazon Elastic Beanstalk, OpsWorks AWS, Google App Engine, Red Hat OpenShift o cualquier proveedor de infraestructura después de una compilación exitosa.

### Shippable
#### Introduccion

Shippable usa Docker para el despliegue de las apps.
Sus casos de uso más comunes, y concretamente los que vamos a darle en el proyecto son:
- Automatización del empaquetado y despliegue de web apps.
- Testeo automatizado y despliegue en caso de éxito.

#### Configurar Shippable para Evenge.

Primeramente, desde www.shipable.com, nos logeamos y conectamos con nuestro GitHub. Podemos seguir este [tutorial](http://docs.shippable.com/en/latest/start.html#getstarted)

Una vez, tenemos ya sincronizado nuestro repo, desde Shippable vamos a crear nuestro YML que irá en función a la plataforma donde vayamos a hacer el despliegue.
En nuestro caso, GAE, Shippable nos proporciona este [tutorial](http://docs.shippable.com/en/latest/continuous_deployment.html#continuous-deployment-to-google-app-engine).
Veamos pasa a paso, como hemos creado nuestro shippable.yml:

El primer paso sería indicar la imagen de DockerHub, nosotros, tenemos ya una creada,
pero vamos a omitirla, y vamos a crearla desde cero, ya que solo es añadir el SDK con Shippable.
Vamos a no indicarla, ya que vamos a usar la que nos da Shippable por defecto. Pero podríamos con algo como esto:
```
build_image :  evenge / entorno
```
Volvemos a repetir, que no vamos a introducir la linea anterior, por lo que partimos de la imagen Shippable por defecto.

Ahora, vamos a indicar el lenguaje que vamos a usar en GAE

```
language: python

python:
- "2.7"
```

Vamos a declarar las variables, rutas, etc necesarias:

```
env:
global:
- GAE_DIR=/tmp/gae
- EMAIL=8macau8@gmail.com
- secure: RACsb1T9/QPr32TxNHaQ5yqq/EyWXSFIKlmmh633cvxygeBt7UJoM674Pqkg2RfwHN4XJ+lrC8s4FDffixbK4OXKr7aW0lNjLNcdPM/1NgZC1mimNGG+UOB1sAMkLUO909V+pMHq53f5oYb+s3aHFukq9zG5+d7+yNZ89bb+lX4ujhFjxMTltT8OOuQvzFwRkOoTH7CdfJDUqeF+MABCuzOFq1ewU6j0QqTi4DtZP4ZNNMA/8b0935U2tOdFlbQ8Xx1ZTm6UFrMGEJGlfRJAOKls20mXiF3wudYSXEw69PztNyJ2vg+WL7oE6xUobJHXOLIReevDm7KrmEC8p7Re4w==
```

Como indica el tutorial, necesitaremos el SDK. Por tanto, vemos si existe, y si no, lo descargamos e instalamos.
```
before_install:
- >
test -e $GAE_DIR ||
(mkdir -p $GAE_DIR &&
  wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.15.zip -q -O /tmp/gae.zip &&
  unzip /tmp/gae.zip -d $GAE_DIR)
```

Posteriormente, vamos a instalar los requerimientos que va a necesitar nuestra máquina para poder usar [NoseGAE](https://github.com/Trii/NoseGAE) para testeo y otras para conexión y provisión del servidor de desarrollo y conexión con la BD
```
nose
coverage
NoseGAE
WebTest
```
Con la orden:
```
install:
- pip install -r requirements.txt
```

Vamos a preparar el entorno para que lanzce los test:
```
before_script:
- echo 'Europe/Madrid' | sudo tee /etc/timezone
- sudo dpkg-reconfigure --frontend noninteractive tzdata
- mkdir -p shippable/testresults
- mkdir -p shippable/codecoverage
```
Y una vez tenemos los directorios y la carpeta donde vamos a gardar los resultados, lanzamos nuestro test.py con Nose antes programado por nostros:

```
script:
- >
nosetests test.py
--with-gae --without-sandbox --gae-lib-root=$GAE_DIR/google_appengine
--with-xunit --xunit-file=shippable/testresults/test.xml
--with-coverage --cover-xml --cover-xml-file=shippable/codecoverage/coverage.xml
```

Este era nuestro test.py, para probar que se ha desplegado correctamente:

```
import unittest
from google.appengine.ext import db
from google.appengine.ext import testbed
from index import Evenge

class EvengeTestCase(unittest.TestCase):
def setUp(self):
self.testbed = testbed.Testbed()
self.testbed.activate()
self.testbed.init_datastore_v3_stub()

def tearDown(self):
self.testbed.deactivate()

def test(self):
evenge = Evenge()
response = evenge.hazElCuadrado(4)
self.assertEqual(response,16)

if __name__ == "__main__":
unittest.main()
```

Si la operación es satisfactoria, procederá al despliegue automático de los achivos del repositorio de la rama Master.
```
after_success:
- if [ "$BRANCH" == "master" ]; then $GAE_DIR/google_appengine/appcfg.py --oauth2_refresh_token=$GAE_TOKEN update . ; else echo "No deployment for this $BRANCH"; fi
```

-------------------------
## Tests unitarios con Shippable y NoseGAE

Podemos consultar la documentación de [NoseGAE](https://github.com/Trii/NoseGAE)
Cuando Shipable, como ya hemos comentado, llega al apartado de ejecución de test, en nuestro caso del archivo test.py, procede a realizar los test unitarios de este módulo.
En nuestro archivo podemos encontrar funciones como esta:

```
def test(self):
evenge = Evenge()
response = evenge.hazElCuadrado(4)
self.assertEqual(response,16)
```
oseGAE establece el entorno de desarrollo GAE antes de su prueba.
Esto significa que usted puede escribir fácilmente test funcionales para su aplicación sin tener que arrancar realmente el servidor dev y ponerlo a prueba a través de HTTP.
El plugin también configura e inicia una instancia TestBed, su application_id basa apagado su app.yaml , y establece los caminos adecuados utilizando dev_appserver.fix_sys_path ().

Es una función básica que nos servirá de ejemplo, pero podemos ver como se trabaja.
Simplemente es la comprobación de si la respuesta a una función dá el valor esperado.
Si es así, el test es satisfactorio, de lo contrario, el test será fallido y Shippable no procederá al despliegue.

Veamos una función que usamos en nuestro test.py:

```
import unittest
from google.appengine.ext import db
from google.appengine.ext import testbed
from index import Evenge
from _oo.classes.ponente import Ponente
from _oo.classes.evento import Evento

class EvengeTestCase(unittest.TestCase):
def setUp(self):
self.testbed = testbed.Testbed()
self.testbed.activate()
self.testbed.init_datastore_v3_stub()

def tearDown(self):
self.testbed.deactivate()

"""
  Función de testeo que comprobará si es factible insertar un Ponente.
  Sirve de utilidad para ver si hay conexión con DataStore y si la introducción de un ponente va a dar o no error.
"""
def testInsertarPonente(self):
  evenge = Evenge()
  ponente = Ponente(
    email = "pepito@jemail.com",
    telefono = "sony xperia",
    twitter = "@pepitoG",
    web = "http://pepitoG.es"
  )
  response = evenge.testPonente(ponente)
  self.assertEqual(response,'pepito@jemail.com')

  if __name__ == "__main__":
    unittest.main()
```

```

# Funcion testPonente() de la clase Evenge

def testPonente(self, ponente):
  ponente.put()
  query = Ponente.query(Ponente.email == 'pepito@jemail.com')
  email = query.email
  query.delete
  return email

```

Con este test, vemos si esta disponible el Datastore para poder insertar ponentes en este caso.
Tenemos que tener en cuenta el importar los módulos necesarios para el test.

A la hora de hacer el despliegue, cuando hacemos un push a la rama master de nuestro repo, Shippable ejecutará estos test, y nos devolverá los resultados de los casos.
![](http://i58.tinypic.com/vwtp2x.png)

-------------------------
#DESPLIEGUE DE LA APLICACIÓN#
Antes de comenzar tenemos que saber que GAE tiene una serie de limitaciones si se usa de forma gratuita a la hora de desplegar nuestras aplicaciones, que son las siguientes:

- Tiene un espacio máximo de 10 aplicaciones de forma gratuita.

- Tiene cierta limitación en la cuota de visita(5 millones de visitas mensuales), ejemplo:

  Si 50 visitantes acceden a mi página, es probable que dicha cuota se encuentre en, aproximadamente, un 10%. Esto indicaría que si accedieran otros 450 visitantes se completaría la cuota, llegando al 100%, y mi aplicación quedaría pausada hasta el reinicio de todas las cuotas (cada 24hs).

- Tiene cierta limitación en el almacenamiento de datos(500MB de espacio), ejemplo:

  Si la cuota estándar (gratis) se limita a los 1000 MB de datos almacenados y nuestra aplicación alcanza dicha cantidad, podrá seguir recibiendo peticiones (si es que no se ha alcanzado el máximo de ésta cuota), pero no podrá continuar almacenando en la base de datos.


Para ello se puede contratar más de cantidad de visitas como de almacenamiento.

##Registro
Antes de despleglar nuestra aplicación debemos de registrar nuestra aplicacion en [appengine.google.com](https://accounts.google.com/ServiceLogin?service=ah&passive=true&continue=https%3A%2F%2Fappengine.google.com%2F_ah%2Fconflogin%3Fcontinue%3Dhttps%3A%2F%2Fappengine.google.com%2F&ltmpl=ae)
Una vez ingresado, presiona en el botón “Create Application”.

[![GAE](http://recursospython.com/wp-content/uploads/2013/10/4.png)]()

Ahora procedemos a rellenar los campos teniendo en cuenta lo siguiente:

- Application Identifier: dominio por el cual tendremos acceso a nuestra aplicación. Utiliza el botón “Check Availability” para verificar que esté disponible.
- Application Title: título para la aplicación. No es muy relevante pero no puede ser cambiado. Te recomiendo un nombre en minúsculas y sin espacios.
En los demás campos deja los valores por defecto.
Por último presiona "Create Application". Una vez creada, dirígete nuevamente a appengine.google.com y verás tu aplicación en la lista.


##Ejecutar nuestra apliación en local

Un paso muy importante antes de desplegar nuestra aplicación en el servidor de GAE, es desplegarla "Localmente", para realizar las pertinentes pruebas y test de funcionamiento.

[Linux]()

Si usamos  linux se realizaria de la siguiente manera en la terminal introduciendo estos comandos:

Iniciar el servidor de desarrollo local indica lo siguiente en la terminal:

      dev_appserver.py ubicacionapp

Por defecto el puerto 8080 será utilizado. Para cambiarlo, indica:

      dev_appserver.py --port=8081 ubicacionapp/

[Mac y Windows]()

Mac y Windows cuentan con un "Laucher" para esta tarea, ambos "Laucher" son iguales así que realizaré la explicación en Mac.

Lo primero que debemos de hacer es instalar el [SDK](https://cloud.google.com/appengine/downloads), en caso de no tenerlo instalado.

Una vez que lo tenemos instalado, vamos a crear el proyecto en con el "Laucher" que se nos ha instalado.

En mi caso yo uso Mac, así que simplemente tenemos que ejecutar el Launcher de GAE que hemos instalado.

Cuando se haya ejecutado le tenemos que dar al botón "+" que se encuentra en la parte inferior izquierda.

Cuando hayamos hecho eso, se nos abrirá una ventanita donde debemos de buscar la carpeta que contiene nuestro proyecto, y también debemos de especificar el nombre que le queremos poner al proyecto para hacer las pruebas en local.

Los siguientes puertos vienen por defecto:
+ Admin port
+ Port

pero nosotros podemos especificar los que queramos.

Cuando ya tengamos todo listo, le damos al botón "Create", de esta manera el proyecto se nos creará y se añadira a la lista de proyectos.

Una vez realizados todos estos pasos, solo debemos de darle a botón "Run" y nuestro proyecto se ejecutará en local.

Ahora solo debemos de irnos a nuestro navegador y escribir:

localhost:8080


[![GAE](http://i.imgur.com/bX9LexV.png)]()

De esta manera se usaría en local nuestra aplicación y podreamos probar todo lo que queramos.

##Desplegar la aplicación definitivamente

Una vez desarrollado la aplicación y testeado su funcionalidad en el servidor de desarrollo local, procederemos a desplegar
la aplicación en Google. Para usuarios de Linux el procedimiento será vía consola. Para Windows y Mac OS X utilizaremos el "Launcher".

[Linux]()

Abre la terminal y ejecuta:

      appcfg.py --email=yo@gmail.com update ubicacionapp/

- La opción --email indica la cuenta de Google en la cual se encuentra registrada la aplicación. Si tu dirección es @gmail.com, éste puede omitirse (--email=yo).
- Luego, será solicitada la contraseña.
- ubicacionapp/ indica la carpeta o ruta en donde se encuentra el archivo app.yaml junto con los demás, pero este primero determinará la existencia de una aplicación en dicha ruta para appcfg.py.
- En caso de haber especificado erróneamente la ubicación, se quejará diciendo:

      appcfg.py: error: Directory does not contain an Documents.yaml configuration file.


[Mac y Windows]()

Para este caso ejecutamos el "Laucher" y selecciona tu aplicación en la lista de aplicaciones. Luego, presiona el botón “Deploy” en la barra superior. La dirección de correo y contraseña serán solicitados. Al finalizar el proceso, la ventana “Delpoyment to Google” indicará que la misma puede ser cerrada.

[![GAE](http://i.imgur.com/LlyJ4F2.png)]()


De esta manera, ya se encuentra nuestra aplicación en funcionamiento.
[evenge-2014.appspot.com](evenge-2014.appspot.com)
