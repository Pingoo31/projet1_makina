import unittest
from src.ligneFacture import LigneFacture
from src.produit import Produit


class TestLigneFacture(unittest.TestCase):
    def test_creation_ligne_facture(self):
        produit = Produit("AndroidOne", 125.8)
        ligne = LigneFacture(produit, 2)
        self.assertIsInstance(ligne.produit, Produit)
        self.assertEqual(ligne.produit.nom, "AndroidOne")
        self.assertEqual(ligne.montant, 125.8 * 2)
