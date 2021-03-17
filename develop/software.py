#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

class Display:
# Lancer le programme purbeurre

#def home_page():
# Afficher la phrase 1 : Purbeurre vous permet de choisir le substitut de vos aliments
# Afficher les 3 propositions suivantes:
    # 1. Quel aliment souhaitez-vous remplacer?
    # 2. Retrouver mes aliments substituts
    # 0.Quitter le programme

#Si l'utilisateur choisi 1. alors lui renvoyer la page des categories
#Si l'utilisateur choisi 2. alors lui renvoyer la table des substituts
# Su l'utilisateur choisi 0. alors fermer le programme

# def categories_page():

# Afficher la phrase 2: Sélectionez la categorie de l'aliment
# Afficher la liste de la class Categories de la méthode def select_categories():
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

# def substitute_page():

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


class Categories:

# def select_categories():

# Selection random de 8 categories differentes dans la Table Categories
# Mettre cette seléction dans une liste avec une numerotation de 1 à 8
# Nettoyer la liste aprés l'iteraction de l'utilisateur

class Product:

# def select_product():
# Selection random de 4 produits differents dans la Table de Produits selon la categorie
# Mettre cette seléction dans une liste avec une numerotation de 1 à 4 avec les noms de produits
# Nettoyer la liste aprés l'iteraction de l'utilisateur

class Substitute:

# def select_substitute ():

# Selon le produit choisi par l'utilisateur la methode va choisire le produit de la même classe
# mais avec nutriscore meilleur.
# Si la methode ne trouve pas de meilleur produit, elle renvoye alors Le MESSAGE: Nous n'avons pas de produits avec
# le meilleur nutriscore
# Si l'utilisateur choisi de sauvegarder le substitut dans la method def substitute_page () alors sauvegarder le substitut
# dans la table Favorites

# Si l'utilisateur choisi d'acceder à sa table de favorites selon la methode def home_page alors ouvrir la table de Favorites
