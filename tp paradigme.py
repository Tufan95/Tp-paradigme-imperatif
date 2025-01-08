# Partie 1 : Saisie des données

def saisir_donnees():
    """
    Fonction pour saisir les noms et les notes des étudiants.
    Renvoie deux listes : noms et notes.
    """
    noms = []
    notes = []
    nombre_etudiants = int(input("Combien d'étudiants souhaitez-vous saisir ? "))

    for i in range(nombre_etudiants):
        nom = input(f"Nom de l'étudiant {i + 1} : ")
        note = float(input(f"Note de {nom} : "))
        noms.append(nom)
        notes.append(note)

    return noms, notes

# Partie 2 : Calcul de la moyenne
def calculer_moyenne(notes):
    """
    Calcule la moyenne d'une liste de notes.
    """
    return sum(notes) / len(notes) if notes else 0

# Partie 3 : Affichage de la répartition
def afficher_repartition(noms, notes):
    """
    Affiche la répartition des étudiants selon leurs résultats (réussite ou échec).
    """
    reussite = [noms[i] for i in range(len(notes)) if notes[i] >= 10]
    echec = [noms[i] for i in range(len(notes)) if notes[i] < 10]

    print("\nÉtudiants ayant réussi :", ", ".join(reussite))
    print("Étudiants en échec :", ", ".join(echec))

if __name__ == "__main__":
    noms, notes = saisir_donnees()
    print("\nDonnées saisies :")
    print("Noms :", noms)
    print("Notes :", notes)
    # Partie 2 : Calcul de la moyenne
    moyenne = calculer_moyenne(notes)
    print(f"\nLa moyenne de la classe est de {moyenne:.2f}.")
     # Partie 3 : Affichage de la répartition
    afficher_repartition(noms, notes)



