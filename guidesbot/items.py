# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpringGuide(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    clone_url = scrapy.Field()
    repo_url = scrapy.Field()
    zip_url = scrapy.Field()
