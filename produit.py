from dataclasses import dataclass


@dataclass
class Produit:

    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
