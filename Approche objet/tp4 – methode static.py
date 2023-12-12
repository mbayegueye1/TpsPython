class ChaineUtils:
    @staticmethod
    def est_anagramme(chaine1, chaine2):
        if len(chaine1) == len(chaine2) and sorted(chaine1) == sorted(chaine1):
           return "Oui Anagramme"
        else:
            return "non pas des annagrammes"

    @staticmethod
    def comptage_chaine(chaine1, chaine2):
        cnt = chaine2.count(chaine1)  ## compte le nombre de fois ou la chaine2 apparait dans la chaine1
        return cnt

resultat = ChaineUtils.est_anagramme("gare", "rage")
nombre = ChaineUtils.comptage_chaine("abc", "abcabcabc")
print(resultat)
print(nombre)
