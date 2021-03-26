#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

from colorama import Fore
from develop.constants import Language
from develop.constants import SqlStatement


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
        selection = input('{}'.format(Language.do_selection))
        if selection == '1':
            return self.categories_page()
        elif selection == '2':
            return self.home_page()
        elif selection == 'q':
            return quit_software()
        else:
            print(Fore.RED + Language.bad_selection)
            return self.home_page()

    def categories_page(self):
        # Afficher la phrase 2: Sélectionez la categorie de l'aliment
        print(Fore.BLUE + Language.welcome_categories_title)
        # Afficher la liste de la class Categories de la méthode def select_categories():
        sql_statement = SqlStatement.sql_categories_selection
        dict_categories = self.bdd.get_query_results(sql_statement, ['pnns_groups_1'])
        for index, category in enumerate(dict_categories):
            print(Fore.YELLOW + '{}: {}'.format(index, category['pnns_groups_1']))
        print(Fore.YELLOW + Language.user_choice_categories_page)
        selection = input('{}'.format(Language.do_selection))
        if selection in ['0', '1', '2', '3']:
            return self.product_page(dict_categories[int(selection)])
        elif selection == 'q':
            return quit_software()
        elif selection == 'r':
            return self.home_page()
        else:
            print(Fore.RED + Language.bad_selection)
            return self.categories_page()

    def product_page(self, categorie_selectione):
        print(Fore.BLUE + Language.welcome_product_title)
        dict_products = self.bdd.get_query_results(SqlStatement.select_products_from_category % (categorie_selectione['pnns_groups_1']), ['generic_name_fr', 'nutrition_grade_fr'])
        for index, product in enumerate(dict_products):
            print(Fore.YELLOW + '{}: nom-{} nutriscore-({})'.format(index, product['generic_name_fr'],
                                                                  product['nutrition_grade_fr'],))
        print(Fore.YELLOW + Language.user_choice_product_page)

        selection = input('{}'.format(Language.do_selection))

        possibilities = [str(index) for index, _ in enumerate(dict_products)]
        if selection in possibilities:
            return self.substitute_page(dict_products[int(selection)], categorie_selectione)
        elif selection == 'q':
            return quit_software()
        elif selection == 'r':
            return self.categories_page()
        else:
            print(Fore.RED + Language.bad_selection)
            return self.product_page(categorie_selectione)

    def substitute_page(self, dict_products, categorie_selectione):
        print(Fore.BLUE + Language.welcome_substitute_title)
        if dict_products['nutrition_grade_fr'] in ['c', 'd', 'e']:
            substitute_score = ('a', 'b')

            dict_substitute = self.bdd.get_query_results(
                SqlStatement.select_substitute_from_product % (categorie_selectione['pnns_groups_1'], substitute_score),
                ['generic_name_fr', 'nutrition_grade_fr', 'url']
            )
            if len(dict_substitute) > 0:
                for index, product in enumerate(dict_substitute):
                    print(Fore.YELLOW + '{}: nom-{} nutriscore-({}) url-{}'.format(index, product['generic_name_fr'],
                                                        product['nutrition_grade_fr'], product['url']))
                print(Fore.YELLOW + Language.user_choice_substitute_page)

                selection = input('{}'.format(Language.do_selection))
                if selection == 's':
                    # TODO: Save favorite in table and back to home
                    return self.favorites.append(dict_substitute)
                elif selection == 'q':
                    return quit_software()
                else:
                    print(Fore.RED + Language.bad_selection)
                    return self.substitute_page(dict_products, categorie_selectione)
            else:
                print(Fore.YELLOW + Language.user_message_nonsubstitute)
                print(Fore.YELLOW + Language.user_choice_nonsubstitute)
                selection = input('{}'.format(Language.do_selection))
                if selection == '0':
                    return self.home_page()
                elif selection == 'q':
                    return quit_software()
                else:
                    print(Fore.RED + Language.bad_selection)
                    return self.home_page()
        else:
            print(Language.user_message_good_product)
            return self.home_page()
        print(self.favorites)

