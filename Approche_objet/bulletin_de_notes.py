class Etudiant:
    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom

class Bulletin(Etudiant):
    def __init__(self, etudiant):
        super().__init__(etudiant._nom, etudiant._prenom)
        self._disciplines = []

    def ajouter_discipline(self, matiere):
        discipline = Discipline(matiere)
        self._disciplines.append(discipline)

    def ajouter_note(self, discipline, valeur, date, categorie):
        note = Note(valeur, date, categorie)
        discipline._notes.append(note)

    def calculer_moyenne(self):
        liste_moyenne = {}
        for discipline in self._disciplines:
            if discipline._notes:
                total_notes = sum(note._valeur for note in discipline._notes)
                moyenne = total_notes / len(discipline._notes)
                liste_moyenne[discipline._matiere] = moyenne
            else:
                print("Impossible")

        return liste_moyenne

    def afficher(self):
        moy = self.calculer_moyenne()
        for discipline, moyenne in moy.items():
            print(f"Matiere: {discipline}, Moyenne: {moyenne}")

class Discipline:
    def __init__(self, matiere):
        self._matiere = matiere
        self._notes = []

class Note:
    def __init__(self, valeur, date, categorie):
        self._valeur = valeur
        self._date = date
        self._categorie = categorie

etudiant1 = Etudiant("yi", "xo")

bulletin1 = Bulletin(etudiant1)
bulletin1.ajouter_discipline("Python")
bulletin1.ajouter_discipline("JAVA")

bulletin1.ajouter_note(bulletin1._disciplines[0], 17, "26/05/2023", "Devoir")
bulletin1.ajouter_note(bulletin1._disciplines[0], 18, "26/05/2023", "Examen")
bulletin1.ajouter_note(bulletin1._disciplines[0], 15, "26/05/2023", "tp")

bulletin1.ajouter_note(bulletin1._disciplines[1], 12, "26/05/2023", "Devoir")
bulletin1.ajouter_note(bulletin1._disciplines[1], 17, "26/05/2023", "Examen")
bulletin1.ajouter_note(bulletin1._disciplines[1], 13, "26/05/2023", "tp")


bulletin1.afficher()
