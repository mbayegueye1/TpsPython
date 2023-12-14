class Livre:
    def __init__(self, titre:str, auteur:str, achetable:bool):
        self._titre = titre
        self._auteur = auteur
        self._achetable = achetable
    def afficher_infos(self):
        print(f"le titre {self._titre}, l'auteur {self._auteur} achetable {self._achetable}")

class  LivrePapier(Livre):
    def __init__(self,titre:str, auteur:str, achetable:bool, etat:str):
        super().__init__(titre,auteur,achetable)
        self._etat = etat
    def afficher_infos(self):
        print(f"le titre: {self._titre}, l'auteur: {self._auteur} achetable: {self._achetable}, etat:{self._etat}")

class  LivreNumerique(Livre):
    def __init__(self,titre:str, auteur:str, achetable:bool, format:str):
        super().__init__(titre,auteur,achetable)
        self._format = format
    def afficher_infos(self):
        print(f"le titre: {self._titre}, l'auteur: {self._auteur} achetable: {self._achetable}, format:{self._format}")
#if __name__ == "__main__":
liste = []
livrep1 = LivrePapier("Soufi mon ", "Elif Shafak", False,"abime")
livrep2 = LivrePapier("Alerte sous les tropiques", "Cheikh  Diop",True,"Moyen")
livren1 = LivreNumerique("dssda", "xi",True,"pdf")
livren2 = LivreNumerique("dsfresda", "xive",True,"kindle")

liste.append(livrep1)
liste.append(livrep2)
liste.append(livren1)
liste.append(livren1)
for roman in liste:
    roman.afficher_infos()


