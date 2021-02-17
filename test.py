"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/17/21
"""
# coding: utf-8
from CPP.crawler import CPPCrawler
from ult import to_json, read_json

cc = CPPCrawler()
data = cc.get_all_data()

to_json(data, 'data.json')


