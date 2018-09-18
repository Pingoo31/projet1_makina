from dataclasses import dataclass


@dataclass
class Client:
    nom: str
    prenom: str

    @property
    def nom_complet(self):
        return self.prenom + " " + self.nom
