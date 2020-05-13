# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import requests
from typing import List, NoReturn

from .settings import WEB_URL
from twenty_first_century.items import ProductItem


class TwentyFirstCenterPipeline(object):

    def __init__(self) -> NoReturn:
        self.products: List[ProductItem] = list()

    def process_item(self, product, spider) -> ProductItem:
        self.products.append(product)
        return product

    def close_spider(self, spider) -> NoReturn:
        requests.patch(
            url=WEB_URL.format(os.environ['SCRAPY_JOB']),
            json={'data': [dict(item) for item in self.products]}
        )
