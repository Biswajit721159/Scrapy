import scrapy


class SwiggyhyderabadSpider(scrapy.Spider):
    name = "swiggyhyderabad"
    allowed_domains = ["www.swiggy.com"]
    start_urls = ["https://www.swiggy.com/restaurants/meridian-restaurant-panjagutta-hyderabad-25251"]

    def parse(self, response):
        alldata=response.xpath('//div[@class="styles_container__-kShr"]')
        for i in range(len(alldata)):
            data=alldata[i]
            product=data.xpath('div[@class="styles_item__3_NEA styles_hasImage__3OsYt"]')
            product_name_price_searve=product.xpath('div[@class="styles_detailsContainer__22vh8"]')
            product_name=product_name_price_searve.xpath('div[@class="styles_itemName__hLfgz"]/h3[@class="styles_itemNameText__3ZmZZ"]/text()').get()
            price=product_name_price_searve.xpath('div[@class="styles_itemPortionContainer__1u_tj"]/span[@class="styles_price__2xrhD styles_itemPrice__1Nrpd styles_s__66zLz"]/span[@class="rupee"]/text()').get()
            searve=product_name_price_searve.xpath('div[@class="styles_itemDesc__3vhM0"]/text()').get()
            image=product.xpath('div[@class="styles_itemImageContainer__3Czsd"]/div/button[@class="styles_itemImage__3CsDL"]/img/@src').get()
            # image=product.xpath('//[@class="styles_itemImage__3CsDL"]/img/@src').get()

            yield{
                "product_name":product_name,
                "price":price,
                "searve":searve,
                "image":image
            }

