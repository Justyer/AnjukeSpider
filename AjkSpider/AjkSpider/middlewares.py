# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import requests

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        try:
            url = 'http://api.ip.data5u.com/dynamic/get.html?order=82fdbca90fb003889c47a3bfc3d5897c&sep=5'
            proxy_url = requests.get(url=url,timeout=2).text.split(',')[0]
            # print 'proxyUrl:', proxy_url
            if proxy_url != 'too many requests':
                request.meta['proxy'] = "http://" + proxy_url
        except Exception, e:
            pass
