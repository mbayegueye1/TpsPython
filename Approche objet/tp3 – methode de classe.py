class Zoo:
    animaux = {}

    def __init__(self, animaux_presents, nombretot):
        self.animaux_presents = animaux_presents
        self.nombretot = nombretot

    @classmethod
    def ajouter_animaux(cls, animal, nombre):
        if animal not in cls.animaux:
            cls.animaux[animal] = 0

        cls.animaux[animal] += nombre
        print(f"{nombre} {animal} ajoutés")


Zoo.ajouter_animaux("Tigre", 4)
Zoo.ajouter_animaux("lion", 5)
Zoo.ajouter_animaux("elephant", 5)
print("Dans le zoo, on a:")
print(Zoo.animaux)
