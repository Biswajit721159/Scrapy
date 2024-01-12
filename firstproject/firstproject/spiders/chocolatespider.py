import scrapy
from firstproject.items import netmeds
class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    start_urls = ["https://www.netmeds.com/non-prescriptions/personal-care/face-personal-care/face-wash-cleansers"]

    custom_settings={
        'FEEDS':{
                'netmeds.json':{'format':'json','overwrite':True}
        }
    }

    def parse(self, response):
        alldata = response.xpath('.//div[@class="row product-list"]//div[@class="cat-item "]')
        for i in range(len(alldata)):
            data = alldata[i]
            netmedsdata=netmeds()
            
            netmedsdata['offer'] = data.xpath('.//span[@class="save-badge"]/text()').get()
            netmedsdata['product_name']=data.xpath('.//span[@class="clsgetname"]/text()').get()
            netmedsdata['product_img']=data.xpath('.//span[@class="cat-img"]/img/@src').get()
            netmedsdata['rating']=data.xpath('.//span[@class="rating"]/text()').get()
            netmedsdata['price']=data.xpath('.//span[@class="price-box"]/span[@id="final_price"]/text()').get()

            yield netmedsdata
            
            next_page = response.css("li.next a::attr(href)").get()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
       








        # for quote in response.css("div.quote"):
        #     yield {
        #         "text": quote.css("span.text::text").get(),
        #         "author": quote.css("small.author::text").get(),
        #         "tags": quote.css("div.tags a.tag::text").getall(),
        #     }
        
        # next_page = response.css("li.next a::attr(href)").get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)



            # text = quote.css("span.text::text").get()
            # author = quote.css("small.author::text").get()
            # tags = quote.css("div.tags a.tag::text").getall()
            # print(dict(text=text, author=author, tags=tags))
        # y=x.css("div.tags a::attr(href)").getall()
        # y=x.css("div.tags a.tag::text").getall()
        # y=x.css("a::attr(href)").get()
        # print("Hello World")
        # print(y)
        # alldata=response.css("div.quote")
        # for data in alldata:
        #     text = data.css("span.text::text").get()
        #     author = data.css("small.author::text").get()
        #     tags = data.css("div.tags a.tag::text").getall()
        #     print(dict(text=text, author=author, tags=tags))

