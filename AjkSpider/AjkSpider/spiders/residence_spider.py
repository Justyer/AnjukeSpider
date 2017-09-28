#-*- encoding:utf-8 -*-

import re
import time
import datetime
import psycopg2

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.http import Request

from AjkSpider.items import *
from AjkSpider.Db.Mysql import *

class ResidenceSpider(CrawlSpider):
    name = 'ajk_get_residence'
    start_urls = []
    custom_settings = {
        'FEED_URI': '/usr/local/crawler/dxc/common/ajk/data/ajk_residence_irt_%s.csv' % datetime.date.today(),
        'JOBDIR': '/usr/local/crawler/dxc/common/ajk/crawls/ajk_residence_irt_%s' % datetime.date.today(),
        'LOG_FILE': '/usr/local/crawler/dxc/common/ajk/logs/ajk_residence_irt_%s.log' % datetime.date.today(),
        'DOWNLOADER_MIDDLEWARES':{
            'AjkSpider.middlewares.ProxyMiddleware': 202,
        },
        'ITEM_PIPELINES':{
        #    'AjkSpider.pipelines.InsertMysqlPipeline': 300,
        #    'AjkSpider.pipelines.JsonPipeline': 301,
        }
    }

    def __init__(self):
        self.d_c = {}

    def start_requests(self):
        q_result = Mysql().query_by_sql('''
                            select co.id,di.route d_r,co.route c_r,ci.url
                            from t_web_ajk_community co,t_web_ajk_district di,t_web_ajk_city ci
                            where co.district_id=di.id and di.city_id=ci.id;
                        ''')
        for one_r in q_result:
            self.d_c[one_r['d_r'] + '_' + one_r['c_r']] = one_r['id']

        for one_d in q_result:
            yield Request(
                one_d['url'] + 'xiaoqu/' + one_d['c_r'] + '/',
                callback=self.get_residence_url
            )

    def get_residence_url(self,response):
        li = Selector(response).xpath('/html/body/div[4]/div[1]/ul/li').extract()
        for l in li:
            st = Selector(text=l)
            url = st.xpath('//*[@class="img"]/@href').extract_first()
            district = st.xpath('//*[@class="district"]/@href').extract_first().split('/')[-2]
            community = st.xpath('//*[@class="bizcircle"]/@href').extract_first().split('/')[-2]
            yield Request(
                url,
                meta={'d_c': district + '_' + community},
                callback=self.get_residence_info
            )
        page_box = Selector(response).xpath('//*[@class="page-box house-lst-page-box"]').extract_first()
        if page_box is not None:
            totalPage = eval(Selector(text=page_box).xpath('//@page-data').extract_first())['totalPage']
            curPage = eval(Selector(text=page_box).xpath('//@page-data').extract_first())['curPage']
            if totalPage > curPage:
                yield Request(
                    response.url[0:response.url.find('/', 30) + 1] + 'pg' + str(curPage + 1) + '/',
                    callback=self.get_residence_url
                )

    def get_residence_info(self, response):
        sr = Selector(response)
        item = ResidenceItem()
        item['residence_name']   = sr.xpath('//*[@class="detailTitle"]/text()').extract_first()
        item['avg_price']        = sr.xpath('//*[@class="xiaoquUnitPrice"]/text()').extract_first()
        item['avg_time']         = sr.xpath('//*[@class="xiaoquUnitPriceDesc"]/text()').extract_first()
        item['address']          = sr.xpath('//*[@class="detailDesc"]/text()').extract_first()
        item['coordinate']       = sr.xpath('//*[@class="xiaoquInfoContent"]/span/@xiaoqu').extract_first()
        item['build_time']       = sr.xpath('//*[@class="xiaoquInfo"]/div[1]/span[2]/text()').extract_first()
        item['property_price']   = sr.xpath('//*[@class="xiaoquInfo"]/div[3]/span[2]/text()').extract_first()
        item['property_company'] = sr.xpath('//*[@class="xiaoquInfo"]/div[4]/span[2]/text()').extract_first()
        item['developer']        = sr.xpath('//*[@class="xiaoquInfo"]/div[5]/span[2]/text()').extract_first()
        item['total_buildings']  = sr.xpath('//*[@class="xiaoquInfo"]/div[6]/span[2]/text()').extract_first()
        item['total_houses']     = sr.xpath('//*[@class="xiaoquInfo"]/div[7]/span[2]/text()').extract_first()
        item['url']              = response.url
        item['crawl_time']       = time.strftime("%Y-%m-%d %X",time.localtime())
        item['community_id']     = self.d_c[response.request.meta['d_c']]
        yield item