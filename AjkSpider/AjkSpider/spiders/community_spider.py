import re
import psycopg2

from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.http import Request

from AjkSpider.items import *
from AjkSpider.Db.Mysql import *

class CommunitySpider(CrawlSpider):
    name = 'ajk_get_community'
    start_urls = []
    custom_settings = {
        'DOWNLOADER_MIDDLEWARES':{
        #    'AjkSpider.middlewares.ProxyMiddleware': 202,
        },
        'ITEM_PIPELINES':{
           'AjkSpider.pipelines.InsertMysqlPipeline': 300,
        }
    }

    def start_requests(self):
        id_and_route = Mysql().query_by_sql('''
                            select di.id,di.route,ci.url
                            from t_web_ajk_district di,t_web_ajk_city ci
                            where di.city_id=ci.id
                        ''')
        for one in id_and_route:
            yield Request(
                one['url'] + 'community/' + one['route'] + '/',
                meta={'id': one['id']},
                callback=self.get_community,
                dont_filter=True
            )

    def get_community(self, response):
        district_id = response.meta['id']
        cn_name = Selector(response).xpath('/html/body/div[5]/div[2]/div[1]/span[2]/div/a/@data-id').extract()
        route = Selector(response).xpath('/html/body/div[5]/div[2]/div[1]/span[2]/div/a/@href').extract()
        item = CommunityItem()
        flag = False
        for n, r in zip(cn_name, route):
            if flag:
                item['cn_name'] = n
                item['route'] = r.split('/')[-2]
                item['district_id'] = district_id
                yield item
            else:
                flag = True;
