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
from AjkSpider.Exception import tryex

class ResidenceSpider(CrawlSpider):
    name = 'ajk_get_residence'
    start_urls = []
    custom_settings = {
        # 'FEED_URI': '/usr/local/crawler/dxc/common/ajk/data/ajk_residence_irt_%s.csv' % datetime.date.today(),
        # 'LOG_FILE': '/usr/local/crawler/dxc/common/ajk/logs/ajk_residence_irt_%s.log' % datetime.date.today(),
        'DOWNLOADER_MIDDLEWARES':{
            'AjkSpider.middlewares.ProxyMiddleware': 202,
        },
        'ITEM_PIPELINES':{
           'AjkSpider.pipelines.InsertMysqlPipeline': 300,
        }
    }

    def start_requests(self):
        q_result = Mysql().query_by_sql('''
                            select co.id,co.route,ci.url
                            from t_web_ajk_community co,t_web_ajk_district di,t_web_ajk_city ci
                            where co.district_id=di.id and di.city_id=ci.id;
                        ''')

        for one_d in q_result:
            yield Request(
                one_d['url'] + 'community/' + one_d['route'] + '/',
                meta={'id': one_d['id'], 'url': one_d['url']},
                callback=self.get_residence_url
            )

    def get_residence_url(self,response):
        urls = Selector(response).xpath('//*[@_soj="xqlb"]/@link').extract()
        for url in urls:
            yield Request(
                response.request.meta['url'] + url[0:-1] + '?from=Filter_1&hfilter=filterlist',
                meta=response.request.meta,
                callback=self.get_residence_info
            )
        next_page_url = Selector(response).xpath('//*[@class="aNxt"]/@href').extract_first()
        if next_page_url is not None:
            yield Request(
                next_page_url,
                meta=response.request.meta,
                callback=self.get_residence_url
            )

    def get_residence_info(self, response):
        sr = Selector(response)
        item = ResidenceItem()
        item['residence_name']    = tryex.strip(sr.xpath('//*[@id="content"]/div[3]/div[1]/h1/text()').extract_first())
        item['avg_price']         = sr.xpath('//*[@id="basic-infos-box"]/div[1]/span[1]/text()').extract_first()

        qushi = sr.xpath('//*[@id="basic-infos-box"]/div[1]/span[2]/i/text()').extract_first()
        num = sr.xpath('//*[@id="basic-infos-box"]/div[1]/span[2]/text()').extract_first()
        item['compare_pre_month'] = qushi + num

        item['address']           = sr.xpath('//*[@class="sub-hd"]/text()').extract_first()
        item['build_time']        = sr.xpath('//*[@id="basic-infos-box"]/dl/dd[5]/text()').extract_first()
        item['property_type']     = sr.xpath('//*[@id="basic-infos-box"]/dl/dd[1]/text()').extract_first()
        item['property_price']    = sr.xpath('//*[@id="basic-infos-box"]/dl/dd[2]/text()').extract_first()
        item['property_company']  = sr.xpath('//*[@id="basic-infos-box"]/dl/dd[10]/text()').extract_first()
        item['developer']         = sr.xpath('//*[@id="basic-infos-box"]/dl/dd[9]/text()').extract_first()
        item['total_areas']       = sr.xpath('//*[@id="basic-infos-box"]/dl/dd[3]/text()').extract_first()
        item['total_houses']      = sr.xpath('//*[@id="basic-infos-box"]/dl/dd[4]/text()').extract_first()
        item['parking_space']     = sr.xpath('//*[@id="basic-infos-box"]/dl/dd[6]/text()').extract_first()
        item['accumulation_rate'] = sr.xpath('//*[@id="basic-infos-box"]/dl/dd[7]/text()').extract_first()
        item['green_rate']        = sr.xpath('//*[@id="basic-infos-box"]/dl/dd[8]/text()').extract_first()

        item['bsn_dt']            = str(datetime.date.today())
        item['tms']               = datetime.datetime.now().strftime('%Y-%m-%d %X')
        item['url']               = response.url
        item['webst_nm']          = u'安居客'
        item['crawl_time']        = datetime.datetime.now().strftime('%Y-%m-%d %X')
        item['community_id']      = response.request.meta['id']
        yield item
