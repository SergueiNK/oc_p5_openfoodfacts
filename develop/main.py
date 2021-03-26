#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

from services.bdd import Bdd
from software import Display

if __name__ == "__main__":
    Display(Bdd())

# TODO: switch case pour les redirections
# TODO: Ne pas importer le produit en cas d'une case vide ou unknown
