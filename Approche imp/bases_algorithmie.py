print("######## EXERCICE1######")
for i in range(11):
    if i%2==0 :
        print(i)

print("######## EXERCICE2######")
liste=[1,15,-3,0,8,7,4,-2,28,7,-1,17,2,3,0,14,-4]
iliste =[]
print("les elements de la liste:")
for i in liste:
    print(i)
print(" les éléments positifs sont:")
for i in liste:
    if i>0:
        iliste.append(i)
        print(i)

print("les elements positifs:",iliste)
print("le nombre d'elements positifs est :",len(iliste))

