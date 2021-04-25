import scrapy
import json
# Inspect HTTP request
# Learn to inspect the fields of HTTP request
# Some website would check HTTP headers such as Referer to block some abnormal request.

class Ex5Spider(scrapy.Spider):
    name = 'ex5'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/detail_header']
    url = 'https://scrapingclub.com/exercise/ajaxdetail_header/'

    def parse(self, response):
        yield scrapy.Request(f'https://scrapingclub.com/exercise/ajaxdetail/',
                                headers={'referer': self.start_urls[0]},
                                callback=self.parse_ajax)

    def parse_ajax(self, response):
        yield json.loads(response.text)

# bascially it is same as ex4, except header need to be added to call the ajax request url.