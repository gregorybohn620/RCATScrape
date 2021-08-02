import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from news_scraper.items import News


class CnnSpider(scrapy.Spider):
    name = 'cnn'
    allowed_domains = ['www.cnn.com']
    #start_urls = ['http://www.cnn.com/africa']
    start_urls = ['https://www.cnn.com/2021/07/30/africa/tigray-un-food-aid-famine-intl/index.html']

    def parse(self, response):
        news = News()
        news["title"] = response.xpath('//h1[@class="pg-headline"]/text()').get()
        news["url"] = response.url
        news["source"] = "CNN"
        news["author"] = response.xpath('//meta[@name="author"]/text()').get()
        news["date"] =  response.xpath('//meta[@name="lastmod"]/@content').get()
        news["description"] =response.xpath('//meta[@name="description"]/').get()

        return news



