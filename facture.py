import random

class Facture(object):


    def __init__(self, client):
        self.clent = client
        self.numero = random.random() * 10000
        self.lignes_produit = []
        self.tva = 1.2

    def ajouter_ligne_produit(self, ligne):
        self.lignes_produit.append(ligne)

    def numero_facture(self):
        return str(int(self.numero))

    def montant_total(self):
        return self.montant_HT() * self.tva

    def montant_HT(self):
        ht = 0
        for ligne in self.lignes_produit:
            ht += ligne.montant()
        return ht

