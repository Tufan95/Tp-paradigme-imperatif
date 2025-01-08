# Partie 1 : Saisie des données

def saisir_donnees(): # Fonction pour saisir les noms et les notes des étudiants. Renvoie deux listes : noms et notes.
    """
    Fonction pour saisir les noms et les notes des étudiants.  
    Renvoie deux listes : noms et notes.
    """
    noms = [] # Liste pour stocker les noms des étudiants.
    notes = [] # Liste pour stocker les notes des étudiants.
    nombre_etudiants = int(input("Combien d'étudiants souhaitez-vous saisir ? ")) # Demande le nombre d'étudiants à l'utilisateur.

    for i in range(nombre_etudiants): # Boucle pour saisir les noms et les notes des étudiants.
        nom = input(f"Nom de l'étudiant {i + 1} : ") # Demande le nom de l'étudiant.
        note = float(input(f"Note de {nom} : "))  # Demande la note de l'étudiant.
        noms.append(nom) # Ajoute le nom à la liste des noms.
        notes.append(note) # Ajoute la note à la liste des notes.

    return noms, notes # Renvoie les listes des noms et des notes.

# Partie 2 : Calcul de la moyenne
def calculer_moyenne(notes): # Fonction pour calculer la moyenne d'une liste de notes. Renvoie la moyenne.
    """
    Calcule la moyenne d'une liste de notes.
    """
    return sum(notes) / len(notes) if notes else 0 # Renvoie la moyenne si la liste n'est pas vide, sinon 0.

# Partie 3 : Affichage de la répartition
def afficher_repartition(noms, notes): # Fonction pour afficher la répartition des étudiants selon leurs résultats (réussite ou échec).
    """
    Affiche la répartition des étudiants selon leurs résultats (réussite ou échec).
    """
    reussite = [noms[i] for i in range(len(notes)) if notes[i] >= 10] # Liste des étudiants ayant réussi.	
    echec = [noms[i] for i in range(len(notes)) if notes[i] < 10] # Liste des étudiants en échec.	

    print("\nÉtudiants ayant réussi :", ", ".join(reussite)) # Affiche les étudiants ayant réussi.	
    print("Étudiants en échec :", ", ".join(echec)) # Affiche les étudiants en échec.	

# Partie 4 : Meilleure note
def meilleure_note(noms, notes): # Fonction pour identifier l'étudiant ayant la meilleure note et afficher son nom et sa note.
    """
    Identifie l'étudiant ayant la meilleure note et affiche son nom et sa note.
    """
    if not notes:
        print("Pas de notes disponibles.")
        return

    indice_meilleur = notes.index(max(notes)) # Indice de la meilleure note.
    print(f"\nL'étudiant ayant la meilleure note est {noms[indice_meilleur]} avec {notes[indice_meilleur]}.")

if __name__ == "__main__":  
    noms, notes = saisir_donnees() # Saisie des données.
    print("\nDonnées saisies :")
    print("Noms :", noms) 
    print("Notes :", notes)
   
    moyenne = calculer_moyenne(notes) # Calcul de la moyenne.
    print(f"\nLa moyenne de la classe est de {moyenne:.2f}.")
    
    afficher_repartition(noms, notes) 
    
    meilleure_note(noms, notes)



