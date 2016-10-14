# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  json
import  codecs
from scrapy.exceptions import DropItem


class KanFang(object):
    def __init__(self):
        self.file = codecs.open('kanfang.json', mode="wb", encoding='utf-8')

    def process_item(self,item, spider):
        if 'title' in item:
            line = json.dumps(dict(item))+'\n'
            self.file.write(line.decode('unicode_escape'))
            return item
        else:
            raise DropItem("Missing")
    def spider_closed(self,spider):
        self.file.close()