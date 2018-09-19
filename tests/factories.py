import factory

from src.client import Client
from src.facture import Facture
from src.produit import Produit


class client_factory(factory.Factory):
    class Meta:
        model = Client

    nom = factory.Faker("last_name")
    prenom = factory.Faker('first_name')


class facture_factory(factory.Factory):
    class Meta:
        model = Facture

    client = client_factory()
    numero = factory.Faker('pyint')


class produit_factory(factory.Factory):
    class Meta:
        model = Produit

    nom = factory.Faker('company')
    prix = factory.Faker('pyfloat', left_digits=3, right_digits=2, positive=True)
