# Tests unitarios con Shippable y NoseGAE

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
