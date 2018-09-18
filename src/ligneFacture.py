class LigneFacture:

    def __init__(self, produit, quantite):
        self.produit = produit
        self.quantite = quantite

    @property
    def montant(self):
        return self.produit.prix * self.quantite
