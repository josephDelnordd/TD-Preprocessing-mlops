# TD - Préparation et nettoyage de données avec Pandas & NumPy

## Auteur

Joseph DELNORD

## Module

Introduction à l'IA et au Machine Learning pour les DEV

## Objectifs du TD

Ce TD a pour objectif d'apprendre les principales étapes de préparation des données avant l'entraînement d'un modèle de Machine Learning :

- Manipulation de données avec Pandas
- Utilisation des Series et DataFrames
- Chargement de fichiers CSV
- Détection des valeurs manquantes
- Nettoyage des données
- Imputation avec Pandas
- Imputation avec Scikit-Learn
- Analyse et préparation de nouveaux datasets

---

## Structure du projet

```text
.
├── data/
│   ├── Custemers.csv
│   ├── olympics.csv
│   ├── flicker.csv
│   └── melb_data.csv
│
├── src/
│   ├── ex1_series.py
│   ├── ex2_load_csv.py
│   ├── ex3_missing_values.py
│   ├── ex4_cleaning.py
│   ├── ex5_imputation.py
│   ├── ex6_simple_imputer.py
│   └── ex7_strategy.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Créer un environnement virtuel :

```bash
python -m venv .venv
```

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

### Sortir de l'environnement virtuel

```bash
deactivate
```

---

## Lancement des exercices

### Exercice 1

```bash
python src/ex1_series.py
```

### Exercice 2

```bash
python src/ex2_load_csv.py
```

### Exercice 3

```bash
python src/ex3_missing_values.py
```

### Exercice 4

```bash
python src/ex4_cleaning.py
```

### Exercice 5

```bash
python src/ex5_imputation.py
```

### Exercice 6

```bash
python src/ex6_simple_imputer.py
```

### Exercice 7

```bash
python src/ex7_strategy.py
```

---

## Datasets utilisés

- Custemers.csv
- melb_data.csv
- olympics.csv
- flicker.csv

---

## Bibliothèques utilisées

- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Compétences travaillées

- Data Cleaning
- Data Exploration
- Gestion des valeurs manquantes
- Imputation
- Prétraitement des données
- Pipelines de préparation de données

---

## Résultat attendu

À l'issue du TD, les datasets doivent être :

- Explorés
- Nettoyés
- Vérifiés
- Dédupliqués
- Imputés lorsque nécessaire
- Prêts pour une utilisation dans un pipeline Machine Learning

---

## Remarques

- Assurez-vous que les fichiers CSV sont correctement placés dans le dossier `data/`.
- Vérifiez que l'environnement virtuel est activé avant d'exécuter les scripts.
- Les scripts Python sont conçus pour être exécutés de manière séquentielle, chaque exercice construisant sur le précédent.
