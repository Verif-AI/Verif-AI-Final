# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PolitifactItem(scrapy.Item):
    # Homepage Item List Fields
    claim = scrapy.Field()
    claim_source = scrapy.Field()
    review_date = scrapy.Field()
    review_author = scrapy.Field()
    veracity = scrapy.Field()

    # Article Fields
    review_tags = scrapy.Field()
    review_points = scrapy.Field()
    review_article = scrapy.Field()
    review_url = scrapy.Field()