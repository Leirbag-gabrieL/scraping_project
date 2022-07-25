import json
import scrapy
from item_scraper.spiders.url_builder import build_url
from item_scraper.spiders.take_a_line import random_line
root_build_url = "https://api.zenithwakfu.com/builder/api/build/"

class BuildSpider(scrapy.Spider):
    name = "build_spider"
    
    def start_requests(self):
        url = build_url(classes=["roub"], level_begin=0, level_end=50, page=1)
        headers = {
            "Host":"api.zenithwakfu.com",
            "Accept-Encoding":"gzip, deflate, br",
            "Origin":"https://www.zenithwakfu.com",
            "Connection":"keep-alive",
            "Referer":"https://www.zenithwakfu.com/",
            "Sec-Fetch-Dest":"empty",
            "Sec-Fetch-Mode":"cors",
            "Sec-Fetch-Site":"same-site",
            "User-Agent":random_line(),
            "Accept":"application/json, text/plain, */*",
            "Accept-Language":"en-US,en;q=0.5",
            "X-Requested-With":"XMLHttpRequest",
            "Pragma":"no-cache",
            "Cache-Control":"no-cache"
        }
        yield scrapy.Request(url, headers=headers, callback=self.parse)

    def parse(self, response):
        print("\n\n\n\n\n")
        jsonresp = json.loads(response.text)
        print(f"nombre de pages : {jsonresp['pages']}")
        for i in jsonresp['builds']:
            print(f"lien build : {i['link_build']} | user : {i['user']}")
        print("\n\n\n\n\n")