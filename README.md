# 🎓 Gestion des autorisations des étudiants

## 📌 Présentation du projet
Ce projet a été réalisé dans le cadre du cours d’Advanced Programming.

L’objectif est de créer un système permettant de gérer les autorisations des étudiants, notamment :
- les retards (entrée tardive)
- les sorties pendant les cours

Le programme permet également de générer automatiquement une autorisation et d’informer le professeur par email.

---

## 🧱 Organisation du projet

Le projet est divisé en plusieurs fichiers :

### 🔹 person.py
Ce fichier contient la classe **Person**, qui représente une personne avec :
- son nom
- son prénom
- son identifiant

C’est une classe de base utilisée pour construire d’autres objets.

---

### 🔹 student.py
Ce fichier contient la classe **Student**, qui hérite de `Person`.

Elle permet de gérer :
- la filière de l’étudiant
- l’heure d’entrée et de sortie
- la détection du retard

Une méthode permet aussi de vérifier si un étudiant est en retard et de combien de minutes.

---

### 🔹 bit_gestion.py
C’est le fichier principal du projet.

Il permet :
- de vérifier l’accès administrateur (mot de passe)
- de choisir le type d’autorisation (entrée ou sortie)
- de saisir les informations de l’étudiant
- de calculer le retard ou la durée d’absence
- d’afficher une autorisation claire
- d’envoyer un email au professeur

---

## ⚙️ Fonctionnement

1. L’administrateur entre le mot de passe  
2. Il choisit le type d’autorisation  
3. Il saisit les informations de l’étudiant  
4. Le programme effectue les calculs automatiquement  
5. Une autorisation est affichée et un email peut être envoyé  

---

## ▶️ Exécution du programme

Dans le terminal :

```bash
python bit_gestion.py# Groupe-10_Advanced-programming-python-and-c-

