# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = ['https://www.reddit.com/r/gameofthrones/']

    def parse(self, response):
        #Extracting the content using css selectors
        titles = response.css('h3._eYtD2XCVieq6emjKBH3m::text').extract()
        votes = response.css('div._23h0-EcaBUorIHC-JZyh6J > div > div::text').extract()
        times = response.css('div.BiNC74axuTz66dlnEgicY > div > div._3AStxql1mQsrZuUIFP9xSg.nU4Je7n-eSXStTBAPMYt8 a::text').extract()
        urls = response.css('div.BiNC74axuTz66dlnEgicY > div > div._3AStxql1mQsrZuUIFP9xSg.nU4Je7n-eSXStTBAPMYt8 a::attr(href)').extract()
        comments = response.css('div._3-miAEojrCvx_4FQ8x3P-s > a > span::text').extract()
        #Give the extracted content row wise
        for item in zip(titles,votes,times,urls,comments):
            #print("item "+item)
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'vote' : item[1],
                'created_at' : item[2],
                'url' : item[3],
                'comments' : item[4],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
