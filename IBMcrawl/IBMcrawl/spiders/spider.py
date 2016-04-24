import scrapy
import re
from IBMcrawl.items import IBMcrawlItem

year = raw_input("Which year are you interested? \n")
start_url = [ ]

for i in range(1, 250):
    link = "http://www-03.ibm.com/press/us/en/pressreleases/finder.wss?rN="+str(i)+"&topic=458&year="+str(year)
    start_url.append(link)
    i = i + 20



class IBMcrawlSpider(scrapy.Spider):
    name = "IBMcrawl"
    allowed_domains = ['www-03.ibm.com']
    start_urls = start_url


    def parse(self,response):
        links = response.xpath("//a/@href").extract()
        crawledLinks = [ ]
        LinkPattern = re.compile("^/press/us/en/pressrelease/[0-9]+\.wss")
        for link in links:
            if LinkPattern.match(link) and not link in crawledLinks:
                crawledLinks.append("http://www-03.ibm.com"+link)
        for link in crawledLinks:
                yield scrapy.Request(link, callback=self.parse_every_link)
                
    def parse_every_link(self,response):
        for sel in response.xpath('//div[@id="ibm-top"]'):
            item = IBMcrawlItem()
            item["body"] = response.xpath('//div[@class = "ibm-container-body"]/p/text()').extract() 
                                                 
                                                 
            yield item
                                                