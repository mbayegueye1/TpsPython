class Ville:
    def __init__(self,nom, population):
        self.nom = nom
        self.population = population
    def __eq__(self, autre):
        if not isinstance(autre,Ville):
            return False
        return self.nom==autre.nom and self.population==autre.population




ville1 = Ville("montpellier", 300000)
ville2 = Ville("montpellier", 300000)
print(ville1 == ville2)
