class Ville:
    def __init__(self,nom, population):
        self.nom = nom
        self.population = population
    def __repr__(self):
        return f"Ville(nom='{self.nom}', population= '{self.population})'"
    def __str__(self):
        return f"nom={self.nom}, population: {self.population}"


ville1 = Ville("montpellier", 300000)

print(str(ville1))
print(repr(ville1))


