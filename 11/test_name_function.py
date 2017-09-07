import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """test name_function.py"""

    def test_first_last_name(self):
        """Can handle Janis Joplin correctly?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """Can handle Wolfgang Amadeus Mozart correctly?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()