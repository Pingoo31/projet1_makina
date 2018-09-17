from client import Client
from facture import Facture
from ligneFacture import LigneFacture
from produit import Produit

produit1 = Produit("AndroidOne", 355)
produit2 = Produit("LinuxPhone", 241)

client = Client("THIPHONET", "Stéphane")
print("Nouveau client créé: " + client.nom_complet())

facture = Facture(client)
print("Facture n°: " + facture.numero_facture())

ligne1 = LigneFacture(produit1, 2)
facture.ajouter_ligne_produit(ligne1)
print("1 ligne ajoutée : " + ligne1.produit.nom + ", Qté : " + str(ligne1.quantite) + ", montant : " + str(ligne1.montant()))
ligne2 = LigneFacture(produit2, 1)
facture.ajouter_ligne_produit(ligne2)
print("1 ligne ajoutée : " + ligne2.produit.nom + ", Qté : " + str(ligne2.quantite) + ", montant : " + str(ligne2.montant()))

print("Montant HT = " + str(facture.montant_HT()))
print("Montant Total = " + str(facture.montant_total()))

