#-*- encoding:utf-8 -*-

import codecs
import datetime

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.http import Request

from AjkSpider.items import *
from AjkSpider.Db.Mysql import *

from AjkSpider.Exception import tryex

class TestSpider(CrawlSpider):
    name = 'sys_test'
    start_urls = [
        'https://beijing.anjuke.com/prop/view/A1002780223?from=filter-saleMetro&spread=filtersearch_p&position=59&kwtype=filter&now_time=1508215566',
    ]
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES':{
            # 'AjkSpider.middlewares.ProxyMiddleware': 202,
        },
        'ITEM_PIPELINES':{
        #    'AjkSpider.pipelines.InsertPostgresqlPipeline': 300,
        }
    }

    def start_requests(self):
        return [Request(
            self.start_urls[0],
            callback=self.test_page,
            dont_filter=True
        )]

    def test_page(self, response):
        sr = Selector(response)
        st = sr.xpath('//*[@class="houseInfoV2-detail clearfix"]/div/dl/dt[text()="%s"]/following-sibling::*[1]/p/text()[2]' % u'位置：').extract_first()
        print 'st:', st.replace('\n', '').replace(' ', '')[1:]
