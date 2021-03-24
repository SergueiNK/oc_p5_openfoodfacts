#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

from colorama import Fore
from services.bdd import get_bdd_connector
import time


def quit_software():
    exit()


class Display:
    # Lancer le programme purbeurre
    bdd_connection = None
    favorites = []

    def __init__(self):
        self.bdd_connection = get_bdd_connector()
        self.home_page()

    def home_page(self):
        # Afficher la phrase 1 : Purbeurre est votre meilleur compagnon sur le schéma de la meilleur nutrition
        print(Fore.BLUE + "\n++++Page d'acceuil++++\n")
        print(Fore.GREEN + "\nPurbeurre est votre meilleur compagnon sur le schéma de la meilleur nutrition! \n")
        print(Fore.YELLOW + "1: Quel aliment souhaitez-vous remplacer? \n2: Retrouver mes aliments substituts. \n "
                            "\nq: Quitter le programme")
        selection = input("Faites votre selection")
        if selection == '1':
            return self.categories_page()
        elif selection == '2':
            print(self.favorites)
            return self.home_page()
        elif selection == 'q':
            return quit_software()
        else:
            print(Fore.RED + "Mauvaise selection")
            return self.home_page()

    def categories_page(self):
        # Afficher la phrase 2: Sélectionez la categorie de l'aliment
        print(Fore.BLUE + "\n ++++Page Categories++++ \n")
        # Afficher la liste de la class Categories de la méthode def select_categories():
        cursor = self.bdd_connection.cursor()
        cursor.execute("""SELECT DISTINCT pnns_groups_1 FROM Categories ORDER BY RAND() LIMIT 4""")
        dict_categories = cursor.fetchall()
        print(dict_categories)
        categories = []
        for index, category in enumerate(dict_categories):
            # category is a tuple
            string_category = [''.join(item) for item in category][0]
            categories.append(string_category)
            print(Fore.YELLOW + '{}: {}'.format(index, string_category))
        print(Fore.YELLOW + "\nq: Quitter le programme \nr: Retour vers la page d'acceuil")
        selection = input("Faites votre selection")
        if selection in ['0', '1', '2', '3']:
            categorie_selectione = categories[int(selection)]
            return self.product_page(categorie_selectione)
        elif selection == 'q':
            return quit_software()
        elif selection == 'r':
            return self.home_page()
        else:
            print (Fore.RED + "Mauvaise selection")
            return self.categories_page()

    def product_page(self, categorie_selectione):
        print(Fore.BLUE + "\n ++++Page Produits++++ \n")
        cursor = self.bdd_connection.cursor()
        cursor.execute(f"""SELECT generic_name_fr, nutrition_grade_fr FROM Products 
        INNER JOIN Categories ON Products.code = Categories.code 
        WHERE Categories.pnns_groups_1 = '{categorie_selectione}' ORDER BY RAND() LIMIT 4""")
        dict_product = cursor.fetchall()
        print(dict_product)
        # nutrition_grade_fr_product = cursor.fetchall()
        # print(nutrition_grade_fr_product)
        string_product = []
        for index, product in enumerate(dict_product):
            # category is a tuple
            string_product = [''.join(item) for item in product][0]
            print(string_product)
            print(Fore.YELLOW + '{}: {}'.format(index, string_product))
        print(Fore.YELLOW + "\nq: Quitter le programme \nr: Retour vers la page de categories")

        selection = input("Faites votre selection")
        print("votre choix >>> {}".format(selection))

        if selection in ['0','1','2','3']:
            print(string_product)
            product_selectione = string_product[int(selection)]
            print(product_selectione)
            return self.substitute_page(product_selectione, categorie_selectione)
        elif selection == 'q':
            return quit_software()
        elif selection == 'r':
            return self.categories_page()
        else:
            print (Fore.RED + "Mauvaise selection")
            return self.product_page(None)

    def substitute_page(self, product_selectione, categorie_selectione):
        print(Fore.BLUE + "\n ++++Page Substituts++++ \n")
        cursor = self.bdd_connection.cursor()
        print(f"""SELECT generic_name_fr FROM Products
                    INNER JOIN Categories ON Products.code = Categories.code
                    WHERE Categories.pnns_groups_1 = '{categorie_selectione}'
                        AND nutrition_grade_fr > '{product_nutrition_grade}' ORDER BY RAND() LIMIT 4""")
        cursor.execute(f"""SELECT generic_name_fr FROM Products
                    INNER JOIN Categories ON Products.code = Categories.code
                    WHERE Categories.pnns_groups_1 = '{categorie_selectione}'
                        AND nutrition_grade_fr > '{product_nutrition_grade}' ORDER BY RAND() LIMIT 4""")
        dict_substitute = cursor.fetchall()
        print(dict_substitute)
        string_substitute = []
        print(categorie_selectione)
        print(product_selectione)
        for index, product in enumerate(dict_substitute):
            # category is a tuple
            string_substitute = [''.join(item) for item in product][0]
            print(string_substitute)
            print(Fore.YELLOW + '{}: {}'.format(index, string_substitute))
        print(Fore.YELLOW + "\nq: Quitter le programme \nr: Retour vers la page de categories")

        selection = input("Faites votre selection")
        print("votre choix >>> {}".format(selection))

        if selection in ['0']:
            substitute_selectione = string_substitute[int(selection)]
            print(substitute_selectione)
            # return self.substitute_page()
        elif selection == 'q':
            return quit_software()
        elif selection == 'r':
            return self.categories_page()
        else:
            print(Fore.RED + "Mauvaise selection")
            return self.product_page(None)

