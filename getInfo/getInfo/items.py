# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # swept排量 pid 爬下来的数据 顺次加一
    pid = scrapy.Field()
    pname = scrapy.Field()
    score = scrapy.Field()
    price = scrapy.Field()
    img_url = scrapy.Field()
    swept = scrapy.Field()
