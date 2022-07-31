from email import header
import json
from wsgiref import headers
import scrapy
from item_scraper.spiders.url_builder import *
import pandas as pd
root_build_url = "https://api.zenithwakfu.com/builder/api/build/"
base_url_pageless = ""
item_array = {}
shitty_build_count = 0

class BuildSpider(scrapy.Spider):
    name = "build_spider"

    def start_requests(self):
        global base_url_pageless
        global root_build_url
        global item_array
        
        request = getattr(self, 'request', None)
        display = getattr(self, 'display', None)


        if display is not None and request is not None:
            yield scrapy.Request(url=request, callback=self.printer)
            return

        if(request is None):
            raise scrapy.exceptions.CloseSpider("Mettre -a request=<lien de requête ici> à l'appel du programme")
        
        url, base_url_pageless = build_url(request)
        if(url is None):
            raise scrapy.exceptions.CloseSpider("Mauvaise request, il faut copier coller une requête directement du site")

        yield scrapy.Request(url, headers= generate_builds_header(), callback=self.parse)
    

    def printer(self, response):
        print(f"\n\n{response.text}\n\n")

    def parse(self, response):
        jsonresp = json.loads(response.text)

        for i in range(1,jsonresp['pages']+1):
            yield scrapy.Request(url=base_url_pageless + str(i), headers=generate_builds_header(), callback=self.parse_page_with_builds)
    
    def parse_page_with_builds(self, response):
        jsonresp = json.loads(response.text)
        global shitty_build_count
        for build in jsonresp['builds']:
            if len(build['equipments_light']) >= 10:
                yield scrapy.Request(url=root_build_url + build['link_build'], headers=generate_single_build_header(), callback=self.parse_page_with_single_build)
            else:
                shitty_build_count += 1
    
    def parse_page_with_single_build(self, response):
        jsonresp = json.loads(response.text)
        for item in jsonresp['equipments']:
            if item['name_equipment'] in item_array:
                item_array[item['name_equipment']] += 1
            else:
                item_array[item['name_equipment']] = 1

    def closed(self, reason):
        if reason == "finished":
            pd.DataFrame(sorted(item_array.items(), key=lambda item: item[1], reverse=True)).to_csv('out.csv')
            print(f"\n\n\nShitty build count : {shitty_build_count}\n\n\n")