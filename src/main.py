#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

from src.classes.bdd import Bdd
from src.classes.software import Display

if __name__ == "__main__":
    Display(Bdd())

# TODO: Ne pas importer le produit en cas d'une case vide ou unknown
