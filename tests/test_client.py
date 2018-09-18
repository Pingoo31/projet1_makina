import unittest
from src.client import Client


class TestClient(unittest.TestCase):
    def test_creation_client(self):
        client = Client("Pingoo", "Stéphane")
        self.assertEqual(client.nom_complet, "Stéphane Pingoo")
