def calcul_moyenne(a):
    ma_liste =[]
    somme =0
    nbr_val =a
    for i in range(a):
        ma_liste.append(i)
        for i in ma_liste:
            somme = somme+i
            moyenne = somme/nbr_val
    return print(moyenne)

calcul_moyenne(10)


