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

    def create_from_api(user_json):
        record = user_json['results'][0]
        return User(record['name']['title'], record['name']['last'], record['name']['first'],
                    record['login']['username'], record['email'])
