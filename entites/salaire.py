from pythonProject.Approche_objet.ManipulationChaine import *


class Salaire:
    def __init__(self, nom, prenom, salaire):
        self._nom = nom
        self._prenom = prenom
        self._salaire = salaire
    def sortie(self):
        print( f"{self._nom},{self._prenom} a un salaire de {self._salaire} euros ")

s1 = Salaire(nom , prenom, salaire )
s1.sortie()
