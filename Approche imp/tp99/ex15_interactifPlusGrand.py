liste =[]
val = int(input("entree 10 nombres"))
while True:
    for i in range(11):
        value =int(input())
        liste.append(value)
    break
maxi = max(liste)
print(maxi)
