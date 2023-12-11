def func_recursive(liste):
    nbr_elements=0
    for i in liste:
        if type(i) == int:
            nbr_elements += 1
        elif type(i) == list:
            nbr_elements += func_recursive(i)

    return nbr_elements
print(func_recursive([28, [12, [13, 1], -2, [[4, 5], -5]]]))




