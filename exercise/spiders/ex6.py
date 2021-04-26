import scrapy
import json
# Scraping Infinite Scrolling Pages (Ajax)
# The key to scrape infinite scrolling pages is to use network panel in your browser to figure out the url of next page.
# Sometimes you also need to take care of the http headers to make your code work.
# In this exercise, try to crawl all product info.

class Spider(scrapy.Spider):
    name = 'ex6'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/list_infinite_scroll/']
    base = 'https://scrapingclub.com'
    # def parse(self, response):
    #     yield scrapy.Request(f'https://scrapingclub.com/exercise/ajaxdetail/',
    #                             headers={'referer': self.start_urls[0]},
    #                             callback=self.parse_ajax)

    def to_ajax(self, original_url):
        return original_url.replace('list_detail_infinite_scroll' ,
                                        'list_detail_ajax_infinite_scroll')

    def parse(self, response):
        products = response.xpath("//div[contains(@class, 'card')]/a/@href").getall()   #/exercise/list_detail_infinite_scroll/90008-E/

        for p in products:
            yield scrapy.Request(url = self.base + self.to_ajax(p)
                                , callback = self.parse_ajax
                                , headers ={'referer': self.base + p,
                                            'User-Agent':  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'
                                            }
                                )

    def parse_ajax(self, response):
        print(response.text)
        # yield json.loads(response.text) 

    # def parse_product(self, response):
        # print(response.body)
        # new_p = response.url.replace('list_detail_infinite_scroll', 'list_detail_ajax_infinite_scroll')
        # yield scrapy.Request(url=f'https://scrapingclub.com{new_p}'
        #                          , callback = self.parse_ajax
        #                          , headers = {'referer': response.url})

        # next_page = response.xpath("//a[text()='Next']/@href").get()
        # if next_page:
        #     yield response.follow(f'https://scrapingclub.com/exercise/list_infinite_scroll/{next_page}'
        #                           , callback=self.parse
        #                           , headers={'referer': f'{self.start_urls[0]}'})

