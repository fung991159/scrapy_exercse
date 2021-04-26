import scrapy
import json

# Login form
# Scrape data behind login form
# In this exercise, you need to use username scrapingclub and password
# scrapingclub to login in, after you successfully login in, you will be redirected in a welcome page.

def authentication_failed(response):
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
    success_text = response.xpath("//p[text()[contains(.,'You have successfully login in, Congratulations')]]/text()").get()
    return False if success_text else True

class Spider(scrapy.Spider):
    name = 'ex8'
    allowed_domains = ['scrapingclub.com']
    start_urls = ['https://scrapingclub.com/exercise/basic_login/']

    def parse(self, response):
        yield scrapy.Request(self.start_urls[0],
                                headers={'referer': self.start_urls[0]},
                                callback=self.login)

    def login(self, response):
        form_data = {'name': 'scrapingclub', 'password': 'scrapingclub'}
        yield scrapy.FormRequest.from_response(
            response,
            formdata=form_data,
            callback=self.after_login
        )

    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error("Login failed")
            return

# copied above code from scrapy doc, I think using a genric "post"
# request would work just as well