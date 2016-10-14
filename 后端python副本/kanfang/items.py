# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangwuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    money = scrapy.Field()
    star = scrapy.Field()
    address = scrapy.Field()
    link = scrapy.Field()
    img = scrapy.Field()
    pass

