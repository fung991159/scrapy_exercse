import scrapy

# Basic Info Scraping
# You can choose the one you like to extract the info, in this exercise,
# try to extract this product detail such as title, desc and price.

class Ex1Spider(scrapy.Spider):
    name = 'ex1'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/detail_basic']

    def parse(self, response):
        path = "//div[contains(@class, 'card-body')]/{}/text()"
        yield dict(
            title = response.xpath(path.format('h3')).get(),
            price = response.xpath(path.format('h4')).get(),
            desc = response.xpath(path.format('p')).get()
        )

