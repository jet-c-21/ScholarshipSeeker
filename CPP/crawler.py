"""
author: Jet Chien
GitHub: https://github.com/jet-c-21
Create Date: 2/17/21
"""
# coding: utf-8
from . import cfg
from ult import http
from pyquery import PyQuery as pq
import datetime
from urllib.parse import urljoin
from tqdm import tqdm


class CPPCrawler:
    def __init__(self, base_url=None):
        if base_url is None:
            self.base_url = cfg.BASE_URL
        else:
            self.base_url = base_url

        self.total_page = 0
        self.all_data = list()

    @staticmethod
    def _str_to_datetime(s: str) -> datetime:
        return datetime.datetime.strptime(s, '%m/%d/%Y')

    @staticmethod
    def _get_post_content(post_url: str) -> str:
        doc = http.get_doc(post_url)
        return doc('section#main').text()

    def _get_page_count(self, doc: pq):
        page_tags = doc('#page > option')
        self.total_page = list(page_tags.items())[-1].attr('value')
        self.total_page = int(self.total_page)

    def get_all_data(self) -> list:
        doc = http.get_doc(self.base_url)
        self._get_page_count(doc)

        for page_num in range(1, self.total_page + 1):
            page_url = f"{self.base_url}?page={page_num}"
            self._fetch_data_per_page(page_url)

        return self.all_data

    def _fetch_data_per_page(self, page_url: str):
        doc = http.get_doc(page_url)
        posts_tag = doc('.full.striped-table > tbody > tr')
        for post_info in tqdm(list(posts_tag.items())):
            deadline_str = post_info('td.center > span.mq-no-bp-only.clr.block').text()
            if deadline_str in ['Ended', '']:
                continue
            deadline = CPPCrawler._str_to_datetime(deadline_str)
            if deadline > datetime.datetime.now():
                award = post_info('td.mq-no-bp-only.strong.h4.table__column--max-width-250').text()
                title_tag = post_info('th > span.strong.h4.block > a')
                title = title_tag.text()
                post_url = urljoin(self.base_url, title_tag.attr('href'))
                content = CPPCrawler._get_post_content(post_url)

                record = {
                    'title': title,
                    'award': award,
                    'deadline': deadline_str,
                    'content': content,
                    'url': post_url
                }

                self.all_data.append(record)

