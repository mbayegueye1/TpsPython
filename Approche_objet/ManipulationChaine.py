chaine = "Durand;Marcel;2 523.5"

premier_caratere = chaine[0]
print("Premier caractère:",premier_caratere)

print("longueur chaine:", len(chaine))
index = chaine.index(";")
print(index)
portion = chaine[4:7]
print(portion)
nom1 = chaine[chaine.index("D"):chaine.index(";")]
print(nom1.upper())
print(nom1.lower())
new_chaine =chaine.split(";")
salair =new_chaine[2]
float_salaire = float(salair.replace(" ",""))
new_chaine[2]=float_salaire
print(new_chaine)
nom = new_chaine[0]
prenom = new_chaine[1]
salaire = new_chaine[2]



