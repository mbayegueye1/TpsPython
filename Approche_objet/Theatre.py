class Theatre:
    def __init__(self,nom, capa_max, tot_clients, tot_recette):
        self._nom = nom
        self._capa_max = capa_max
        self._tot_clients = tot_clients
        self._tot_recette = tot_recette

    def inscrire(self, nbr_clients, tarif):
        if self._tot_clients + nbr_clients <= self._capa_max:
            clients = self._tot_clients + nbr_clients
            gain = self._tot_recette + nbr_clients*tarif
            return f" total de clients inscrits{clients}, recette totale de l’établissement{gain}"


        else:
            return print("Erreur ")


t1 = Theatre("Comedie", 300,250,2000)
resultat = t1.inscrire(75, 20)


