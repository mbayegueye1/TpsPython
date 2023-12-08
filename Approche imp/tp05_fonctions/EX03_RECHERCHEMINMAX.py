def min_max(a):
    ma_liste =[]
    maxVal =0
    min_val =0
    for i in range(a):
        ma_liste.append(i)
    for i in ma_liste:
        if i>=maxVal:
            maxVal=i
        elif i<min_val:
            min_val=i
        else:
            print("impossible")

    return print(maxVal , min_val)
min_max(17)

