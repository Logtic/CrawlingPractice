import scrapy


class InfoSpider(scrapy.Spider):
    name = 'getInfo'

    allowed_domains = ["tokyosharehouse.com"]

    def __init__(self):
        filename = 'getInfo.txt'
        with open(filename, 'w') as f:
            f.write('')
    def urlList():
        filename = 'getUrl.txt'
        baseUrl = 'https://tokyosharehouse.com'
        newList = list()
        with open(filename, 'r') as f:
            while True:
                line = f.readline()
                if not line: break
                else:
                    newline = baseUrl + line
                    newList.append(newline)
        return newList

    start_urls = urlList()


    def parse(self, response):
        filename = 'getInfo.txt'
        with open(filename, 'a') as f:
            f.write(response.url+'\n');
            shareHouseName = response.css('div.leftHouseName h1::text').extract()
            for line in shareHouseName:
                f.write(line + '\n')
            detailRoom = response.css('div.room-item div.room-info span::text').extract()
            for line in detailRoom:
                f.write(line + '\t')
            f.write("\n")
            roomPrice = response.css('div.room-item div.room-price div.price::text').extract()
            for line in roomPrice:
                f.write(line[1:] + '\t')
            f.write("\n")
            roomFee = response.css('div.room-item div.room-price div.fee::text').extract()
            for line in roomFee:
                f.write(line[1:] + '\t')
            f.write('\n\n\n')








