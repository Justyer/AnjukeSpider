# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TestItem(scrapy.Item):
    __table__ = 'test'

    t1 = scrapy.Field()
    t2 = scrapy.Field()

class CityItem(scrapy.Item):
    __table__ = 't_web_ajk_city'

    cn_name = scrapy.Field()
    route   = scrapy.Field()
    url     = scrapy.Field()

class DistrictItem(scrapy.Item):
    __table__ = 't_web_ajk_district'

    cn_name = scrapy.Field()
    route   = scrapy.Field()
    city_id = scrapy.Field()

class CommunityItem(scrapy.Item):
    __table__ = 't_web_ajk_community'

    cn_name     = scrapy.Field()
    route       = scrapy.Field()
    district_id = scrapy.Field()

class ResidenceItem(scrapy.Item):
    __table__ = 't_web_ajk_residence'

    residence_name    = scrapy.Field()
    avg_price         = scrapy.Field()
    address           = scrapy.Field()
    build_time        = scrapy.Field()
    property_type     = scrapy.Field()
    property_price    = scrapy.Field()
    property_company  = scrapy.Field()
    developer         = scrapy.Field()
    total_areas       = scrapy.Field()
    total_houses      = scrapy.Field()
    parking_space     = scrapy.Field()
    accumulation_rate = scrapy.Field()
    green_rate        = scrapy.Field()
    bsn_dt            = scrapy.Field()
    tms               = scrapy.Field()
    url               = scrapy.Field()
    webst_nm          = scrapy.Field()
    crawl_time        = scrapy.Field()
    city              = scrapy.Field()
    district          = scrapy.Field()
    community         = scrapy.Field()
    community_id      = scrapy.Field()

class EsfItem(scrapy.Item):
    __table__ = 't_web_ajk_esf'

    structure         = scrapy.Field()
    orientation       = scrapy.Field()
    area              = scrapy.Field()
    decoration        = scrapy.Field()
    address           = scrapy.Field()
    floor             = scrapy.Field()
    total_floor       = scrapy.Field()

    ajk_num           = scrapy.Field()

    house_type        = scrapy.Field()
    listing_date      = scrapy.Field()
    total_price       = scrapy.Field()
    unit_price        = scrapy.Field()
    build_time        = scrapy.Field()

    bsn_dt            = scrapy.Field()
    tms               = scrapy.Field()
    url               = scrapy.Field()
    webst_nm          = scrapy.Field()
    crawl_time        = scrapy.Field()
    residence_url     = scrapy.Field()
    residence_id      = scrapy.Field()
