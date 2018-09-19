from dataclasses import dataclass


@dataclass
class User:
    titre: str
    nom: str
    prenom: str
    username: str
    email: str

    @property
    def nom_complet(self):
        return self.prenom + " " + self.nom
