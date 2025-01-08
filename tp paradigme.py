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

if __name__ == "__main__":
    noms, notes = saisir_donnees()
    print("\nDonnées saisies :")
    print("Noms :", noms)
    print("Notes :", notes)


