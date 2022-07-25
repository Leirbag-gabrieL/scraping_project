authorized_flags = ["dps", "heal", "tank", "supp", "dj", "bu", "pvp", "easy", "medium", "hard"]

authorized_class = ["feca", "osa", "enu", "sram", "xel", "eca", "eni", "iop", "cra", "sadi", "sacri", "panda", "roub", "zobal", "ougi", "steam", "elio", "hupper"]

def build_url(classes= [], level_begin= 0, level_end= 230, page = 1, flags = []):
    base_url = "https://api.zenithwakfu.com/builder/api/list?"

    if page < 1:
        "Wrong page number"
        return None

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
    
    base_url += f"level={level_begin}%2C{level_end}&page={page}"
    return base_url