import requests

from src.user import User

response = requests.get('http://randomuser.me/api/')

result = response.json()
# prettyprinter.cpprint(result)
record = result['results'][0]

user = User(record['name']['title'], record['name']['last'], record['name']['first'], record['login']['username'],
            record['email'])

print(f"{user.titre} {user.nom_complet}")
