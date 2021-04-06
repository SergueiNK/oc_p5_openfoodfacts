#!/usr/bin/python3.9
# -*- coding:utf-8 -*-
import mysql.connector as mysql
from src.config.constants import infos_db, create_tables_cmd
from src.purbeurre.api import api_get_products
from src.config.constants import SqlStatement

def create_database():
    """Create the database purbeurre"""
    try:
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
            insert_in_tables(connector)
            connector.close()
        except Exception as e:
            # In case of pb drop the database
            connector.close()
            raise e
    except Exception as e:
        # print(e)
        raise e

def insert_in_tables(connector):
    """Insert values to tables """
    try:
        cursor = connector.cursor()
        sql_products = SqlStatement.insert_values_products_table
        sql_categories = SqlStatement.insert_values_categories_table
        for product in api_get_products():

            # Insert verified data to products
            if verify_product(product):
                cursor.execute(sql_products, (
                    product.get('generic_name_fr'),
                    product.get('code'),
                    product.get('url'),
                    product.get('nutrition_grade_fr'),
                    product.get('stores')))
                connector.commit()
                # Insert verified data to categories
                cursor.execute(sql_categories, (
                    product.get('pnns_groups_1'),
                    product.get('code')
                ))
                connector.commit()

    except Exception as e:
        raise e


def verify_product(product):
    """ Check and sort the API before insert in tables """
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
            and product.get('stores') != '' \
            and product.get('pnns_groups_1') \
            and product.get('pnns_groups_1') != 'unknown' \
            and product.get('pnns_groups_1') != '' \
            and product.get('code') \
            and product.get('code') != 'unknown' \
            and product.get('code') != '':
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        create_database()
        print("Base de données créée")
    except Exception as e:
        print(e)