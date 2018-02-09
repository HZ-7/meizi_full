# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeiziAllItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type = scrapy.Field()
    image_title = scrapy.Field()
    image_src = scrapy.Field()
    image_alt = scrapy.Field()

