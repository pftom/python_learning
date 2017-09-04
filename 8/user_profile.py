def build_profile(first, last, **user_info):
    """create a dict about me"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


my_first_brief = build_profile('pf', 'tom', 
                            target='enhance this world',
                            current='love what you do',
                            future='do what you love')
print(my_first_brief)