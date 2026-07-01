from itemadapter import ItemAdapter
from product_scraper.storage.database import init_database
from product_scraper.storage.repository import ProductRepository


class ProductScraperPipeline:
    def __init__(self):
        init_database()

        self.repository = ProductRepository()

    def process_item(self, item, spider):
        self.repository.save(item)
        return item
