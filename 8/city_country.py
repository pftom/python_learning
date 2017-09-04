# 8-6
def city_country(city, country):
    """formatted city and country"""
    formatted_city_country = city + ", " + country
    return formatted_city_country


city_one = city_country('changde', 'china')
print(city_one)

city_two = city_country('diaozhou', 'china')
print(city_two)

city_three = city_country('xinayng', 'china')
print(city_three)


def make_album(singer, special, songs_count=0):
    """make a album 8-7"""
    album = {'singer': singer, 'special': special}
    if songs_count:
        album['songs_count'] = songs_count

    return album


album_one = make_album('weige', 'dahai')
print(album_one)

album_two = make_album('azhe', 'linjunjie', 3)
print(album_two)

album_three = make_album('huang', 'hhh')
print(album_three)

while True:
    print("\nPlease tell me the album singer and special")
    print("(Enter 'q' at any time to quit)")

    singer = input("Singer: ")
    if singer == 'q':
        break

    special = input("Special: ")
    if special == 'q':
        break

    album = make_album(singer, special)
    print(album)
