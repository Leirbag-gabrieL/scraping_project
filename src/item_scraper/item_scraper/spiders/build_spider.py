from email import header
import json
from wsgiref import headers
import scrapy
from item_scraper.spiders.url_builder import *
import unidecode
root_build_url = "https://api.zenithwakfu.com/builder/api/build/"
base_url_pageless = ""

class BuildSpider(scrapy.Spider):
    name = "build_spider"

    def start_requests(self):
        global base_url_pageless
        global root_build_url
        
        url, base_url_pageless = build_url(classes=['panda'], level_begin=50, level_end=50, flags=['hard', 'dps'])
        yield scrapy.Request(url, headers= generate_builds_header(), callback=self.parse)

    def parse(self, response):
        jsonresp = json.loads(response.text)

        for i in range(1,jsonresp['pages']+1):
            yield scrapy.Request(url=base_url_pageless + str(i), headers=generate_builds_header(), callback=self.parse_page_with_builds)
    
    def parse_page_with_builds(self, response):
        jsonresp = json.loads(response.text)

        for hash in list(map(lambda build: build['link_build'], jsonresp['builds'])):
            yield scrapy.Request(url=root_build_url + hash, headers=generate_single_build_header(), callback=self.parse_page_with_single_build)
    
    def parse_page_with_single_build(self, response):
        jsonresp = json.loads(response.text)
        return {"item_names": list(map(lambda item: unidecode.unidecode(item['name_equipment']), jsonresp['equipments'])),
                "build_name": unidecode.unidecode(jsonresp['name_build']) if jsonresp['name_build'] else "build sans nom"
        }