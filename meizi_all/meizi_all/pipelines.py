# -*- coding: utf-8 -*-
# 项目管道文件
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy,os
from meizi_all.settings import IMAGES_STORE
class MeiziAllPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item
    offset = 0
    def get_media_requests(self, item, info):
        imagsrc = item['image_src']
        yield scrapy.Request(imagsrc)

    def item_completed(self, results, item, info):
#         创建分类文件夹
        if not os.path.exists(IMAGES_STORE + item['type']):
            os.mkdir(IMAGES_STORE + item['type'])
#         创建图片标题文件夹
        if not os.path.exists(IMAGES_STORE +item['type']+'/'+ item['image_title']):
            os.mkdir(IMAGES_STORE +item['type']+'/'+ item['image_title'])
        image_path = [x['path'] for ok, x in results if ok]
#         重命名图片
        os.rename(IMAGES_STORE + image_path[0], IMAGES_STORE +item['type']+'/'+ item['image_title']+ "/" + item['image_alt'] +"-"+ str(self.offset)+".jpg")
        self.offset += 1
