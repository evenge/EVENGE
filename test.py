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
