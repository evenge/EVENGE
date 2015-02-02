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

    def test(self):
        evenge = Evenge()
        response = evenge.hazElCuadrado(4)
        self.assertEqual(response,16)

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

    def testInsertarEvento(self):
        evenge = Evenge()
        evento = Evento(
            evt.nombre = "Evento de prueba"
            evt.tipo = 1
            evt.privado = 1
            evt.idCreador = "1"
            evt.lugar = "Granada"
        )
        response = evenge.testInsertarEvento(evento)
        self.assertEqual(response, True)

    def testInsertarUsuario(self):
        evenge = Evenge()
        usuario = Usuario(
            nombre = "Pepe",
            apellidos = "Ortiz",
            email = "pepe@gmail.com",
            telefono = "680178921"
        )
        response = evenge.testInsertarUsuario(usuario)
        self.assertEqual(response, True)
        
if __name__ == "__main__":
	unittest.main()
