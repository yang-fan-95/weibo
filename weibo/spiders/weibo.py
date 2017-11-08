# -*- coding: utf-8 -*-
import scrapy
import json

from scrapy import Request

from weibo.items import WeiboItem


class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['https://m.weibo.cn']
    start_urls = ['https://m.weibo.cn']
    cookie={
        '''
            填入自己的账号的cookie
        '''
    }
    headers = {"Host":
                   "weibo.cn",
               "Accept":
                   "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Data":
                   "Thu, 19 Oct 2017 09:49:18 GMT",
               "Accept-Language":
                   "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
               "Accept-Encoding":
                   "gzip, deflate",
               "User-Agent":
                   "Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9A334 Safari/7534.48.3 "}

    def start_requests(self):
        for i in range(1,95962):
            yield Request('https://m.weibo.cn/api/comments/show?id=4160547694498927&page=' + str(i),cookies=self.cookie, meta=self.headers,
                    callback=self.parse)

    def parse(self, response):
        sites = json.loads(response.body_as_unicode())
        isOk = sites["ok"]
        items = []
        if isOk == 1:
            data = sites["data"]
            for j in range(len(data)):
                item = WeiboItem()
                item['text'] = data[j]['text']
                items.append(item)
            return items
        else:
            Request('https://m.weibo.cn/api/comments/show?id=4160547694498927&page=500', cookies=self.cookie,
                    meta=self.headers)
