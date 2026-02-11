import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MotDePasseFort",
    database = "boutique_pro_historique"
)

if connection.is_connected():
    print("Base de donnee connecter")


def menu():
    print("======================MENU======================")
    print("1: Ajouter categories")
    print("2: Afficher categories")
    print("3: Ajouter produits par categorie")
    print("4: Afficher produits")
    print("5: Ajouter mouvement")
    print("6: Modifier une quantite produits")
    print("7: Afficher produits par categorie")
    print("8: Afficher historique mouvement")
    print("9: Stock faible")
    print("=================================================")

def ajout_cat():

    nom_cat = input("Entrez une categorie:")
    if not nom_cat.isalpha():
        print("Erreur de saisie")
        return
    cursor = connection.cursor()
    query = "insert into categories (nom_cat) values (%s)"
    cursor.execute(query, (nom_cat,))
    connection.commit()


def update_quantite():
    afficher_produits()
    
    id_pro = int(input("Entrez l'id du produit:")).strip()

    quantite = int(input("Entrez la quantite du produit:"))
   
    cursor = connection.cursor()
    
    cursor.execute("select * from produits where id_produit = %s", (id_pro,))
    produit = cursor.fetchone()
    if not produit:
        print("produit existe pas")

    id_prod = produit[0]

    query = "update produits set quantite = %s where id_produit = %s"
    cursor.execute(query, (quantite, id_prod))
    connection.commit()
    print("Ajouter avec succes")


def ajouter_mouvement():
    id_produit = (input("Entrer id produit : "))
    quantite = int(input("Entrer la quantite : "))
    type_mouvement = input("Type (ENTREE/SORTIE) : ")

    cursor = connection.cursor()

    query = "insert into mouvement (id_produit, quantite_mouv, type_mouvement) values (%s, %s, %s)"
    cursor.execute(query, (id_produit, quantite, type_mouvement))
    connection.commit()
    print("Mouvement mis à jour avec succès !")

def afficher_mouvement():
    cursor = connection.cursor()
    query = "select * from mouvement"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)


def afficher_cat():
    cursor = connection.cursor()
    query = "select * from categories"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

def ajout_produits():
    nom_pro = input("Entrez le nom du produit:").strip()
    if not nom_pro.isalpha():
        print("Erreur de saisie")
        return
    prix = input("Entrez le prix:")
    if not prix.isdigit():
        print("Erreur de saisie")
        return
    
    etat = input("Entrez l'etat du produit:").strip()
    if not etat.isalpha():
        print("Erreur de saisie")
        return
    id_cat = input("Entrez id categorie:")
    if not id_cat.isdigit():
        print("Erreur de saisie")
        return
    quantite = input("Entrez id categorie:")
    if not quantite.isdigit():
        print("Erreur de saisie")
        return   
    cursor = connection.cursor()
    
    
    query = "insert into produits (nom_pro, prix, etat, id_cat, quantite) values (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nom_pro, prix, etat, id_cat, quantite))
    connection.commit()

def afficher_produits():
    cursor = connection.cursor()
    query = "select * from produits"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

def afficher_pro_nom_cat():
    cursor = connection.cursor()
    query = "select categories.nom_cat, produits.nom_pro from produits inner join categories on categories.id_cat = produits.id_cat"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(f"Nom categorie: {row[0]} | nom produits : {row[1]}")


def stock_faible():
    cursor = connection.cursor()
    query = "Select id_produit, quantite from produits where quantite < 5"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(f"id_produit :{row[0]} stock : {row[1]}")
    


def choix():
    while True:
        menu()
        choix = input("Entrez votre choix:")
        if choix == "1":
            ajout_cat()
        elif choix == "2":
            afficher_cat()
        elif choix == "3":
            ajout_produits()
        elif choix == "4":
            afficher_produits()
        elif choix == "5":
            ajouter_mouvement()
        elif choix == "6":
            update_quantite()
        elif choix == "7":
            afficher_pro_nom_cat()
        elif choix == "8":
            afficher_mouvement()
        elif choix == "9":
            stock_faible()
        else:
            print("erreur")
choix()