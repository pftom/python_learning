def get_formatted_city_country(city, country, population=0):
    """11-1 test city_functions"""
    if population:
        formatted_city_country = (city + ', ' + 
        country + " - population " + str(population))
    else:
        formatted_city_country = city + ', ' + country
    return formatted_city_country.title()
