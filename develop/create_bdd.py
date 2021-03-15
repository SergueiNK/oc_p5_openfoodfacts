#!/usr/bin/python3.9
# -*-coding:utf-8 -

import requests
import mysql.connector
from mysql.connector import errorcode
import json

# import bdd.sql

# récuperation de l'API


# def api_request():
#     try:
#         url_request = 'https://fr.openfoodfacts.org/cgi/search.pl'
#         params = {
#             "action": "process",
#             "sort_by": "unique_scans_n",
#             "page_size": 50,
#             "json": 1,
#             "page": 1,
#             "fields": "generic_name_fr,product_name_fr_imported,ingredients_text_with_allergens_fr,"
#                       "code, url, nutrition_grade_fr"
#         }
#         response = json.loads(requests.get(url_request, params).text)
#         print(response.get('products'))
#         print(len(response.get('products')))
#     except Exception as e:
#         print(e)


try:
    infos_db = {
              'user': 'serguei',
              'password': 'Made1609!*',
              'host': '127.0.0.1',
              'database': 'Purbeurre'
              }
    connexion = mysql.connector.connect(**infos_db)
    connexion.close()
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    connexion.close()






# def create_tables():
#     mysql.cursor.execute("""SET NAMES utf8mb4;""")
#     mysql.cursor.execute("""CREATE TABLE [IF NOT EXISTS] Food(
#         id INT UNSIGNED AUTO_INCREMENT,
#         generic_name_fr VARCHAR(250),
#         product_name_fr_imported VARCHAR(250),
#         ingredients_text_with_allergens_fr TEXT,
#         code INT UNSIGNED,
#         url VARCHAR(250),
#         nutrition_grade_fr VARCHAR(5),
#         PRIMARY KEY (id)
#         )ENGINE=INNODB;""")
#     insert_stmt = (
#
#     )
#
#     mysql.cursor.execute("""CREATE TABLE [IF NOT EXISTS] Category(
#         id INT UNSIGNED AUTO_INCREMENT,
#         categories VARCHAR(250),
#         code INT UNSIGNED,
#         PRIMARY KEY (id)
#         )ENGINE=INNODB;""")
#
#     mysql.cursor.execute("""CREATE TABLE [IF NOT EXISTS] Place_to_buy(
#         id INT UNSIGNED AUTO_INCREMENT,
#         stores VARCHAR (250),
#         code INT UNSIGNED,
#         PRIMARY KEY (id)
#         )ENGINE=INNODB;""")
#
#     mysql.cursor.execute("""CREATE TABLE [IF NOT EXISTS] Favorites(
#         id INT UNSIGNED AUTO_INCREMENT,
#         generic_name_fr VARCHAR(250),
#         product_name_fr_imported VARCHAR(250),
#         ingredients_text_with_allergens_fr TEXT,
#         code INT UNSIGNED,
#         url VARCHAR(250),
#         nutrition_grade_fr VARCHAR(5),
#         PRIMARY KEY (id)
#         )ENGINE=INNODB;""")
#
#     mysql.cursor.execute("""ALTER TABLE Category ADD CONSTRAINT fk_code FOREIGN KEY (code) REFERENCES Category(code)""")
