# -*- coding: utf-8 -*-
  #coding=utf-8
import scrapy
from  kanfang.items import FangwuItem


sturl=[]
for i in range(1,150):
      sturl.append('http://newhouse.cd.fang.com/house/s/b9%d/?ctm=1.cd.xf_search.page.12'%i)

# print(sturl)

class KanfangSpider(scrapy.Spider):
  name = "kanfang"
  allowed_domains = [".cd.fang.com"]
  start_urls = sturl

  def parse(self, response):
        # filename = response.url.split('/')[-2]+".html"
        # with open(filename,'wb') as fb:
        #     fb.write(response.body)
        lis = response.css('#bx1 > div > div.contentListf.fl.clearfix > div.nhouse_list_content > div > div > ul li')
        for li in lis:
            item = FangwuItem() #init item

            if li.css('.nlcd_name')!=[]:
                print('yangshi1')
                if li.css('.nlcd_name').xpath('a/text()')!=[]:
                    item['title'] = ("".join(li.css('.nlcd_name').xpath('a/text()').extract())).strip()
                    item['link'] = ("".join(li.css('.nlcd_name').xpath('a/@href').extract())).strip()
                    item['address'] =("".join(li.css('.relative_message a').xpath('@title').extract())).strip()
                    # item['ip'] =response.css('#result .well p').xpath('code/text()')
                    # print ('%s') %response.css('#result .well p').xpath('code/text()')
                    item['money'] = ("".join(li.css('.nhouse_price').xpath('span/text()').extract()+li.css('.nhouse_price').xpath('em/text()').extract())).strip()
                    item['img'] = ("".join(li.css('.nlc_img a').xpath('img/@src').extract())).strip()

                else:
                     pass
            else:
                print('yangshi2')
                print(li)
                if li.xpath('div/div/dl/dd[1]/div[1]/h4/a/text()')!=[]:
                    item['title'] = ("".join(li.xpath('div/div/dl/dd[1]/div[1]/h4/a/text()').extract())).strip()
                    item['link'] = ("".join(li.xpath('div/div/dl/dt/a/@href').extract())).strip()
                    item['address'] = ("".join(li.xpath('div/div/dl/div/a/text()').extract())).strip()
                    item['money'] = ("".join(li.xpath('div/div/dl/dd[1]/div[2]/h5/span/text()').extract())+"".join(li.xpath('div/div/dl/dd[1]/div[2]/h5/em/text()').extract())).strip()
                    item['img'] = ("".join(li.xpath('div/div/dl/dt/a').xpath('img/@src').extract())).strip()
                else:
                    pass
            yield item





