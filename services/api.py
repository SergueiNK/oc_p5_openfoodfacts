#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

import requests
from develop.constants import products_params, url_request
import json


# récuperation de l'API
def api_get_products():
    try:
        request_response = requests.get(url_request, products_params)
        response = json.loads(request_response.text)
        return response.get('products')
    except Exception as e:
        raise e

