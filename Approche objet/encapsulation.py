class Livre:
    achetable = False
    def __init__(self, titre:str , auteur:str, achetable:bool):
        self._titre = titre
        self._auteur = auteur
        self._achetable = achetable
    @property
    def titre(self):
        return self._titre
    @titre.setter
    def titre(self, nvtitre):
        self._titre = nvtitre
    @property
    def auteur(self):
        return self._auteur
    @auteur.setter
    def auteur(self, nvauteur):
        self._auteur = nvauteur
    @property
    def achetable(self):
        return self._achetable
    @achetable.setter
    def achetable(self, nvachetable):
        self._achetable = nvachetable
    def afficher(self):
        return f"{self.titre}, {self.auteur},{self.achetable}"

livre1 = Livre("Soufi mon ", "Elif Shafak", False)
livre2 = Livre("Alerte sous les tropiques", "Cheikh  Diop",True)

livre1.titre = "Soufi mon Amour"
livre2.auteur = "Cheikh Anta Diop"
roman1 = livre1.afficher()
roman2 = livre2.afficher()
print(roman1)
print(roman2)








