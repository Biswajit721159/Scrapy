import scrapy

class AmbissionBoxSpider(scrapy.Spider):
    name = "AmbissionBox"
    start_urls = ["https://www.ambitionbox.com/overview/riktam-technologies-overview"]

    def parse(self, response):
        alldata = response.xpath('//h1[@class="newHInfo__cNtxt"]/text()').get()
        print(alldata)

        pass