# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

import csv

class OutfunItem(scrapy.Item):
    email = scrapy.Field()


class OutfunSpiderSpider(CrawlSpider):        
    name = "outfunspider"
    allowed_domains = []
    with open('locations.csv', 'rb') as csvfile:
            lines = csv.reader(csvfile, delimiter=';', quotechar='|')
            for line in lines:
                if len(line) > 1:
                    if "http" in line[3]:
                        allowed_domains.append(line[3])
    start_urls = set(allowed_domains)
    rules = (
        Rule(LinkExtractor(), callback="parse_item", follow= True),
        )
    rules = (
        # Follow any item link and call parse_item.
        Rule(LinkExtractor(allow=()), callback='parse_item'),
    )


    def parse_item(self,response):
        
        logging.info("DOES THIS EVER OCCUR???")
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        for href in response.xpath('//a/@href').extract():
            if "mailto" in href and "@" in href:
                item = OutfunItem()
                item["email"]=href[7:]
                return item

        
    

