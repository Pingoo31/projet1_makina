import requests
from prettyprinter import cpprint

from src.user import User


class APIUnreachableException(Exception):
    pass


class HttpNotFound(Exception):
    pass


def get_user():
    user = None
    try:
        response = requests.get('http://randomuser.me/api/')
        if response.status_code == 404:
            raise HttpNotFound()
        result = response.json()
        # prettyprinter.cpprint(result)
        record = result['results'][0]

        return User(record['name']['title'], record['name']['last'], record['name']['first'],
                    record['login']['username'],
                    record['email'])
    except requests.exceptions.ConnectionError:
        raise APIUnreachableException()


def main():
    try:
        user = get_user()
        cpprint(user)
        # print(f"{user.titre} {user.nom_complet}")
    except APIUnreachableException:
        print("L'API est injoignable.")
    except HttpNotFound:
        print("l'URL n'exite pas")


main()
