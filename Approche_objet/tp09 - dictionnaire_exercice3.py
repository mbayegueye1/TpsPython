def  traitement():
    dict_traitement={}
    entree =  ["Ananas", "Banane", "Orange", "Ananas", "Banane"]
    for value in entree:
        cnt = entree.count(value)
        dict_traitement[value] = cnt

    return dict_traitement
recup = traitement()

print(recup)


