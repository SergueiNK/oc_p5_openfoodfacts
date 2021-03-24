#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

from services.bdd import Bdd
from software import Display

if __name__ == "__main__":
    Display(Bdd())


# TODO: classe Enum dans les constantes langue et bdd
# TODO: switch case pour les redirections