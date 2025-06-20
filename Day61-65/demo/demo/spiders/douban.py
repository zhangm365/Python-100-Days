
"""
蜘蛛程序
"""

import scrapy
from scrapy import Selector, Request
from scrapy.http import HtmlResponse

from demo.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]

    def start_requests(self):
        for page in range(10):
            url = f"https://movie.douban.com/top250?start={page * 25}"
            yield Request(url=url, callback=self.parse)

    def parse(self, response: HtmlResponse):
        sel = Selector(response)
        movie_items = sel.css('#content .grid_view > li')
        # movie_items = sel.css('#content > div > div.article > ol > li')
        for movie_sel in movie_items:
            item = MovieItem()
            item['title'] = movie_sel.css('.title::text').extract_first()
            item['score'] = movie_sel.css('.rating_num::text').extract_first()
            item['motto'] = movie_sel.css('.inq::text').extract_first()
            yield item



