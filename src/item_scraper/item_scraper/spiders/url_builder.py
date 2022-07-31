from re import sub
from item_scraper.spiders.take_a_line import random_line

def build_url(site_url):
    if not site_url.startswith('https://www.zenithwakfu.com/builder'):
        print("\n\nTon url doit commencé par https://www.zenithwakfu.com/builder\n\n")
        return None , None

    base_url = "https://api.zenithwakfu.com/builder/api/list?"
    try:
        query = sub("&page=\d+", "", site_url.split('?')[1])
    except IndexError:
        print("\n\nMauvaise url, il faut une url de recherche, pas une url générale\n\n")
        return None, None
    base_request = base_url + query
    pageless_url = base_request + "&page="
    return base_request, pageless_url

def generate_builds_header():
    headers = {
            "Host": "api.zenithwakfu.com",
            "Accept-Encoding": "gzip, deflate, br",
            "Origin": "https://www.zenithwakfu.com",
            "Connection": "keep-alive",
            "Referer": "https://www.zenithwakfu.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": random_line(),
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "X-Requested-With": "XMLHttpRequest",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }
    return headers

def generate_single_build_header():
    headers = {
            "Host": "api.zenithwakfu.com",
            "User-Agent": random_line(),
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.zenithwakfu.com/",
            "Origin": "https://www.zenithwakfu.com",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-site",
            "X-Requested-With": "XMLHttpRequest",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache"
        }
    return headers