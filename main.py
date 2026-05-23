# ==========================================
# PRG1406 - Programmation Avancée
# Partie 2 : Classe Personne
# Membre 2
# ==========================================

class Personne:
    def __init__(self, nom, prenom, id):
        self.nom = nom
        self.prenom = prenom
        self.id = id


# =========================
# Test de la classe
# =========================

personne1 = Personne("NANA", "Prisca", 101)

print("Informations de la personne :")
print(f"Nom : {personne1.nom}")
print(f"Prénom : {personne1.prenom}")
print(f"ID : {personne1.id}")