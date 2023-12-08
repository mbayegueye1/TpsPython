liste1=[1,15,-3,8,7,4,-2,28,-1,17,2,3,0,14,-4]
liste2=[3,-8,17,5,-1,4,0,6,2,11,-5,-4,8]
list_commun = []
print(len(liste1) , len(liste2))
for i in range(len(liste1)):
    for ii in range(len(liste2)):
        if liste1[i] == liste2[ii]:
            list_commun.append([liste1[i],liste2[ii]])
print(len(list_commun))


