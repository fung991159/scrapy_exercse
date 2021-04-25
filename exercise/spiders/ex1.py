import scrapy


class Ex1Spider(scrapy.Spider):
    name = 'ex1'
    allowed_domains = ['https://scrapingclub.com/exercise/detail_basic/']
    start_urls = ['http://https://scrapingclub.com/exercise/detail_basic//']

    def parse(self, response):
        pass
