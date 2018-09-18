import unittest

from src.client import Client
from src.facture import Facture
from src.ligneFacture import LigneFacture
from src.produit import Produit


class testFacture(unittest.TestCase):

    def setUp(self):
        client = Client("Pingoo", "Stéphane")
        produit = Produit("AndroidOne", 125.8)
        produit2 = Produit("LinuxPhone", 241)
        self.facture = Facture(client)
        self.facture.ajouter_ligne_produit(LigneFacture(produit, 2))
        self.facture.ajouter_ligne_produit(LigneFacture(produit2, 1))


    def test_creation_facture(self):
        self.assertEqual(self.facture.montant_HT, 951)
        self.assertEqual(self.facture.montant_total, 1141.2)
