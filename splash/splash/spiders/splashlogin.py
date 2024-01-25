import scrapy


class SplashloginSpider(scrapy.Spider):
    name = "splashlogin"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
