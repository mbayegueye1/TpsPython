def  traitement(liste):
    dict_traitement={}
    entree = ["Coucou", "Hi"]
    for i, value in enumerate(entree):
        dict_traitement[value] = liste[i]

    return dict_traitement

recup=traitement([6,2])
print(recup)
