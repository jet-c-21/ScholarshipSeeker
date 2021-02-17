"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/17/21
"""
# coding: utf-8
import json


def read_json(fp: str) -> dict:
    return json.load(open(fp, 'r', encoding='utf-8'))


def to_json(data, fp: str):
    json.dump(data, open(fp, 'w', encoding='utf-8'), indent=4, ensure_ascii=False)
