import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["https://bantia.in/collections"]

    def parse(self, response):
        producturl=response.xpath('//div[@class="grid__cell 1/2--tablet 1/3--lap-and-up"]')
        for i in range(len(producturl)):
            product=producturl[i]
            url="https://bantia.in/"
            ProduUrl=product.xpath('a/@href').get()
            actualurl=url+ProduUrl
            # print(actualurl)
            yield scrapy.Request(actualurl,callback=self.findProduct_information) 

    def findProduct_information(self,response):
        allproduct=response.xpath('//div[@class="product-item product-item--vertical  1/3--tablet-and-up 1/4--desk"]')
        for i in range(len(allproduct)):
            data=allproduct[i]
            product_name=data.xpath('div[@class="product-item__info"]/div[@class="product-item__info-inner"]/a/text()').get()
            price=data.xpath('div[@class="product-item__info"]/div[@class="product-item__info-inner"]/div[@class="product-item__price-list price-list"]')
            print(price)
            image=data.xpath('a[@class="product-item__image-wrapper "]/div[@class="aspect-ratio aspect-ratio--short"]/noscript/text()').get()
            yield{
                "product_name":product_name,
                # "price":price,
                "image":image
            }