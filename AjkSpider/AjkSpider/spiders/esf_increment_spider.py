#-*- encoding:utf-8 -*-

import re
import datetime

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request

from AjkSpider.items import *
from AjkSpider.Db.Mysql import *
from AjkSpider.Exception import tryex

class EsfIrtSpider(CrawlSpider):
    name = 'ajk_get_esf_irt'
    start_urls = []
    custom_settings = {
        # 'FEED_URI': '/usr/local/crawler/dxc/common/ajk/data/ajk_esf_irt_%s.csv' % datetime.date.today(),
        # 'LOG_FILE': '/usr/local/crawler/dxc/common/ajk/logs/ajk_esf_irt_%s.log' % datetime.date.today(),
        'DOWNLOADER_MIDDLEWARES':{
            # 'AjkSpider.middlewares.ProxyMiddleware': 202,
        },
        'ITEM_PIPELINES':{
           'AjkSpider.pipelines.InsertPostgresqlPipeline': 300,
        }
    }

    def __init__(self):
        self.stop_date = 0

    def start_requests(self):
        id_esf_url = Mysql().query_by_sql('''
                        select co.route,c.url
                        from t_web_ajk_community co,t_web_ajk_district d,t_web_ajk_city c
                        where d.id=co.district_id and d.city_id=c.id
                    ''')
        for one in id_esf_url:
            yield Request(
                one['url'] + 'sale/' + one['route'] + '/',
                callback=self.get_esf_url,
                dont_filter=True
            )

    def get_esf_url(self,response):
        esf_url = Selector(response).xpath('//*[@id="houselist-mod-new"]/li/div[2]/div[1]/a/@href').extract()
        for url in esf_url:
            if stop_date:
                return
            else:
                yield Request(
                    url,
                    callback=self.get_esf_info,
                    dont_filter=True
                )

        next_page_url = Selector(response).xpath('//*[@class="aNxt"]/@href').extract_first()
        if next_page_url is not None:
            yield Request(
                next_page_url,
                callback=self.get_esf_url,
                dont_filter=True
            )

    def get_esf_info(self, response):
        sr = Selector(response)
        item = EsfItem()

        num_and_date = sr.xpath('//*[@class="house-encode"]/text()').extract_first()
        nd_list = re.compile(r'\d+').findall(num_and_date)
        listing_date = nd_list[1] + '-' + nd_list[2] + '-' + nd_list[3]
        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday
        old_latest_date = datetime.datetime.strptime(str(yesterday), '%Y-%m-%d')
        try:
            latest_date = datetime.datetime.strptime(listing_date, '%Y-%m-%d')
        except:
            return
        day_space = (latest_date - old_latest_date).days
        if day_space != 0:
            self.stop_date = 1
            return

        item['structure']         = sr.xpath('//*[@class="houseInfoV2-detail clearfix"]/div/dl/dt[text()="%s"]/following-sibling::*[1]/a/@href' % u'小区：').extract_first()
        item['orientation']       = sr.xpath('//*[@class="houseInfoV2-detail clearfix"]/div/dl/dt[text()="%s"]/following-sibling::*[1]/text()' % u'朝向：').extract_first()
        item['area']              = sr.xpath('//*[@class="houseInfoV2-detail clearfix"]/div/dl/dt[text()="%s"]/following-sibling::*[1]/text()' % u'面积：').extract_first()
        item['decoration']        = sr.xpath('//*[@class="houseInfoV2-detail clearfix"]/div/dl/dt[text()="%s"]/following-sibling::*[1]/text()' % u'装修程度：').extract_first()

        rec = re.compile(r'\d+')
        fl = tryex.strip(sr.xpath('//*[@class="houseInfoV2-detail clearfix"]/div/dl/dt[text()="%s"]/following-sibling::*[1]/text()' % u'楼层：').extract_first()).split('(')
    	if len(fl) == 2:
    		item['floor'] = fl[0]
    		item['total_floor'] = rec.findall(fl[1])[0]
        else:
    		item['floor'] = None
    		item['total_floor'] = None

        item['ajk_num']            = nd_list[0]

        item['house_type']        = sr.xpath('//*[@class="houseInfoV2-detail clearfix"]/div/dl/dt[text()="%s"]/following-sibling::*[1]/text()' % u'房型：').extract_first()
        item['listing_date']      = listing_date
        item['total_price']       = sr.xpath('//*[@class="light info-tag"]/em/text()').extract_first()
        item['unit_price']        = sr.xpath('//*[@class="houseInfoV2-detail clearfix"]/div/dl/dt[text()="%s"]/following-sibling::*[1]/text()' % u'房屋单价：').extract_first()
        item['build_time']        = sr.xpath('//*[@class="houseInfoV2-detail clearfix"]/div/dl/dt[text()="%s"]/following-sibling::*[1]/text()' % u'年代：').extract_first()

        item['bsn_dt']            = str(datetime.date.today())
        item['tms']               = datetime.datetime.now().strftime('%Y-%m-%d %X')
        item['url']               = response.url
        item['webst_nm']          = u'安居客'
        item['crawl_time']        = datetime.datetime.now().strftime('%Y-%m-%d %X')
        item['residence_url']     = sr.xpath('//*[@class="houseInfoV2-detail clearfix"]/div/dl/dt[text()="%s"]/following-sibling::*[1]/a/@href' % u'小区：').extract_first()
        item['residence_id']      = 0
        yield item
