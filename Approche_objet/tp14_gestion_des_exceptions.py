class VilleException(Exception):
    def valider(self, ville):
        if not ville.nom:
            raise VilleException("Le nom n’est pas renseigné")
        if len(ville.nom.strip()) < 2:
            raise VilleException("Le nom fait moins de 2 caractères")
        if not ville.population:
            raise VilleException("La population n’est pas renseignée")
        if ville.population < 2000:
            raise VilleException("La population est inférieure à 2000 habitants")

class Ville:
    def __init__(self, nom, population):
        self.nom = nom
        self.population = population


ville1 = Ville("Montpellier", 300000)
ville2 = Ville("Pa", 1200)
ville3 = Ville("Ma", 500)

exceptions = VilleException()

try:
    exceptions.valider(ville1)
except VilleException as e:
    print("Erreur:", e)
else:
    print("Ville valide.")

try:
    exceptions.valider(ville2)
except VilleException as e:
    print("Erreur:", e)
else:
    print("Ville valide.")

try:
    exceptions.valider(ville3)
except VilleException as e:
    print("Erreur:", e)
else:
    print("Ville valide.")
