##   JEU PENDU
from random import *
f = open('mots.txt')
liste = []
for line in f.readlines():
    liste.append(line.strip()) ##.strip() pour sauter les caracteres speciaux et saut de ligne
nbr_lines = len(liste)
mot_tire = choice(liste)  ##tirer aleatoirement un mot d'un liste
le_mot_trouve = set()
max_erreur = randint(3, 5)
print(max_erreur)

print("_"*len(mot_tire))
erreur = 0
while True:
    lettre_str = str(input(("Propose une lettre")))
    if len(lettre_str) ==1:
        if lettre_str in le_mot_trouve:
            print("bien choisi en autre")
        elif lettre_str not in le_mot_trouve:
            erreur += 1
            if erreur == max_erreur:
                print("Game Over")
                break
        else:
            le_mot_trouve.add(lettre_str)
            print(mot_tire)












