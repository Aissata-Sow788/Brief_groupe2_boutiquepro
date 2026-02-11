README – Gestion de Stock avec Historique – Boutique Pro
 Contexte du projet
Dans le cadre d’une structure solidaire (type Simplon), cette application permet de gérer un stock important de matériel informatique.
L’objectif est :
 Connaître le stock actuel

 Suivre chaque entrée et sortie de stock

Éviter les pertes ou vols

Organiser les produits par catégories

Détecter les produits en stock faible

L’application est développée en Python (backend) avec une base de données MySQL.
Structure de la base de données
Table categories
| Champ         | Type recommandé          | Description                                              |
| ------------- | ------------------------ | -------------------------------------------------------- |
| id_cat        | INT (PK, AUTO_INCREMENT) | Identifiant unique de la catégorie                       |
| nom_categorie | VARCHAR(100)             | Nom de la catégorie (Informatique, Papeterie, Mobilier…) |

Table : produits
| Champ      | Type          | Null | Clé    | Valeur par défaut | Extra          | Description                          |
| ---------- | ------------- | ---- | ------ | ----------------- | -------------- | ------------------------------------ |
| id_produit | INT           | NO   | 🔑 PRI | NULL              | AUTO_INCREMENT | Identifiant unique du produit        |
| nom_pro    | VARCHAR(100)  | NO   |        | NULL              |                | Nom du produit                       |
| prix       | DECIMAL(10,2) | NO   |        | NULL              |                | Prix du produit                      |
| etat       | VARCHAR(100)  | NO   |        | disponible        |                | État du produit                      |
| id_cat     | INT           | YES  | 🔗 MUL | NULL              |                | Référence vers la table `categories` |
| quantite   | INT           | YES  |        | 0                 |                | Quantité disponible en stock         |

Table : mouvements
| Champ          | Type                    | Null | Clé    | Valeur par défaut | Extra             | Description                          |
| -------------- | ----------------------- | ---- | ------ | ----------------- | ----------------- | ------------------------------------ |
| id_mouv        | INT                     | NO   | 🔑 PRI | NULL              | AUTO_INCREMENT    | Identifiant unique du mouvement      |
| id_produit     | INT                     | NO   | 🔗 MUL | NULL              |                   | Référence vers le produit concerné   |
| quantite       | INT                     | NO   |        | NULL              |                   | Quantité ajoutée ou retirée          |
| type_mouvement | ENUM('ENTREE','SORTIE') | NO   |        | NULL              |                   | Type de mouvement (entrée ou sortie) |
| date_mouvement | DATETIME                | YES  |        | CURRENT_TIMESTAMP | DEFAULT_GENERATED | Date et heure du mouvement           |

Table : produits
+------------+---------+-----------+------------+--------+----------+
| id_produit | nom_pro | prix      | etat       | id_cat | quantite |
+------------+---------+-----------+------------+--------+----------+
|          1 | Dell    | 160000.00 | disponible |      1 |        0 |
|          2 | clavier |   3000.00 | disponible |      1 |        0 |
|          3 | Disque  |  15000.00 | disponible |      1 |        5 |
+------------+---------+-----------+------------+--------+----------+

Fonctionnalités
 Gestion des catégories

Ajouter une catégorie

Lister les catégories

Gestion des produits

Ajouter un produit associé à une catégorie existante

Afficher tous les produits

Afficher les produits avec leur catégorie (JOIN)

Modifier la quantité d’un produit

Gestion des mouvements

Ajouter une entrée ou une sortie de stock

Historiser automatiquement chaque mouvement

Afficher l’historique des mouvements

 Alerte Stock Faible

Afficher les produits dont le stock est inférieur à 5 unités

Logique métier

Chaque produit est obligatoirement lié à une catégorie

Les mouvements permettent de tracer toutes les opérations

Le stock faible est détecté dynamiquement

Les relations entre tables sont gérées avec des clés étrangères

Technologies utilisées

Python 3

MySQL

mysql-connector-python

Installation :

pip install mysql-connector-python

🚀 Lancer le projet

Créer la base de données :

CREATE DATABASE boutique_pro_historique;


Créer les tables.

Modifier les paramètres de connexion dans le fichier Python :

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MotDePasseFort",
    database="boutique_pro_historique"
)


Lancer le script :

python main.py

📋 Menu principal
1: Ajouter categories
2: Afficher categories
3: Ajouter produits par categorie
4: Afficher produits
5: Ajouter mouvement
6: Modifier une quantite produits
7: Afficher produits par categorie
8: Afficher historique mouvement
9: Stock faible

J'ai creer un triggers dans la base de donne dans le terminal pour gerer le mouvement quand on insert un mouvement sa met automatiquement a jour la quantite produit par entree ou sortie
CREATE TRIGGER apres_insert_mouvement
    -> AFTER INSERT ON mouvement
    -> FOR EACH ROW
    -> BEGIN
    ->     IF NEW.type_mouvement = 'ENTREE' THEN
    ->         UPDATE produits
    ->         SET quantite = quantite + NEW.quantite_mouv
    ->         WHERE id_produit = NEW.id_produit;
    -> 
    ->     ELSEIF NEW.type_mouvement = 'SORTIE' THEN
    ->         UPDATE produits
    ->         SET quantite = quantite - NEW.quantite_mouv
    ->         WHERE id_produit = NEW.id_produit;
    -> 
    ->     END IF;
    -> END$$



