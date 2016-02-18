# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class OutfunPipeline(object):
    def __init__(self):
        self.file = open('mailto.txt','a')
    
    def process_item(self, item, spider):
        if "mailto" in href and "@" in href:
                self.file.write(href[7:]+'\n')
        return item
