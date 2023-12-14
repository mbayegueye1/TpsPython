class Zoo:
    animaux = {}

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
