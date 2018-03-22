import scrapy

class naverSpider(scrapy.Spider):
    name = 'naver'

    start_urls = ['https://www.naver.com',]
    
    def parse(self, response):
        filename = 'naver.txt'
        with open(filename, 'w') as f:
            href = response.css('title::text').extract()
            for line in href:
                f.write(line + '\n')

        
        






















