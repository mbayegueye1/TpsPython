from abc import ABC, abstractmethod
from tp6_redef_method import *


class Sortie(ABC):
    def __init__(self, date, livre):
        self._date= date
        self._livre = livre
    @abstractmethod
    def get_montant(self):
        pass

class Emprunt(Sortie):
    def __init__(self,date, livre, duree:int):
        super().__init__(date, livre)
        self._duree = duree
    def get_montant(self):
        if isinstance(self._livre, LivrePapier):
            return self._duree*0.5
        elif isinstance(self._livre, LivreNumerique):
            return self._duree*0.25
        else:
            return False

class Achat(Sortie):
    def __init__(self, date, livre, montant:int):
        super().__init__(date, livre)
        self._montant = montant
    def get_montant(self):
        if isinstance(self._livre, LivrePapier) or isinstance(self._livre, LivreNumerique):
            return self._montant

l1p = Emprunt("12/04/2017", livrep1 , 4)
l2p = Emprunt("21/04/2017", livrep2, 10)
l1n = Emprunt("12/04/2017", livren1 , 4)
l2n = Emprunt("21/04/2017", livren2, 10)

l1pA = Achat("12/04/2017", livrep1 , 4)
l2pA = Achat("21/04/2017", livrep2, 10)
l1nA = Achat("12/04/2017", livren1 , 4)
l2nA= Achat("21/04/2017", livren2, 10)

liste =[l1p,l2p,l1n,l2n,l1pA,l2pA,l1nA,l2nA]
somme =0
for i in liste:
    a= i.get_montant()
    somme +=a
print(somme)






