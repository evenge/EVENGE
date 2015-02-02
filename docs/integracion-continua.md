# Integración continua.

Para provisionar nuestro proyecto con integración continua barajamos varias posibilidades.
1. La sincronización directa con GitHub que nos provee GAE.
Simplemente con añadir el repo donde tenemos el código, GAE sincroniza la app con el, y cuando se realice un push, se hará el despliegue automático.
Esto es factible, si y solo si tenemos unicamente el código de la aplicación el el repo.
Pero nosotros tenemos documentación, lista de tareas, etc. Por lo que no nos valía.

1. La segunda opción, y por la que nos decantamos finalmente, fue el despliegue por Shippable.
Este sistema de CI permite crear, provisionar, testear y desplegar nuestra app en una máquina virtual, en el servidor que queramos.
Además trabaja con IaaS y PaaS como Heroku, Amazon Elastic Beanstalk, OpsWorks AWS, Google App Engine, Red Hat OpenShift o cualquier proveedor de infraestructura después de una compilación exitosa.

## Shippable
### Introduccion

Shippable usa Docker para el despliegue de las apps.
Sus casos de uso más comunes, y concretamente los que vamos a darle en el proyecto son:
- Automatización del empaquetado y despliegue de web apps.
- Testeo automatizado y despliegue en caso de éxito.

### Configurar Shippable para Evenge.

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
