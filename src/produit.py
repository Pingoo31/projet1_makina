from dataclasses import dataclass


@dataclass
class Produit:
    nom: str
    prix: float = 0.0
