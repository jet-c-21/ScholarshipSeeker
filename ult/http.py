"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/17/21
"""
# coding: utf-8
import requests
from pyquery import PyQuery as pq


def get(url: str) -> requests.Response:
    return requests.get(url)


def post(url: str) -> requests.Response:
    pass


def get_doc(url: str, method='GET') -> pq:
    if method == 'GET':
        return pq(get(url).text)
    else:
        # post
        pass
