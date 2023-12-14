class Salarie:
    def __init__(self, nom, matricule, service):
        self._nom = nom
        self.matricule = matricule
        self._service = service
    @staticmethod
    def comptage_chaine(liste):
        dict_traitement={}
        for value in liste:
            cnt = liste.count(value[2])
            key = value[2]
            if key not in dict_traitement:
                dict_traitement[key] = 1
            else:
                dict_traitement[key] += 1
        dict_traitement[value[2]] = cnt
        return dict_traitement


liste = [["Antoine Dupont", 127, "DSI/JAVA"],
         ["Berthe Casa", 238, "DSI/PHP"],
         ["Fatima Ouassa", 478, "DSI/JAVA"],
         ["Cassian Andor", 156, "DSI/PYTHON"],
         ["Lee Wu", 559, "DSI/PH"],
         ["Hassan Missen", 96, "DSI/PYTHON"],
         ["Aurélien PIC", 889, "DSI/JAVA"]]

dico = Salarie.comptage_chaine(liste)
print(dico)



