chars = {
    'a': 'abc',
    'b': 'bcd',
    'c': 'cde',
    }
for char_item_index, char_item_value in chars.items():
    print(char_item_index + '\n' + char_item_value)


aliens = []

for alien_number in range(30):
    new_alien = { 'color': 'green', 'points': 5, 'speed': 'slow' }
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("The total length of list is " + str(len(aliens)))




print('-------')
pf_tom = {
    'name': 'tom',
    'age': 21
    }

pf_mRc = {
    'name': 'mRc',
    'age': 20
    }

person_list = [pf_tom, pf_mRc]


for person in person_list:
    print("My name is " + person['name'] + ", and my age is " + str(person['age']))


# 6-9
print('-----')
favorite_places = {
    'tom': ['changde', 'shanghai', 'Stanford'],
    'mRc': ['diaozhou', 'shanghai', 'Stanford'],
    'tao': ['xinyang', 'shanghai', 'HanDe']
    }

for person, places in favorite_places.items():
    if len(places) > 1:
        print(person + "'s favorite place are ")
        for place in places:
            print('\t' + place)
    else:
        print(person + "'s favorite place is ")
        for place in places:
            print('\t' + place)


# 6-11
print('-----')
cities = {
    'changde': {
        'country': 'China',
        'population': 3600,
        'fact': 4,
        },
    'shanghai': {
        'country': 'China',
        'population': 4000,
        'fact': 3,
        },
    'Stanford': {
        'country': 'US',
        'population': 2000,
        'fact': 4,
        },
    }

for city, info in cities.items():
    print("The name of this city is " + city)
    for key, value in info.items():
        if key == 'population' or key == 'fact':
            print('\t' + key + ':' + str(value))
        else:
            print('\t' + key + ':' + value)