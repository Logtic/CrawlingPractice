import scrapy

class shareHouseSpider(scrapy.Spider):
    name = 'getUrl'

    #start_urls = ['https://tokyosharehouse.com/eng/area/search/3/',]
    
    def get_urls():
        base_url = 'https://tokyosharehouse.com/eng/area/search/3/'
        page_num = 2
        urlList = list()
        urlList.append(base_url)
        while(page_num<11):
            page = base_url + "page:%d"%page_num
            urlList.append(page)
            page_num = page_num+1
        return urlList
            
    start_urls = get_urls()

    def __init__(self):
        filename = 'getUrl.txt'
        with open(filename, 'w') as f:
            f.write('')

    def parse(self, response):
        filename = 'getUrl.txt'
        with open(filename, 'a') as f:
            href = response.css('div.list-item-inner div.lineupLeft a::attr(href)').extract()
            for line in href:
                f.write(line + '\n')

        
        






















