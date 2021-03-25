#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

import mysql.connector as mysql
from mysql.connector import errorcode
from develop.constants import infos_db_purbeurre, infos_db, create_tables_cmd
from services.api import api_get_products
from develop.constants import SqlStatement


class Bdd:
    def __init__(self):
        try:
            self.connexion = mysql.connect(**infos_db_purbeurre)
        except mysql.Error as err:
            # TODO: Gérer les erreurs plus proprement
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == 1049:
                self.create_database()
                self.connexion = mysql.connect(**infos_db_purbeurre)
            else:
                raise err

    def create_database(self):
        connector = mysql.connect(**infos_db)
        cursor = connector.cursor()
        cursor.execute(SqlStatement.use_utf8)
        cursor.execute(SqlStatement.create_purbeurre)
        cursor.execute(SqlStatement.use_purbeurre)
        try:
            for cmd in create_tables_cmd:
                # create the tables
                cursor.execute(cmd)
            self.insert_in_tables(connector)
            connector.close()
        except Exception as e:
            # In case of pb drop the database
            cursor.execute(SqlStatement.drop_purbeurre)
            connector.close()
            raise e

    def insert_in_tables(self, connector):
        try:
            # TODO: Le code produit sera t-il une clé en bdd ? Si oui à gérer en cas de vide ou None
            # TODO: Ne pas importer le produit en cas d'une case vide ou uknown
            cursor = connector.cursor()
            sql_products = SqlStatement.insert_values_products_table
            sql_categories = SqlStatement.insert_values_categories_table
            sql_stores =SqlStatement.insert_values_stores_table
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
                    product.get('pnns_groups_1') if product.get('pnns_groups_1') is not None else '',
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

    def get_query_results(self, sql_statement, columns):
        dict_results = []
        cursor = self.connexion.cursor()
        cursor.execute(sql_statement)
        query_results = cursor.fetchall()
        print(query_results)
        for query_tuple in query_results:
            query_list = list(query_tuple)
            query_object = {}
            for index, item in enumerate(query_list):
                query_object[columns[index]] = item
            dict_results.append(query_object)
        return dict_results
