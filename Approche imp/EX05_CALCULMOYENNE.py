liste=[1,15,-3,0,8,7,4,-2,28,7,-1,17,2,3,0,14,-4]
nbr_val =len(liste)
somme= 0
print("la moyenne des valeurs de la liste :")
for i in liste:
    somme = somme+i
    moyenne = somme/nbr_val
print(moyenne)
print("la moyenne des valeurs positifs de la liste :")
for i in liste:
    if i%2 ==0:
        somme = somme+i
        moyenne_positifs = somme/nbr_val
print(moyenne_positifs)


