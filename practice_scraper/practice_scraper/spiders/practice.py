import scrapy


class PracticeSpider(scrapy.Spider):
    name = 'practice'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        title = response.xpath('//span[@class="title"]/text()').get()
        author = response.xpath('//span[@class="author-name"]/text()').get()
        date = response.xpath('//span[@class="date"]/text()').get()
        subheadings = response.xpath('//span[@class="subheading"]/text()').getall()
        text = response.xpath('//div[@class="text"]/text()').getall()
        description = response.xpath('//meta[@name="DC.Creator"]/@content').get()
        return {"title":title, "author":author, "date":date, "subheadings":subheadings,"text": text}


