# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.item import Field, Item
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose


class grabstoreItem(Item):
    product_name = Field()
    price = Field()
    listing_number = Field()
    expiry = Field()
    expired = Field()
    seller = Field()
    photo_url = Field()
    url = Field()
    sku = Field()



class GrabstoreSpider(CrawlSpider):
    name = 'grabstore'
    allowed_domains = ['trademe.co.nz']
    start_urls = ['https://www.trademe.co.nz/stores/grabstore?v=List']

    custom_settings = {
        'FEED_FORMAT' : 'csv',
        'FEED_URI' : 'grabstore-feed.csv'
    }    
    
    rules = (
        #Rule(LinkExtractor(allow=r'&page='), follow=True),
        Rule(LinkExtractor(allow=r'rsqid='), callback='parse_item'),
    )

    def parse_item(self, response):
        #item = {}
        item = ItemLoader(grabstoreItem(),response)
        item.add_css('product_name', '#ListingTitleBox_TitleText > h1::text')
        item.add_css('listing_number', 'div.listing-id::text', MapCompose(lambda i: ''.join(c for c in i if c.isdigit())))
        item.add_css('price', '#BuyNow_BuyNow::text')
        item.add_css('expiry', '#ClosingTime_ClosingTime::text')
        item.add_css('seller', '#SellerProfile_MemberNicknameLink::text')
        item.add_css('photo_url', '#zoom > div > img::attr(src)')
        expired =  response.css('#ExpiredListingOptions_ExpiredHeading').extract_first()
        if expired:
            item.add_value('expired', 'Expired')
        else:
            item.add_value('expired', 'Not Expired')

        #item.add_xpath('sku', '/html/head/script[19]/text()')
        try:
            data = json.loads(response.xpath('//script[@type="application/ld+json"]//text()').extract_first())
            item.add_value('sku', data['sku'])
            item.add_value('url', data['url'])
        except:
            data = response.xpath('//script[text()[contains(.,"SKU")]]//text()').extract_first()
            item.add_value('sku', data.split('"SKU":')[1].split('"')[1])
            item.add_value('url', response.request.url)
            
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        #/html/head/script[19]/text()
        return item.load_item()
