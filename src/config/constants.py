#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

# Sql TABLE creation
# TODO: Delete the TABLE Place_to_buy
from enum import Enum


create_tables_cmd = [
    "CREATE TABLE  Products(id INT UNSIGNED AUTO_INCREMENT, generic_name_fr VARCHAR(250), product_name_fr_imported "
    "VARCHAR(250), ingredients_text_with_allergens_fr TEXT, code VARCHAR(50), url VARCHAR(250), nutrition_grade_fr "
    "VARCHAR(5), name VARCHAR(250), stores VARCHAR (250), PRIMARY KEY (id) )ENGINE=INNODB;",
    "CREATE TABLE  Categories(id INT UNSIGNED AUTO_INCREMENT, pnns_groups_1 VARCHAR(500), code VARCHAR(50), PRIMARY KEY "
    "(id))ENGINE=INNODB;",
    "CREATE TABLE Favoris(id INT UNSIGNED AUTO_INCREMENT, generic_name_fr VARCHAR(250), nutrition_grade_fr VARCHAR(5), url VARCHAR(250), PRIMARY KEY (id));",
    "ALTER TABLE Categories ADD CONSTRAINT fk_categories FOREIGN KEY (id) REFERENCES Products(id);"
]

# Creating data base
infos_db = {
    'user': 'root',
    'password': 'Aukey2041!*',
    'host': '127.0.0.1'
}

# Connexion to database

infos_db_purbeurre = {
    'user': 'root',
    'password': 'Aukey2041!*',
    'host': '127.0.0.1',
    'database': 'purbeurre'
}


# Constants for API requests
# REMINDER: pas d'espaces dans les fields
url_request = 'https://fr.openfoodfacts.org/cgi/search.pl'
products_params = {
    "action": "process",
    "sort_by": "unique_scans_n",
    "page_size": 50,
    "json": 1,
    "page": 1,
    "fields": "pnns_groups_1,stores,generic_name_fr,product_name_fr_imported,"
              "ingredients_text_with_allergens_fr,code,url,nutrition_grade_fr,name,stores"
}


class Language (str, Enum):
    welcome_home_title = "\n++++Page d'acceuil++++\n"
    description_purbeurre_title = "\nPurbeurre est votre meilleur compagnon sur le schéma de la meilleur nutrition! \n"
    user_choice_home_page = "1: Quel aliment souhaitez-vous remplacer? \n2: Retrouver mes aliments substituts. \n " " \nq: Quitter le programme"

    welcome_categories_title = "\n ++++Page Categories++++ \n"
    message_error_pw = "Something is wrong with your user name or password"
    user_choice_categories_page = "\nq: Quitter le programme \nr: Retour vers la page d'acceuil"

    welcome_product_title = "\n ++++Page Produits++++ \n"
    user_choice_product_page = "\nq: Quitter le programme \nr: Retour vers la page de categories"

    welcome_substitute_title = "\n ++++Page Substituts++++ \n"
    user_choice_substitute_page = "\nq: Quitter le programme \ns: Sauvegarder le substitute dans mes favoris"
    user_message_nonsubstitute = "Nous n'avons pas de substituts à vous proposer"
    user_choice_nonsubstitute = "0: Retour au menu principal \nq: Quitter le programme"
    user_message_good_product = "Vous avez déjà un trés bon produit"

    bad_selection = "Mauvaise selection"
    do_selection = "Faites votre selection => "


class SqlStatement (str, Enum):

    sql_categories_selection = """SELECT DISTINCT pnns_groups_1 FROM Categories ORDER BY RAND() LIMIT 4"""
    use_utf8 = "SET NAMES utf8;"
    apply_utf8 = "SET CHARACTER SET utf8;"
    create_purbeurre = "CREATE DATABASE purbeurre;"
    use_purbeurre = "USE purbeurre;"
    drop_purbeurre = "DROP DATABASE purbeurre;"
    insert_values_products_table = """INSERT INTO Products(generic_name_fr,product_name_fr_imported, 
            ingredients_text_with_allergens_fr,code, url, nutrition_grade_fr, name, stores) VALUES (%s, %s, %s, %s, %s, %s, %s, %s); """
    insert_values_categories_table = """INSERT INTO Categories(pnns_groups_1, code) VALUES (%s, %s);"""
    select_products_from_category = """SELECT DISTINCT generic_name_fr, nutrition_grade_fr FROM Products 
            INNER JOIN Categories ON Products.code = Categories.code 
            WHERE Categories.pnns_groups_1 = '%s' ORDER BY RAND() LIMIT 4"""
    select_substitute_from_product = """SELECT generic_name_fr, nutrition_grade_fr, url FROM Products
                        INNER JOIN Categories ON Products.code = Categories.code
                        WHERE Categories.pnns_groups_1 = '%s'
                        AND nutrition_grade_fr in %s ORDER BY RAND() LIMIT 1"""

    save_in_table_favoris = """INSERT INTO Favoris (generic_name_fr, nutrition_grade_fr, url) VALUES ('%s', '%s', '%s'); """
    select_table_favoris = """SELECT * FROM Favoris"""