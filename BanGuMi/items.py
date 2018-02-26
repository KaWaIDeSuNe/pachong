# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BangumiItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    smail_title = scrapy.Field()
    img = scrapy.Field()
    rank = scrapy.Field()
    fade = scrapy.Field()
    num = scrapy.Field()
    info = scrapy.Field()


