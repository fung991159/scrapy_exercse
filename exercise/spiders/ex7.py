import scrapy
import json

# Find gold in cookie
# Make your spider can work with the cookie
# Try to extract the product detail such as title, desc and price.
# Tips:
# After some tests, you might find out it is hard to make the spider get the data through normal Ajax, so you need to dive into the detail of the ajax request.
# You need to make sure the URL, HTTP header, cookie values are all reasonable just like what your browser does.

class Spider(scrapy.Spider):
    name = 'ex7'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/detail_cookie/']

    def parse(self, response):
        yield scrapy.Request(self.start_urls[0],
                                headers={'referer': self.start_urls[0]},
                                callback=self.get_token)

    def get_token(self, response):
        cookie = response.headers['Set-Cookie'].decode('utf-8')
        token = cookie.split(';')[0]
        headers = {
            'referer': self.start_urls[0],
            'X-Requested-With': 'XMLHttpRequest'
        }
        yield scrapy.Request(f'https://scrapingclub.com/exercise/ajaxdetail_cookie/?{token}',
                                headers=headers,
                                callback=self.parse_ajax)


    def parse_ajax(self, response):
        yield json.loads(response.text)

# interesting to learn how request work by first gettin the token from cookie, then send the "real" request to AJAX to fetch data
