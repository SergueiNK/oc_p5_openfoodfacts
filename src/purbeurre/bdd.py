#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

import mysql.connector as mysql
from mysql.connector import errorcode
from src.config.constants import infos_db_purbeurre, infos_db, create_tables_cmd
from src.purbeurre.api import api_get_products
from src.config.constants import SqlStatement
import sys


class Bdd:
    """
    class Bdd who defined the creation and modifications of data base
    """
    def __init__(self):
        try:
            self.connexion = mysql.connect(**infos_db_purbeurre)
        except mysql.Error as err:
            if err.errno == 1049:
                self.create_database()
                self.connexion = mysql.connect(**infos_db_purbeurre)
            # si il y a une erreur de connexion alors arrêter le le programme
            else:
                print(err)
                sys.exit()

    def create_database(self):
        connector = mysql.connect(**infos_db)
        cursor = connector.cursor()
        cursor.execute(SqlStatement.use_utf8)
        cursor.execute(SqlStatement.apply_utf8)
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
            cursor = connector.cursor()
            sql_products = SqlStatement.insert_values_products_table
            sql_categories = SqlStatement.insert_values_categories_table
            for product in api_get_products():
                # insert data to product

                if self.verify_product(product):
                    cursor.execute(sql_products, (
                        product.get('generic_name_fr'),
                        product.get('code'),
                        product.get('url'),
                        product.get('nutrition_grade_fr'),
                        product.get('stores')))
                    connector.commit()
                    # Insert data to categories
                    cursor.execute(sql_categories, (
                        product.get('pnns_groups_1'),
                        product.get('code')
                    ))
                    connector.commit()

        except Exception as e:
            raise e

    def get_query_results(self, sql_statement, columns):
        dict_results = []
        cursor = self.connexion.cursor()
        cursor.execute(sql_statement)
        query_results = cursor.fetchall()
        for query_tuple in query_results:
            query_list = list(query_tuple)
            query_object = {}
            for index, item in enumerate(query_list):
                query_object[columns[index]] = item
            dict_results.append(query_object)
        return dict_results

    def save(self, sql_statement):
        cursor = self.connexion.cursor()
        cursor.execute(sql_statement)
        self.connexion.commit()

    def verify_product(self, product):
        if product.get('generic_name_fr') \
                and product.get('generic_name_fr') != 'unknown' \
                and product.get('generic_name_fr') != '' \
                and product.get('code') \
                and product.get('code') != 'unknown' \
                and product.get('code') != '' \
                and product.get('url') \
                and product.get('url') != 'unknown' \
                and product.get('url') != '' \
                and product.get('nutrition_grade_fr') \
                and product.get('nutrition_grade_fr') != 'unknown' \
                and product.get('nutrition_grade_fr') != '' \
                and product.get('stores') \
                and product.get('stores') != 'unknown' \
                and product.get('stores') != ''\
                and product.get('pnns_groups_1') \
                and product.get('pnns_groups_1') != 'unknown' \
                and product.get('pnns_groups_1') != ''\
                and product.get('code') \
                and product.get('code') != 'unknown' \
                and product.get('code') != '':
            return True
        else:
            return False
