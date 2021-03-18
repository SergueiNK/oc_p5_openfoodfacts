#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

from services.bdd import init_database
from software import Display

if __name__ == "__main__":
    init_database()
    run = Display()
