import unittest
from google.appengine.api import users
from index import Evenge

class EvengeTestCase(unittest.TestCase):
	def setUp(self):
		pass

	def test(self):
		evenge = Evenge()
		response = evenge.hazElCuadrado(4)
		self.assertEqual(response,16)


if __name__ == "__main__":
	unittest.main()
