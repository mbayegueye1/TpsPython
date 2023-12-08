def somme_parair(i):
    ma_liste =[]
    somme_pairs = 0
    for a in range(i):
        ma_liste.append(a)
        for j in range(len(ma_liste)):
            if ma_liste[j]%2 == 0:
                somme_pairs = somme_pairs + ma_liste[j]
    return somme_pairs

print(somme_parair(10))

