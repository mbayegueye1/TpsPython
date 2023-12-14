class AdressePostale:
    def __init__(self, num_rue, libelle, code_postal, ville):
        self.num_rue = num_rue
        self.libelle = libelle
        self.code_postal = code_postal
        self.ville = ville


adr1 = AdressePostale(20, "av Toulouse", 34000, "Montpellier")
adr2 = AdressePostale(1, "Rue vieille Monnaie", 25000, "Besancon")

print(adr1.num_rue, adr1.libelle, adr1.code_postal, adr1.ville)


class Personne:
    def __init__(self, nom, prenom, adresse:AdressePostale):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
    def set_nom(self,nom):
        self.nom = nom
    def set_prenom(self,prenom):
        self.prenom = prenom
    def set_adresse(self,adresse):
        self.adresse = adresse
    def dire_nom(self):
        return "Son nom est :"+ self.nom
    def dire_prenom(self):
        return "Son prenom est :"+ self.prenom
    def dire_adresse(self):
        return self.adresse
    def afficher(self):
        print(self.nom, self.prenom, self.adresse.code_postal,self.adresse.ville)
pers1 = Personne("madi", "bo", adr1)
pers1.set_nom("NDi")
pers1.set_prenom("Aye")
last_name = pers1.dire_prenom()
name =pers1.dire_nom()
print(name)
print(last_name)
attributs =pers1.afficher()
pers2 = Personne("embi", "CI", adr2)
print(pers1.nom, pers1.prenom, pers1.adresse.num_rue, pers1.adresse.libelle, pers1.adresse.code_postal,
      pers1.adresse.ville)
print(pers2.nom, pers2.prenom, pers2.adresse.num_rue, pers2.adresse.libelle, pers2.adresse.code_postal,
      pers2.adresse.ville)
