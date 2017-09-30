import re

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.http import Request

from AjkSpider.items import *
from AjkSpider.Db.Mysql import *

class DistrictSpider(CrawlSpider):
    name = 'ajk_get_district'
    start_urls = []
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES':{
           'AjkSpider.middlewares.ProxyMiddleware': 202,
        },
        'ITEM_PIPELINES':{
           'AjkSpider.pipelines.InsertMysqlPipeline': 300,
        }
    }

    def start_requests(self):
        id_url = Mysql().query_by_sql('''
                    select id,url
                    from t_web_ajk_city
                ''')
        for one in id_url:
            yield Request(
                one['url'] + 'community/?from=navigation',
                meta={'id': one['id']},
                callback=self.get_district
            )

    def get_district(self, response):
        cn_name = Selector(response).xpath('/html/body/div[5]/div[2]/div[1]/span[2]/a/text()').extract()
        route = Selector(response).xpath('/html/body/div[5]/div[2]/div[1]/span[2]/a/@href').extract()
        item = DistrictItem()
        flag = False
        for n, r in zip(cn_name, route):
            if flag:
                item['cn_name'] = n
                item['route'] = r.split('/')[-2]
                item['city_id'] = response.request.meta['id']
                yield item
            else:
                flag = True
