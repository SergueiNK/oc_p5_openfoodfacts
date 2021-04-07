#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

import mysql.connector as mysql
from src.config.constants import infos_db_purbeurre
import sys


class Bdd:
    """
    class Bdd who defined the creation and modifications of data base
    """
    def __init__(self):
        """Initialize the connexion to Mysql and print error if not"""
        try:
            self.connexion = mysql.connect(**infos_db_purbeurre)
        except mysql.Error as err:
            print(err)
            sys.exit()

    def get_query_results(self, sql_statement, columns):
        """Transform the result on dictionnary"""
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
        """Save the user selection in database"""
        cursor = self.connexion.cursor()
        cursor.execute(sql_statement)
        self.connexion.commit()

