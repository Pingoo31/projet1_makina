import random
from dataclasses import dataclass

from src.client import Client


@dataclass
class Facture:
    client: Client
    numero:int = int(random.random() * 10000)
    lignes_facture = []
    tva: float = 1.2

    def ajouter_ligne_produit(self, ligne):
        self.lignes_facture.append(ligne)

    @property
    def numero_facture(self):
        return str(self.numero)

    @property
    def montant_total(self):
        return self.montant_HT * self.tva

    @property
    def montant_HT(self):
        ht = 0
        for ligne in self.lignes_facture:
            ht += ligne.montant
        return ht

