import pathlib
from random import randint

from src.ligneFacture import LigneFacture
from tests.factories import client_factory, facture_factory, produit_factory

# produit1 = Produit("AndroidOne", 355)
# produit2 = Produit("LinuxPhone", 241)
produit1 = produit_factory()
produit2 = produit_factory()

client = client_factory()
print("Nouveau client créé: " + client.nom_complet)

# facture = Facture(client)
facture = facture_factory()
print(f"Facture client : {facture.client.nom_complet}")
print(f"Facture n°: {facture.numero_facture}")

# ligne1 = LigneFacture(produit1, 2)
ligne1 = LigneFacture(produit_factory(), 2)
facture.ajouter_ligne_produit(ligne1)
print(f"1 ligne ajoutée : {ligne1.produit.nom}, Qté : {str(ligne1.quantite)}, montant : {str(ligne1.montant)}")
# ligne2 = LigneFacture(produit2, 1)
ligne2 = LigneFacture(produit_factory(), 1)
facture.ajouter_ligne_produit(ligne2)
print(f"1 ligne ajoutée : {ligne2.produit.nom}, Qté : {str(ligne2.quantite)}, montant : {str(ligne2.montant)}")

print(f"Montant HT = {str(facture.montant_HT)}")
print(f"Montant Total = {str(facture.montant_total)}")


def pdf_generator(content, filename):
    from weasyprint import HTML
    from weasyprint.fonts import FontConfiguration

    font_config = FontConfiguration()
    html = HTML(string=content)
    html.write_pdf(filename, font_config=font_config)


def generator():
    from jinja2 import Environment, FileSystemLoader
    import jinja2

    env = Environment(
        loader=FileSystemLoader('templates'),
        # pour déclencher une exeption en cas d'erreur dans le template
        undefined=jinja2.StrictUndefined,
    )
    template = env.get_template('facture.html')
    facture = facture_factory()
    for x in range(randint(2, 15)):
        facture.ajouter_ligne_produit(LigneFacture(produit_factory(), randint(1, 5)))
    facture_html = template.render(facture=facture)
    # print(facture_html)
    pathlib.Path('/tmp/facture.html').write_text(facture_html)
    pdf_generator(facture_html, '/tmp/facture.pdf')


generator()
