# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # offer = scrapy.Field()
    # product_name = scrapy.Field()
    # product_img = scrapy.Field()
    # rating = scrapy.Field()
    # price = scrapy.Field()
    pass

class netmeds(scrapy.Item):
    # define the fields for your item here like:
    offer = scrapy.Field()
    product_name = scrapy.Field()
    product_img = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()    
    
