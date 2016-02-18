import csv
import scrapy

            
    

class outfun(scrapy.Spider):
    def __init__(self):
        name = "outfun"
        allowed_domains = [url for url in self.load_urls()]
    
    def parse(self, response):
        with open("mailto.txt",'a') as f:
            for href in response.xpath('//a/@href').extract():
                if "mailto" in href:
                    f.write(href)
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)
        
    
            
    def load_urls(self):    
        with open('locations.csv', 'rb') as csvfile:
            lines = csv.reader(csvfile, delimiter=';', quotechar='|')
            for line in lines:
                if len(line) > 1:
                    if "http" in line[3]:
                        yield line

out = outfun()