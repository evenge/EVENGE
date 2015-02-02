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
