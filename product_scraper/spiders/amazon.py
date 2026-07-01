import os

import scrapy
from product_scraper.items import ProductScraperItem


class AmazonScrapper(scrapy.Spider):

    name = "amazon"


    start_urls = os.getenv("AMAZON_PRODUCT_URLS", "").split(",")


    def parse(self, response):
        yield ProductScraperItem(

            name=response.css(
                "#productTitle::text"
            ).get(),

            price=response.css(
                ".a-price-whole::text"
            ).get(),

            url=response.url,

            store="amazon"
        )