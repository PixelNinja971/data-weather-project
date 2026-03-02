# Weather Data Engineering Project

## 📌 Description
Ce projet est un mini système de Data Engineering permettant de collecter des données météo via une API publique, de les transformer afin de ne conserver que les informations utiles, puis de les stocker dans une base de données SQL.

Il a pour objectif de démontrer les bases d’un pipeline data simple : collecte, transformation et stockage.

---

## 🧱 Architecture du projet

- `api.py` : récupération des données météo via une API REST
- `transform.py` : transformation et nettoyage des données brutes
- `database.py` : création de la base de données et insertion des données
- `main.py` : orchestration complète du pipeline

---

## ⚙️ Technologies utilisées

- Python
- API REST (OpenWeather)
- SQL (SQLite)
- Git

---

## ▶️ Exécution du projet

1. Créer et activer un environnement virtuel
2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt

## Ajouter une clé API OpenWeather dans un fichier .env :
API_KEY=your_api_key_here
 
 ## Lancer le programme :
python src/main.py
