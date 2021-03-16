#!/usr/bin/python3.9
# -*-coding:utf-8 -

import mysql.connector
from mysql.connector import errorcode
from develop.constants import infos_db_purbeurre, infos_db, create_tables_cmd
from services.api import api_get_products


def init_database():
    try:
        connexion = mysql.connector.connect(**infos_db_purbeurre)
        connexion.close()
    except mysql.connector.Error as err:
        # TODO: Gérer les erreurs plus proprement
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == 1049:
            create_database()
        else:
            raise err


def create_database():
    try:
        connector = mysql.connector.connect(**infos_db)
        cursor = connector.cursor()
        cursor.execute("SET NAMES utf8;")
        cursor.execute("CREATE DATABASE purbeurre;")
        cursor.execute("USE purbeurre;")
        for cmd in create_tables_cmd:
            # creation des tables
            cursor.execute(cmd)
        insert_in_table_products(connector)
    except Exception as e:
        raise e


def insert_in_table_products(connector):
    try:
        for product in api_get_products():
            sql = """INSERT INTO Products(generic_name_fr,product_name_fr_imported,
            ingredients_text_with_allergens_fr,code, url, nutrition_grade_fr) VALUES (%s, %s, %s, %s, %s, %s);"""
            cursor = connector.cursor()
            cursor.execute(sql, (
                product.get('generic_name_fr') if product.get('generic_name_fr') is not None else '',
                product.get('product_name_fr_imported') if product.get('product_name_fr_imported') is not None else '',
                product.get('ingredients_text_with_allergens_fr') if product.get('ingredients_text_with_allergens_fr') is not None else '',
                product.get('code') if product.get('code') is not None else '',
                product.get('url') if product.get('url') is not None else '',
                product.get('nutrition_grade_fr') if product.get('nutrition_grade_fr') is not None else ''))
            connector.commit()
    except Exception as e:
        raise e
