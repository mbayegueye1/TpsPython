class Ville:
    def __init__(self,nom, population):
        self.nom = nom
        self.population = population
    def __eq__(self, autre):
        if not isinstance(autre,Ville):
            return False
        return self.nom==autre.nom and self.population==autre.population
    def __hash__(self):
        return hash((self.nom, self.population ))


ville1 = Ville("montpellier", 300000)
ville2 = Ville("montpellier", 300000)
mon_set ={ville1, ville2}
print(mon_set)
for ville in mon_set:
    print(ville.nom, ville.population)
