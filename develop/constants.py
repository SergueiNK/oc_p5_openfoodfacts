#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

# Sql TABLE creation
# TODO: Add 'name' to product table
create_tables_cmd = [
    "CREATE TABLE  Products(id INT UNSIGNED AUTO_INCREMENT, generic_name_fr VARCHAR(250), product_name_fr_imported "
    "VARCHAR(250), ingredients_text_with_allergens_fr TEXT, code VARCHAR(50), url VARCHAR(250), nutrition_grade_fr "
    "VARCHAR(5), name VARCHAR(250),PRIMARY KEY (id) )ENGINE=INNODB;",
    "CREATE TABLE  Categories(id INT UNSIGNED AUTO_INCREMENT, pnns_groups_1 VARCHAR(500), code VARCHAR(50), PRIMARY KEY "
    "(id))ENGINE=INNODB;",
    "CREATE TABLE  Places_to_buy(id INT UNSIGNED AUTO_INCREMENT, stores VARCHAR (250), code VARCHAR(50), PRIMARY KEY "
    "(id))ENGINE=INNODB;",
    "CREATE TABLE  Favorites(id INT UNSIGNED AUTO_INCREMENT, generic_name_fr VARCHAR(250), product_name_fr_imported "
    "VARCHAR(250), ingredients_text_with_allergens_fr TEXT, code VARCHAR(50), url VARCHAR(250), nutrition_grade_fr "
    "VARCHAR(5), PRIMARY KEY (id))ENGINE=INNODB;",
    "ALTER TABLE Categories ADD CONSTRAINT fk_categories FOREIGN KEY (code) REFERENCES Products(code)"
]

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
              "ingredients_text_with_allergens_fr,code,url,nutrition_grade_fr,name"
}

# Creating data base
infos_db = {
    'user': 'root',
    'password': 'Server1438!*',
    'host': '127.0.0.1'
}

# Connexion to database

infos_db_purbeurre = {
    'user': 'root',
    'password': 'Server1438!*',
    'host': '127.0.0.1',
    'database': 'purbeurre'
}
