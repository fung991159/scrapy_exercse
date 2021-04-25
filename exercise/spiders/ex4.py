import scrapy
import json
# Mimicking Ajax requests
# Inspect Ajax requests and mimic them

class Ex4Spider(scrapy.Spider):
    name = 'ex4'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/detail_ajax']

    def parse(self, response):
        yield scrapy.Request(f'https://scrapingclub.com/exercise/ajaxdetail/', callback=self.parse_ajax)

    def parse_ajax(self, response):
        yield json.loads(response.text)

# not sure if I am doing it right, first invoke the page
# then fetch product info from ajax reqeuest url json