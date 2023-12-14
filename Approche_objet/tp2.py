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


pers1 = Personne("madi".upper(), "bo".upper(), adr1)
pers2 = Personne("embi".upper(), "CI".upper(), adr2)
print(pers1.nom, pers1.prenom, pers1.adresse.num_rue, pers1.adresse.libelle, pers1.adresse.code_postal,
      pers1.adresse.ville)
print(pers2.nom, pers2.prenom, pers2.adresse.num_rue, pers2.adresse.libelle, pers2.adresse.code_postal,
      pers2.adresse.ville)
