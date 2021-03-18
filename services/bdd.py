#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

import mysql.connector as mysql
from mysql.connector import errorcode
from develop.constants import infos_db_purbeurre, infos_db, create_tables_cmd
from services.api import api_get_products


def init_database():
    try:
        connexion = mysql.connect(**infos_db_purbeurre)
        connexion.close()
    except mysql.Error as err:
        # TODO: Gérer les erreurs plus proprement
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == 1049:
            create_database()
        else:
            raise err


def create_database():
    connector = mysql.connect(**infos_db)
    cursor = connector.cursor()
    cursor.execute("SET NAMES utf8;")
    cursor.execute("CREATE DATABASE purbeurre;")
    cursor.execute("USE purbeurre;")
    try:
        for cmd in create_tables_cmd:
            # create the tables
            cursor.execute(cmd)
        insert_in_tables(connector)
        connector.close()
    except Exception as e:
        # In case of pb drop the database
        cursor.execute("DROP DATABASE purbeurre;")
        connector.close()
        raise e


def insert_in_tables(connector):
    try:
        # TODO: Le code produit sera t-il une clé en bdd ? Si oui à gérer en cas de vide ou None
        cursor = connector.cursor()
        sql_products = """INSERT INTO Products(generic_name_fr,product_name_fr_imported, 
        ingredients_text_with_allergens_fr,code, url, nutrition_grade_fr, name) VALUES (%s, %s, %s, %s, %s, %s, %s); """
        sql_categories = """INSERT INTO Categories(categories, code) VALUES (%s, %s);"""
        sql_stores = """INSERT INTO Places_to_buy(stores, code) VALUES (%s, %s);"""
        for product in api_get_products():
            # insert data to product
            cursor.execute(sql_products, (
                product.get('generic_name_fr') if product.get('generic_name_fr') is not None else '',
                product.get('product_name_fr_imported') if product.get('product_name_fr_imported') is not None else '',
                product.get('ingredients_text_with_allergens_fr') if product.get(
                    'ingredients_text_with_allergens_fr') is not None else '',
                product.get('code') if product.get('code') is not None else '',
                product.get('url') if product.get('url') is not None else '',
                product.get('nutrition_grade_fr') if product.get('nutrition_grade_fr') is not None else '',
                product.get('name') if product.get('name') is not None else ''))
            connector.commit()
            # Insert data to categories
            cursor.execute(sql_categories, (
                product.get('categories') if product.get('categories') is not None else '',
                product.get('code') if product.get('code') is not None else '',
            ))
            connector.commit()
            # Insert data to stores
            cursor.execute(sql_stores, (
                product.get('stores') if product.get('stores') is not None else '',
                product.get('code') if product.get('code') is not None else '',
            ))
            connector.commit()
    except Exception as e:
        raise e


def get_bdd_connector():
    # Return new cursor from bdd (to avoid connection lost)
    # TODO: Connexion perdu = program crash
    connector = mysql.connect(**infos_db_purbeurre)
    return connector
