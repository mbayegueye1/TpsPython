class Animal:
    def __init_(self,nom, categorie, comportement):
        self._nom = nom
        self._categorie = categorie
        self._comportement = comportement

class Zoo:
    def __init__(self, nom, liste_zones):
        self._nom = nom
        self._liste_zones = liste_zones

class Zone:
    def __init__(self, nom, liste_animaux):
        self._nom = nom
        self.liste_animaux = liste_animaux

