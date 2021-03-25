#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

from colorama import Fore
from develop.constants import Language


def quit_software():
    exit()


class Display:
    # Lancer le programme purbeurre
    favorites = []

    def __init__(self, bdd):
        self.bdd = bdd
        self.home_page()

    def home_page(self):
        # Afficher la phrase 1 : Purbeurre est votre meilleur compagnon sur le schéma de la meilleur nutrition
        print(Fore.BLUE + Language.welcome_home_title)
        print(Fore.GREEN + Language.description_purbeurre_title)
        print(Fore.YELLOW + Language.user_choice_home_page)
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
        print(Fore.BLUE + Language.welcome_categories_title)
        # Afficher la liste de la class Categories de la méthode def select_categories():
        sql_statement = Language.sql_categories_selection
        dict_categories = self.bdd.get_query_results(sql_statement, ['pnns_groups_1'])
        for index, category in enumerate(dict_categories):
            print(Fore.YELLOW + '{}: {}'.format(index, category['pnns_groups_1']))
        print(Fore.YELLOW + Language.user_choice_categories_page)
        selection = input("Faites votre selection")
        if selection in ['0', '1', '2', '3']:
            return self.product_page(dict_categories[int(selection)])
        elif selection == 'q':
            return quit_software()
        elif selection == 'r':
            return self.home_page()
        else:
            print(Fore.RED + "Mauvaise selection")
            return self.categories_page()

    def product_page(self, categorie_selectione):
        print(Fore.BLUE + Language.welcome_product_title)
        sql_statement = f"""SELECT DISTINCT generic_name_fr, nutrition_grade_fr FROM Products 
        INNER JOIN Categories ON Products.code = Categories.code 
        WHERE Categories.pnns_groups_1 = '{categorie_selectione['pnns_groups_1']}' ORDER BY RAND() LIMIT 4"""
        dict_products = self.bdd.get_query_results(sql_statement, ['generic_name_fr', 'nutrition_grade_fr'])
        for index, product in enumerate(dict_products):
            print(Fore.YELLOW + '{}: nom-{} nutriscore-({})'.format(index, product['generic_name_fr'],
                                                                  product['nutrition_grade_fr'],))
        print(Fore.YELLOW + "\nq: Quitter le programme \nr: Retour vers la page de categories")

        selection = input("Faites votre selection")
        print("votre choix >>> {}".format(selection))
        # TODO: add in display ex: nutrition_grade_fr:a
        if selection in ['0', '1', '2', '3']:
            return self.substitute_page(dict_products[int(selection)], categorie_selectione)
        elif selection == 'q':
            return quit_software()
        elif selection == 'r':
            return self.categories_page()
        else:
            print (Fore.RED + "Mauvaise selection")
            return self.product_page(categorie_selectione)

    def substitute_page(self, dict_products, categorie_selectione):
        print(Fore.BLUE + "\n ++++Page Substituts++++ \n")
        if dict_products['nutrition_grade_fr'] in ['c', 'd', 'e']:
            substitute_score = ('a', 'b')
            sql_statement = f"""SELECT generic_name_fr, nutrition_grade_fr, url FROM Products
                    INNER JOIN Categories ON Products.code = Categories.code
                    WHERE Categories.pnns_groups_1 = '{categorie_selectione['pnns_groups_1']}'
                    AND nutrition_grade_fr in {substitute_score} ORDER BY RAND() LIMIT 1"""
            dict_substitute = self.bdd.get_query_results(sql_statement,
                                                         ['generic_name_fr', 'nutrition_grade_fr', 'url'])
            print(dict_substitute)
            if len(dict_substitute) > 0:
                for index, product in enumerate(dict_substitute):
                # TODO: add in print 'nutrition_grade_fr', 'url'
                    print(Fore.YELLOW + '{}: nom-{} nutriscore-({}) url-{}'.format(index, product['generic_name_fr'],
                                                        product['nutrition_grade_fr'], product['url']))
                print(Fore.YELLOW + "\nq: Quitter le programme \ns: Sauvegarder le substitute dasn mes favoris")

                selection = input("Faites votre selection")
                print("votre choix >>> {}".format(selection))
                if selection in ['0']:
                    print('ok')
                # TODO: save in favorites et return to home
                elif selection == 's':
                    # TODO: print to see that the append of favorites is ok
                    return self.favorites.append(dict_substitute)
                elif selection == 'q':
                    return quit_software()
                else:
                    print(Fore.RED + "Mauvaise selection")
                    return self.substitute_page(dict_products, categorie_selectione)
            else:
                # TODO: add case if none substitute product
                print ("Nous n'avons pas de substituts à vous proposer")
                print(
                    Fore.YELLOW + "0: Retour au menu principal \nq: Quitter le programme")
                selection = input("Faites votre selection")
                if selection == '0':
                    return self.home_page()
                elif selection == 'q':
                    return quit_software()
                else:
                    print(Fore.RED + "Mauvaise selection")
                    return self.home_page()
        else:
            print("Vous avez déjà un trés bon produit")
            return self.home_page()
        print(self.favorites)

