import pytest
import requests
import responses
from prettyprinter import cpprint

from src.user import User


class APIUnreachableException(Exception): pass


class HttpNotFound(Exception): pass


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


mock_user = {
    'results': [{
        'email': 'stephane@thipho.net',
        'name': {
            'title': 'Mr',
            'first': 'Stéphane',
            'last': 'THIPHONET',
        },
        'login': {
            'username': 'Pingoo'
        },
        'gender': 'male',

    }]
}


class Test_user():

    def test_get_user_mock(self, mocker):
        user = User.create_from_api(mock_user)
        mocker.patch('demo_mock_pytest.get_user', return_value=user)
        user = get_user()
        assert isinstance(user, User)
        assert user.prenom == "Stéphane"
        # self.assertEqual(user.nom, "THIPHONET")

    @responses.activate
    def test_get_user(self):
        responses.add(responses.GET, 'http://randomuser.me/api/', json=mock_user)
        user = get_user()
        assert isinstance(user, User)
        assert user.prenom == "Stéphane"
        assert user.nom == "THIPHONET"

    # @pytest.mark.skip("In progress")
    @responses.activate
    def test_get_user_server_unreachable(self):
        with pytest.raises(APIUnreachableException):
            user = get_user()

    # @pytest.mark.skip("In progress")
    @responses.activate
    def test_get_user_url_not_exist(self):
        responses.add(responses.GET, 'http://randomuser.me/api/', status=404)
        with pytest.raises(HttpNotFound):
            user = get_user()
