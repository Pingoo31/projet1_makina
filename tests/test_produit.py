import unittest
from src.produit import Produit


class TestProduit(unittest.TestCase):
    def test_creation_produit(self):
        produit = Produit("AndroidOne", 125.8)
        self.assertEqual(produit.nom, "AndroidOne")
        self.assertEqual(produit.prix, 125.8)
