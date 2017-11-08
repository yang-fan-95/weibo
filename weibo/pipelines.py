# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class WeiboPipeline(object):
    def process_item(self, item, spider):
        fileName = "weibo_info.txt"
        with open(fileName, 'a', encoding='utf-8') as fp:
            fp.write(item['text'] + '\n')

        return item
