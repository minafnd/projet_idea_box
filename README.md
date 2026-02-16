# 📦 projet_idea_box

**projet_idea_box** est une application web développée avec **Python et Flask** permettant de gérer des idées ou événements via une interface web simple et intuitive.

Ce projet a été réalisé dans un contexte pédagogique afin de mettre en pratique le développement backend avec Flask, la gestion des routes, des templates et des fichiers statiques.

---

## 🧠 Fonctionnalités

- 💡 Ajouter une nouvelle idée
- 📄 Afficher la liste des idées enregistrées
- 🛣️ Exposition d'une route sous la forme d'une API/REST destinée à un usage futur 
- 🧩 Interface web dynamique avec Jinja2
- 🎨 Intégration HTML / CSS (TailwindCSS)
- 🚀 Application simple à exécuter en local

---

## 🛠️ Technologies utilisées

- **Python 3**
- **Flask**
- **Jinja2**
- **HTML5**
- **CSS3**

---

## 📁 Structure du projet

```
projet_idea_box/
│
├── app.py                 # Fichier principal Flask
├── requirements.txt       # Dépendances du projet
├── static/                # Fichiers statiques (CSS, images)
│   └── ...
├── instance/              # base de donnée SQLite
│   └── ...
├── templates/             # Templates HTML (Jinja2)
│   └── ...
├── .gitignore
└── README.md
```

---

## 📥 Installation

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/minafnd/projet_idea_box.git
cd projet_idea_box
```

### 2️⃣ Créer un environnement virtuel

```bash
python3 -m venv venv
```

### 3️⃣ Activer l’environnement virtuel

- **Mac / Linux**
```bash
source ./.venv/bin/activate
```

- **Windows**
```bash
source ./.venv/Scripts/activate
```

### 4️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ▶️ Lancer l’application

### Mac / Linux

```bash

flask run --debug
```

L’application sera accessible à l’adresse suivante :

```
http://127.0.0.1:5000/
```

---

## 🧪 Utilisation

1. Ouvrir l’application dans le navigateur.
2. Ajouter une nouvelle proposition d'évènement via le formulaire.
3. Visualiser les propositions enregistrées sur la page principale.
4. Supprimer une proposition.

---

## 📄 Licence

Aucune licence spécifiée pour le moment.  

---

## 👩‍💻 Auteur

Projet réalisé par moi-même, dans le cadre d’un apprentissage du développement web avec Flask.

---

