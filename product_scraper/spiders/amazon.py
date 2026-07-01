import scrapy
from product_scraper.items import ProductScraperItem


class AmazonScrapper(scrapy.Spider):

    name = "amazon"


    start_urls = [
        "https://www.amazon.com.br/Notebook-Gamer-Lenovo-i5-13450HX-83KHS00000/dp/B0GQJM9NJK/ref=pd_ci_mcx_mh_mcx_views_0_title?pd_rd_w=J4QPB&content-id=amzn1.sym.87e935c8-d687-4dd4-9dbf-8b9bdbb5018e%3Aamzn1.symc.c3d5766d-b606-46b8-ab07-1d9d1da0638a&pf_rd_p=87e935c8-d687-4dd4-9dbf-8b9bdbb5018e&pf_rd_r=2JC7G9E1SBYC44D54DD5&pd_rd_wg=4MHTH&pd_rd_r=ae3b70af-ac75-408e-b5b4-47c1d47f269a&pd_rd_i=B0GQJM9NJK"
    ]


    def parse(self, response):
        yield ProductScraperItem(

            name=response.css(
                "#productTitle::text"
            ).get(),

            price=response.css(
                ".a-price-whole::text"
            ).get(),

            url=response.url
        )