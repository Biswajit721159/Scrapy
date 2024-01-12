# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LiciousItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class netmeds(scrapy.Item):
    # define the fields for your item here like:
    bookname = scrapy.Field()
    bookauthername = scrapy.Field()
    bookprice = scrapy.Field()
    bookoffer = scrapy.Field()
    Description = scrapy.Field()   
    bookimg=scrapy.Field()