#!/usr/bin/python3.9
# -*- coding:utf-8 -*-

import requests
from src.config.constants import products_params, url_request
import json


# get API
def api_get_products():
    """Launch the API fetch"""
    try:
        request_response = requests.get(url_request, products_params)
        response = json.loads(request_response.text)
        return response.get('products')
    except Exception as e:
        raise e
