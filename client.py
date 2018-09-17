class Client(object):
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def nom_complet(self):
        return self.prenom + " " + self.nom
