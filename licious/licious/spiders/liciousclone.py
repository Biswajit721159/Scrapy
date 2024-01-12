import scrapy
from licious.items import netmeds

class LiciouscloneSpider(scrapy.Spider):
    name = "liciousclone"
    start_urls = ["https://www.bookchor.com/store/36/39-store"]

    custom_settings={
        'FEEDS':{
                'netmeds.json':{'format':'json','overwrite':True}
        }
    }

    def parse(self, response):
        alldata = response.xpath('.//div[@class="product-item"]')
        for data in alldata:
            imageurl=data.xpath('div[@class="product-item-img"]/a/@href').get() 
            yield scrapy.Request(imageurl, callback=self.findsubcomponent)

            # pass
            # yield netmedsdata
            
        next_page = response.xpath('//div[@class="pagination"]/a[@class=" nextBtn"]/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        

    def findsubcomponent(self,response):
        # print("Hello Bro")
        # print(response)
        netmedsdata=netmeds()
        netmedsdata['bookname']=response.xpath('//h1[@class="for-desktop"]/text()').get()
        netmedsdata['bookauthername']=response.xpath('//div[@class="Products-details-info"]/ul[@class="Author for-desktop"]//strong/a/text()').get()
        netmedsdata['bookprice']=response.xpath('//div[@class="Products-price for-desktop"]/p/text()').get()
        netmedsdata['bookoffer']=response.xpath('//div[@class="Products-price for-desktop"]/span[@id="off_desktop"]/text()').get()
        netmedsdata['Description']=response.xpath('//div[@class="Description"]/p[@id="desc_full"]/text()').get()     
        netmedsdata['bookimg']=response.xpath('//div[@class="Products-details-img"]/div[@class="Products-details-slider"]/div[@class="product-item-nav"]/div[@class="iten-nav"]/img/@src').get()
        
        
        yield netmedsdata    