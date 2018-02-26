# -*- coding: utf-8 -*-
import scrapy
from BanGuMi.items import BangumiItem

class BgminfoSpider(scrapy.Spider):
    name = 'BgmInfo'
    # allowed_domains = ['bangumi.tv']
    url = 'http://bangumi.tv/anime/browser?sort=rank&page=%s'
    start_urls = ['http://bangumi.tv/anime/browser?sort=rank&page=%s'%i for i in range(1,189)]

    def parse(self, response):

        # li_all = response.find('ul',class_='browserFull').find_all('li')
        # print('llllllllllll',li_all)
        div = response.xpath('//div')[0]
        print('tttttttttttt',type(response),response)
        print('dddddddddddddd',type(div),div)
        for i in response.xpath('//ul[@class="browserFull"]/li'):
            print('iiiiiiiiiiiiiiiiiiiiii',i)
            item = BangumiItem()
            item['title']=i.xpath('./div[@class="inner"]/h3/a[@class="l"]/text()').extract()[0]
            item['url']=i.xpath('./div[@class="inner"]/h3/a[@class="l"]/@href').extract()[0]
            try:
                item['smail_title']=i.xpath('./div[@class="inner"]/h3/small[@class="grey"]/text()').extract()[0]
            except:
                item['smail_title']=''
            item['img']=i.xpath('./a[1]/span[1]/img/@src').extract()[0]
            item['rank']=i.xpath('./div[@class="inner"]/span[@class="rank"]/text()').extract()[0]
            item['fade']=i.xpath('./div[@class="inner"]/p[@class="rateInfo"]/small[@class="fade"]/text()').extract()[0]
            item['num']=i.xpath('./div[@class="inner"]/p[@class="rateInfo"]/span[@class="tip_j"]/text()').re(r'(\d+)')[0]
            item['info']=i.xpath('./div[@class="inner"]/p[@class="info tip"]/text()').extract()[0].strip()
            # l = zip(title,url,smail_title,img,rank,fade,num,info)
            # print('1111111111111111',title,url,smail_title,img,rank,fade,num,info)
            yield item
# '//*[@id="item_326"]/a/span[1]/img'.strip()




        # print('llllllllllll',l)

        # print('tttttttt',num,info)
