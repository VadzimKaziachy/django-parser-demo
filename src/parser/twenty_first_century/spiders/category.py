from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from twenty_first_century.items import ProductItem


class CategorySpider(CrawlSpider):
    name = 'category'
    allowed_domains = ['www.21vek.by']
    start_urls = []
    category_pk = None

    rules = (
        Rule(LinkExtractor(restrict_css=['a.j-load_page']), callback='parser_page', follow=True),
    )

    def __init__(self, category_pk=None, category=None, *args, **kwargs):
        self.start_urls.append(category)
        self.category_pk = category_pk
        super().__init__(*args, **kwargs)

    def parser_page(self, response):
        for product in response.css('span.g-item-data'):
            yield ProductItem(
                category_pk=self.category_pk,
                name=product.attrib.get('data-name', None),
                code=product.attrib.get('data-code', None),
                price=product.attrib.get('data-price', None)
            )
