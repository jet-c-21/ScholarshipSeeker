"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/17/21
"""
# coding: utf-8
from ult import to_json, read_json

data = read_json('data.json')
print(len(data))

for d in data:
    d['content'] = d['content'].lower()


def drop_with(data: list, words: list):
    result = list()
    for d in data:
        content = d['content']
        drop_flag = False
        for w in words:
            if w in content:
                drop_flag = True
                continue

        if not drop_flag:
            result.append(d)

    return result


def keep_with(data: list, words: list):
    result = list()
    for d in data:
        content = d['content']
        keep_flag = False
        for w in words:
            if w in content:
                keep_flag = True
                continue

        if keep_flag:
            result.append(d)

    return result


dw = ['full-time', 'full time']
new_data = drop_with(data, dw)

kw = ['international']
new_data = drop_with(new_data, kw)

print(len(new_data))

for d in new_data:
    print(d['title'])
    print(d['url'])
    print()

