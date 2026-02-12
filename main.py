import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MotDePasseFort",
    database = "boutique_pro_historique"
)

if connection.is_connected():
    print("Base de donnee connecter")

#===========================MENU=======================================================

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

#==================================AJOUT CATEGORIE============================================

def ajout_cat():

    nom_cat = input("Entrez une categorie:")
    if not nom_cat.isalpha():
        print("Erreur de saisie")
        return
    cursor = connection.cursor()
    query = "insert into categories (nom_cat) values (%s)"
    cursor.execute(query, (nom_cat,))
    connection.commit()

#==================================MISE A JOUR QUANTITE PRODUIT===================================

def update_quantite():
    afficher_produits()
    
    id_pro = input("Entrez l'id du produit:")
    if not id_pro.isdigit():
        print("Erreur : id doit être un nombre.")
        return

    id_pro = int(id_pro)

    quantite = input("Entrez la quantite du produit:")
    if not quantite.isdigit():
        print("Erreur : la quantité doit être un nombre.")
        return

    quantite = int(quantite)
   
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

#===================================AJOUT MOUVEMENT=============================================

def ajouter_mouvement():

    id_produit = input("Entrer id produit : ").strip()
    if not id_produit.isdigit():
        print("Erreur : id invalide")
        return
    id_produit = int(id_produit)

    quantite = input("Entrer la quantite : ").strip()
    if not quantite.isdigit():
        print("Erreur : quantité invalide")
        return
    quantite = int(quantite)

    type_mouvement = input("Type (ENTREE/SORTIE) : ").strip().upper()
    if type_mouvement not in ["ENTREE", "SORTIE"]:
        print("Erreur : type invalide")
        return

    cursor = connection.cursor()

    query = "insert into mouvement (id_produit, quantite_mouv, type_mouvement) values (%s, %s, %s)"
    cursor.execute(query, (id_produit, quantite, type_mouvement))
    connection.commit()
    print("Mouvement mis à jour avec succès !")

#=================================AFFICHER MOUVEMENT============================================

def afficher_mouvement():
    cursor = connection.cursor()
    query = "select * from mouvement"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(f"id_mouv: {row[0]}| id_produit: {row[1]}| quantite: {row[2]}| type_mouvement: {row[3]}| date_mouvement: {row[4]}")

#=============================AFFICHER CATEGORIE==============================================

def afficher_cat():
    cursor = connection.cursor()
    query = "select * from categories"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(f"id_cat: {row[0]}| nom_cat: {row[1]}")

#==========================AJOUT CATEGORIE================================================

def ajout_produits():
    cursor = connection.cursor()
    nom_pro = input("Entrez le nom du produit:").strip()
    if len(nom_pro) < 2:
        print("Nom invalide")
        return

    prix = input("Entrez le prix:")
    try:
        prix = float(prix)
    except ValueError:
        print("Le prix doit être un nombre.")
        return

    
    etat = input("Entrez l'etat du produit:").strip()
    if not etat.isalpha():
        print("Erreur de saisie")
        return
    
    id_cat = input("Entrez id categorie:")
    cursor.execute("SELECT id_cat FROM categories WHERE id_cat = %s", (id_cat,))
    if not cursor.fetchone():
        print("Categorie inexistante")
        return

    quantite = input("Entrez quantite produit:")
    if not quantite.isdigit():
        print("Erreur de saisie")
        return   
    
    query = "insert into produits (nom_pro, prix, etat, id_cat, quantite) values (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nom_pro, prix, etat, id_cat, quantite))
    connection.commit()

#============================AFFICHER PRODUITS================================================

def afficher_produits():
    cursor = connection.cursor()
    query = "select * from produits"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(f"id_produit: {row[0]}| nom_pro: {row[1]}| prix: {row[2]}| Etat: {row[3]}| id_categorie: {row[4]}| quantite: {row[5]}")

#=================================AFFICHER LES PRODUITS PAR CATEGORIE========================================

def afficher_pro_nom_cat():
    cursor = connection.cursor()
    query = "select categories.nom_cat, produits.nom_pro from produits inner join categories on categories.id_cat = produits.id_cat"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(f"Nom categorie: {row[0]} | nom produits : {row[1]}")

#==============================ATOCK FAIBLE=================================================

def stock_faible():
    cursor = connection.cursor()
    query = "Select id_produit, quantite from produits where quantite < 5"
    cursor.execute(query)
    for row in cursor.fetchall():
        print(f"id_produit :{row[0]} stock : {row[1]}")
    
#==============================CHOIX MENU=========================================================

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

connection.close()