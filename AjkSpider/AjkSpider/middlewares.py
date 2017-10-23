# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import requests

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from scrapy.http import HtmlResponse

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

class CaptchaMiddleware(object):
    def process_request(self, request, spider):
        if request.url[0:38] == 'https://www.anjuke.com/captcha-verify/':
            driver = webdriver.Chrome()
            # dcap = dict(DesiredCapabilities.PHANTOMJS)
            # dcap["phantomjs.page.settings.userAgent"] = (
            # "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"
            # )
            # driver = webdriver.PhantomJS(desired_capabilities=dcap)
            driver.maximize_window()
            #driver.set_window_size(800, 300)
            # driver.set_page_load_timeout(10)
            driver.implicitly_wait(30)
            driver.get(request.url)

            code = driver.find_element_by_xpath('//*[@name="code"]')
            code.click()
            code.clear()
            code.send_keys('fde9e')
            token1 = driver.find_element_by_xpath('//*[@name="token"]').get_attribute('value')
            token2 = driver.find_element_by_xpath('//*[@name="token2"]').get_attribute('value')
            print 'token1-2:', token1, token2
            # ActionChains(driver).click(subt).perform()
            # time.sleep(0.01)
            request.meta['token1'] = token1
            request.meta['token2'] = token2
            print 'xxxxxxxxxxxxx:', request.meta
            body = driver.page_source
            driver.close()
            return HtmlResponse(request.url, body=body, encoding='utf-8', request=request)
