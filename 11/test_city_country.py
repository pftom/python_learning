import unittest

from city_functions import get_formatted_city_country


class CityTestCase(unittest.TestCase):
    """the test class for test formatted city and country"""

    def test_city_country(self):
        """Can city, country like santiago chile run correctly?"""
        formatted_city_country = get_formatted_city_country(
            'santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """
        Can city, population - population xxx like
        Santiago Chile - population 500000 run correctly?
        """
        formatted_city_country_population = get_formatted_city_country(
            'santiago', 'chile', population=500000)
        self.assertEqual(
            formatted_city_country_population, 
            'Santiago, Chile - Population 500000')


unittest.main()