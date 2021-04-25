import scrapy

# Recursively Scraping pages
# Try to extract all product detail infomation such as title, description,
# you should also handle pagination here so in the end you can get about 100+ records.

class Ex3Spider(scrapy.Spider):
    name = 'ex3'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_basic/?page=1']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_product_links)

    def parse_product_links(self, response):
        products = response.xpath("//div[contains(@class, 'card')]/a/@href").getall()
        for p in products:
            yield scrapy.Request(url=f'https://scrapingclub.com{p}', callback=self.parse_item)

        next_page = response.xpath("//a[text()='Next']/@href").get()
        if next_page:
            yield response.follow(f'https://scrapingclub.com/exercise/list_basic/{next_page}', callback=self.parse_product_links)

    def parse_item(self, response):
        path = "//div[contains(@class, 'card-body')]/{}/text()"
        d = dict(
            title = response.xpath(path.format('h3')).get(),
            price = response.xpath(path.format('h4')).get(),
            desc = response.xpath(path.format('p')).get()
        )
        yield d

# comment: so the call back actually stack together and call one after another
# I guess scrapy make use of coroutine / asyncio to do the crawling?
