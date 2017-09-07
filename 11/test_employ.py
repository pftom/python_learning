import unittest

from employ import Employ


class TestEmployCase(unittest.TestCase):
    """The test case for Employ attr and behavior"""
    
    def setUp(self):
        self.employ_one = Employ('pf', 'tom', 10000)
    
    def test_give_default_raise(self):
        """Test give default salary"""
        self.employ_one.give_raise()

        self.assertEqual(15000, self.employ_one.annual_salary)

    def test_give_custom_raise(self):
        """Test give custom salary"""
        self.employ_one.give_raise(6000)

        self.assertEqual(16000, self.employ_one.annual_salary)


unittest.main()