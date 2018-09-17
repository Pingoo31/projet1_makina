from dataclasses import dataclass


@dataclass
class Client:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    @property
    def nom_complet(self):
        return self.prenom + " " + self.nom
