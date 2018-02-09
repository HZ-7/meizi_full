# -*- coding: utf-8 -*-
import scrapy,re,time

from meizi_all.items import MeiziAllItem


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['www.meizitu.com']
    start_urls = ['http://www.meizitu.com/']

    def parse(self, response):
        type_list = response.xpath('//*[@id="subcontent clearfix"]/div[2]/span/a')
        for type in type_list:
            type_page = type.xpath('./@href').extract()[0]
            yield scrapy.Request(url=type_page,callback= self.parse_type)

    def parse_type(self,response):
        node_list = response.xpath('//*[@id="maincontent"]/div[1]/ul/li')
        type_list = response.xpath('//*[@id="maincontent"]/div[1]/div/h3/text()[2]').extract()[0]
        type_text = re.findall('[\u4E00-\u9FA5]+',type_list)[0]
        next_page = response.xpath('//*[@id="wp_page_numbers"]/ul/li/a/@href')
        for node in node_list:
            page_url = node.xpath('./div/div/a/@href').extract()[0]
            image_title = node.xpath('./div/h3/a//text()').extract()[0]
            yield  scrapy.Request(url=page_url,callback=lambda response,type=type_text,img_tit = image_title:self.parse_page(response,type,img_tit))

        if '下一页' in response.xpath('//*[@id="wp_page_numbers"]/ul/li/a//text()').extract():
            next_url = "http://www.meizitu.com/a/"+ next_page[-2].extract()
            yield scrapy.Request(url=next_url, callback=self.parse_type)

    def parse_page(self,response,type,img_tit):
        type_text = type
        image_title = img_tit
        image_list = response.xpath('//*[@id="maincontent"]/div[2]/p[1]/img | //*[ @ id = "picture"]/p/img')
        for image in image_list:
            image_src = image.xpath('./@src').extract()[0]
            image_alt = image.xpath('./@alt').extract()[0]
            item = MeiziAllItem()
            item['type'] = type_text
            item['image_title'] = image_title
            item['image_src'] = image_src
            item['image_alt'] = image_alt
            yield item


