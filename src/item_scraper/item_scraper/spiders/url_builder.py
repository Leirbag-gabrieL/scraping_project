from random import random
from item_scraper.spiders.take_a_line import random_line

authorized_flags = ["dps", "heal", "tank", "supp", "dj", "bu", "pvp", "easy", "medium", "hard"]

authorized_class = ["feca", "osa", "enu", "sram", "xel", "eca", "eni", "iop", "cra", "sadi", "sacri", "panda", "roub", "zobal", "ougi", "steam", "elio", "hupper"]

def build_url(classes= [], level_begin= 0, level_end= 230, flags = []):
    base_url = "https://api.zenithwakfu.com/builder/api/list?"

    if len(flags) != len(set(flags)):
        print("Wrong flag format")
        return None
    
    if len(classes) != len(set(classes)):
        print("Wrong class format")
        return None

    if level_begin > level_end or level_begin < 0 or level_end > 230:
        print("Wrong level")
        return None

    try:
        for i in range(len(flags)):
            index = authorized_flags.index(flags[i]) + 1
            if i == 0:
                base_url += f"bflags={index}"
            else:
                base_url += f"%2C{index}"
    except ValueError:
        print("Wrong flag")
        return None

    try:
        for i in range(len(classes)):
            index = authorized_class.index(classes[i]) + 1
            if i == 0:
                if flags:
                    base_url += "&"
                base_url += f"jobs={index}"
            else:
                base_url += f"%2C{index}"
    except ValueError:
        print("Wrong class")
        return None
    
    if flags or classes:
        base_url += "&"
    
    base_url += f"level={level_begin}%2C{level_end}"
    base_url_pageless = base_url + "&page="

    return base_url, base_url_pageless

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