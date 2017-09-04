def make_shirt(size="large", msg="I love Python"):
    """make a T-Shirt"""
    print("The size is " + str(size) + ", The msg in this clothes " + msg)


# call this def
make_shirt(18, 'I love this world!')
make_shirt(msg='I love youy', size=12)
make_shirt()
make_shirt("medium")
make_shirt(size='large', msg="I love you too!")


# add another def
def describe_city(name, country='China'):
    """make a country"""
    print(name + "is in " + country)


describe_city('changde')
describe_city('diaozhou')
describe_city('Stanford', 'US')
