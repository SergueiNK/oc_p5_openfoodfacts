#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

from colorama import Fore
from services.bdd import get_bdd_connector
import time

class Display:
# Lancer le programme purbeurre
    bdd_connection = None

    def __init__(self):
        self.bdd_connection = get_bdd_connector()
        self.home_page()


    def home_page(self):
            #Afficher la phrase 1 : Purbeurre est votre meilleur compagnon sur le schéma de la meilleur nutrition
        print(Fore.BLUE + "\n++++Page d'acceuil++++\n")
        print(Fore.GREEN + "\nPurbeurre est votre meilleur compagnon sur le schéma de la meilleur nutrition! \n")

        print(Fore.YELLOW + "1. Quel aliment souhaitez-vous remplacer? \n2. Retrouver mes aliments substituts. \n0.Quitter le programme")

        selection = input("Faites votre selection")
        print("votre choix >>> {}".format(selection))
        if selection == '1':
            return self.categories_page()
        elif selection == '2':
            return self.substitute_page()
        elif selection == '0':
            return self.quit_software()
        else:
            print (Fore.RED + "Mauvaise selection")
            return self.home_page()

# Afficher les 3 propositions suivantes:s
    # 1. Quel aliment souhaitez-vous remplacer?
    # 2. Retrouver mes aliments substituts
    # 0.Quitter le programme

#Si l'utilisateur choisi 1. alors lui renvoyer la page des categories
#Si l'utilisateur choisi 2. alors lui renvoyer la table des substituts
# Su l'utilisateur choisi 0. alors fermer le programme

    def categories_page(self):

# Afficher la phrase 2: Sélectionez la categorie de l'aliment
        print(Fore.BLUE + "\n ++++Page Categories++++ \n")
# Afficher la liste de la class Categories de la méthode def select_categories():
        cursor = self.bdd_connection.cursor()
        cursor.execute("""SELECT DISTINCT categories FROM categories ORDER BY RAND() LIMIT 4""")
        dict_categories = cursor.fetchall()
        print(dict_categories)
        for category in dict_categories:
            # category is a tuuple
            print(category)

# Rajouter  à la liste les propositions 9. et 0.
    # Afficher les 10 propositions suivantes:
    # 1. Categorie 1 (nom)
    # 2. Categorie 2 (nom)
    # 3....8 Categories
    # 9. Retour vers la page d'acceuil
    # 0. Fermer le programme

# Si l'utilisateur choisi 1...8 alors lui renvoyer la page des produits de la categorie
# Si l'utilisateur choisi 9 alors revenir sur la page d'acceuil
# Si l'utilisateur choisi 0 alors fermer le programme

# def product_page():

# Afficher la phrase 3: Selectionez le produit
# Afficher les 6 propositions suivantes:
# 1.Product 1 (nom)
# 2.Product 2 (nom)
# 3..4 Products (nom)
# 9. Retour vers la page d'acceuil
# 0. Fermer le programme

#  Si l'utilisateur choisi 1...4 alors lui renvoyer la produit de substitut. Faire appel à la methode choisir
# substit de la class substitute
# Si l'utilisateur choisi 9 alors revenir sur la page d'acceuil
# Si l'utilisateur choisi 0 alors fermer le programme

    def substitute_page(self):
        print("substitute_page")

# Afficher la phrase 4: Voici votre produit de substitution que voulez vous en faire?
# Afficher le substitut avec les informations completes d'un product( name, store, .....)
# Afficher les propositions suivantes:
# 1. Sauvegarder substitut dans mes favoris
# 2. Retour vers la page d'acceuil
# 9. Retour vers la page des produits
# 0. Fermer le programme

# Si l'utilisateur choisi 1. alors renvoyer vers la methode de sauvegarde de la class Substitute
# Si l'utilisateur choisi 2. alors retourner vers la page d'acceuil
# Si l'utilisateur choisi 9. alors retourner vers la page des produits
# Si l'utilisateur choisi 0. alors fermer le programme

    def quit_software(self):
        exit()
# Quitter le programme

class Categories:
    pass

# def select_categories():

# Selection random de 8 categories differentes dans la Table Categories
# Mettre cette seléction dans une liste avec une numerotation de 1 à 8
# Nettoyer la liste aprés l'iteraction de l'utilisateur

class Product:
    pass

# def select_product():
# Selection random de 4 produits differents dans la Table de Produits selon la categorie
# Mettre cette seléction dans une liste avec une numerotation de 1 à 4 avec les noms de produits
# Nettoyer la liste aprés l'iteraction de l'utilisateur

class Substitute:
    pass

# def select_substitute ():

# Selon le produit choisi par l'utilisateur la methode va choisire le produit de la même classe
# mais avec nutriscore meilleur.
# Si la methode ne trouve pas de meilleur produit, elle renvoye alors Le MESSAGE: Nous n'avons pas de produits avec
# le meilleur nutriscore
# Si l'utilisateur choisi de sauvegarder le substitut dans la method def substitute_page () alors sauvegarder le substitut
# dans la table Favorites

# Si l'utilisateur choisi d'acceder à sa table de favorites selon la methode def home_page alors ouvrir la table de Favorites
