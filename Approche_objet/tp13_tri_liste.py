class Ville:
    def __init__(self,nom, population):
        self.nom = nom
        self.population = population
    def __eq__(self, other):
        if not isinstance(other,Ville):
            return False
        return self.nom==other.nom and self.population==other.population

    def __repr__(self):
        return f"Ville(nom='{self.nom}', population= '{self.population})'"

    def __lt__(self, other):
        return self.population < other.population


mes_villes = [Ville("Montpellier", 300000), Ville("Paris", 1200000), Ville("Marseille", 500000)]

print(mes_villes)
print("------------------------")

for ville in sorted(mes_villes):
    print(ville)
