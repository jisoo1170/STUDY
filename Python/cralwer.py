from icrawler.builtin import GoogleImageCrawler, BaiduImageCrawler
import os


def googleCrawl(name, image_dir):
   if name not in image_dir:
       try:
           os.mkdir(image_dir+"\\"+name)
       except:
           pass
   google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                       storage={'root_dir': image_dir+"\\"+name})
   google_crawler.crawl(keyword=name, max_num=1200,
                        min_size=None, max_size=None)

googleCrawl("영화 포스터", 'smile')

# '''
# def baiduCrawl(name, image_dir):
#    if name not in image_dir:
#        try:
#            os.mkdir(image_dir+"\\"+name)
#        except:
#            pass
#    baidu_crawler = BaiduImageCrawler(parser_threads=4, downloader_threads=8,
#                                        storage={'root_dir': image_dir+"\\"+name})
#    baidu_crawler.crawl(keyword=name, max_num=1200,
#                         min_size=None, max_size=None)
# baiduCrawl("紅蘿蔔", 'smile')
