#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

from enum import Enum


"""Sql command. Create tables Products, Categories, Favoris"""

create_tables_cmd = [
    "CREATE TABLE  Products("
    "code_products BIGINT,"
    "generic_name_fr VARCHAR(500),"
    "url VARCHAR(250),"
    "nutrition_grade_fr VARCHAR(5),"
    "stores VARCHAR (250),"
    "PRIMARY KEY (code_products)"
    ")ENGINE=INNODB;",

    "CREATE TABLE Categories("
    "code_categories BIGINT,"
    "pnns_groups_1 VARCHAR(500),"
    "code_products_fk BIGINT,"
    "PRIMARY KEY(code_categories),"
    "FOREIGN KEY (code_products_fk) REFERENCES Products(code_products)"
    ")ENGINE=INNODB;",

    "CREATE TABLE Favoris("
    "id_favoris INT AUTO_INCREMENT,"
    "code_products_fk BIGINT,"
    "PRIMARY KEY (id_favoris),"
    "FOREIGN KEY (code_products_fk)REFERENCES Products(code_products)"
    ")ENGINE=INNODB;"

]

"""Creating data base"""
infos_db = {
    'user': 'root',
    'password': 'Aukey2041!*',
    'host': '127.0.0.1'
}

"""Connexion to database"""
infos_db_purbeurre = {
    'user': 'root',
    'password': 'Aukey2041!*',
    'host': '127.0.0.1',
    'database': 'purbeurre'
}


"""Constants for API requests"""
# REMINDER: without space in fields
url_request = 'https://fr.openfoodfacts.org/cgi/search.pl'
products_params = {
    "action": "process",
    "sort_by": "unique_scans_n",
    "page_size": 500,
    "json": 1,
    "page": 1,
    "fields": "pnns_groups_1,generic_name_fr,"
              "code,url,nutrition_grade_fr,stores"
}


class Language (str, Enum):
    """
    class Language who defined the constants for messages
    that will be print on user display
    """

    """List of constants to print on home page"""
    welcome_home_title = "\n++++Page d'acceuil++++\n"
    description_purbeurre_title = "\npurbeurre est votre meilleur " \
                                  "compagnon sur le schéma " \
                                  "de la meilleur nutrition! \n"
    user_choice_home_page = "1: Quel aliment souhaitez-vous remplacer? " \
                            "\n2: Retrouver mes aliments substituts. \n " \
                            "" " \nq: Quitter le programme"

    """List of constants to print on Categories page"""
    welcome_categories_title = "\n ++++Page Categories++++ \n"
    message_error_pw = "Something is wrong with your user name or password"
    user_choice_categories_page = "\nq: Quitter le programme " \
                                  "\nr: Retour vers la page d'acceuil"

    """List of constants to print on Products page"""
    welcome_product_title = "\n ++++Page Produits++++ \n"
    user_choice_product_page = "\nq: Quitter le programme " \
                               "\nr: Retour vers la page de categories"

    """List of constants to print on Substitutes page"""
    welcome_substitute_title = "\n ++++Page Substituts++++ \n"
    user_choice_substitute_page = \
        "\nq: Quitter le programme " \
        "\ns: Sauvegarder le substitute dans mes favoris"
    user_message_nonsubstitute = \
        "Nous n'avons pas de substituts à vous proposer"
    user_choice_nonsubstitute = \
        "0: Retour au menu principal \nq: Quitter le programme"
    user_message_good_product = "Vous avez déjà un trés bon produit"

    """List of constants to print on saved Substitutes page"""
    welcome_saved_substitute_title = \
        "\n ++++Votre page de substituts sauvegardés++++ \n"
    user_choice_saved_substitute_page = \
        "\nq: Quitter le programme \nr: Retour vers la page d'acceuil"

    """List of generals constants to print"""
    bad_selection = "Mauvaise selection"
    do_selection = "Faites votre selection => "


class SqlStatement (str, Enum):
    """
    class SqlStatement who defined the commands SQL
    for work with data base
    """

    """Sql constants for use utf8"""
    use_utf8 = "SET NAMES utf8;"
    apply_utf8 = "SET CHARACTER SET utf8;"

    """Sql constants for interact with database"""
    create_purbeurre = "CREATE DATABASE purbeurre;"
    use_purbeurre = "USE purbeurre;"

    """Sql constants for sort and edit the tables"""
    sql_categories_selection = """SELECT DISTINCT pnns_groups_1 
    FROM Categories ORDER BY code_categories LIMIT 4"""
    insert_values_products_table = """INSERT INTO Products(generic_name_fr, 
            code_products, url, nutrition_grade_fr,stores) 
            VALUES (%s, %s, %s, %s, %s); """
    insert_values_categories_table = """INSERT INTO 
    Categories(pnns_groups_1, code_categories) VALUES (%s, %s);"""
    select_products_from_category = """SELECT DISTINCT generic_name_fr, 
    nutrition_grade_fr FROM Products 
            INNER JOIN Categories ON Products.code_products = Categories.code_categories 
            WHERE Categories.pnns_groups_1 = '%s' ORDER BY RAND() LIMIT 4"""
    select_substitute_from_product = """SELECT Products.code_products, generic_name_fr, 
    nutrition_grade_fr, stores, url  FROM Products
                        INNER JOIN Categories ON Products.code_products = Categories.code_categories
                        WHERE Categories.pnns_groups_1 = '%s'
                        AND nutrition_grade_fr in %s 
                        ORDER BY RAND() LIMIT 1"""

    select_favoris_from_product = """SELECT generic_name_fr,
    nutrition_grade_fr, stores, url  FROM Products
                        INNER JOIN Favoris ON
                        Products.code_products = Favoris.code_products_fk"""

    save_in_table_favoris = """INSERT INTO Favoris 
    (code_products_fk) VALUES ('%s'); """

    select_table_favoris = """SELECT * FROM Favoris; """
