def comptage_recursif(liste, min, max):
    nbr_element = 0
    for i in liste:
        if type(i) == int and min < i < max:
            nbr_element += 1
        elif type(i) == list:
            nbr_element += comptage_recursif(i,min,max)
    return nbr_element
print(comptage_recursif([28, [12, [13, 1], -2, [[4, 5], -5]]],10,15))



