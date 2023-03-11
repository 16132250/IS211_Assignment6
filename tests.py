import unittest

from conversions import convertCelsiusToKelvin
from conversions import convertCelsiusToFahrenheit

from conversions_refactored import convert

class ConversionsCheck(unittest.TestCase):
    '''
    # Tests Celsius to Kelvin Conversions
    def test_convertCelsiusToKelvin_0(self):
        value = convertCelsiusToKelvin(0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2, msg="tests 0")
        print('testing 0')

    def test_convertCelsiusToKelvin_300(self):
        value = convertCelsiusToKelvin(300.)
        expected = 573.15
        self.assertAlmostEqual(value, expected, places=2)
        print('testing 300')

    def test_convertCelsiusToKelvin_minus99point37(self):
        value = convertCelsiusToKelvin(-99.37)
        expected = 173.78
        self.assertAlmostEqual(value, expected, places=2)
        print('testing -99.37')

    def test_convertCelsiusToKelvin_alpha(self):
        convertCelsiusToKelvin("zero")
        # expected = "Must use a numeric value"
        self.assertRaises(TypeError)
        print('testing alphanumeric')

    def test_convertCelsiusToKelvin_minus273point15(self):
        value = convertCelsiusToKelvin(-273.15)
        # expected = "Must use a numeric value"
        self.assertEqual(value,0)
        print('testin -273.15')
    '''


    # Tests Celsius to Kelvin Conversions
    def test_convertCelsiusToFahrenheit_0(self):
        value = convertCelsiusToFahrenheit(0)
        expected = 32
        self.assertAlmostEqual(value, expected, places=2, msg="tests 0")
        print('testing 0')

    def test_convertCelsiusToFahrenheit_300(self):
        value = convertCelsiusToFahrenheit(300.)
        expected = 572
        self.assertAlmostEqual(value, expected, places=2)
        print('testing 300')

    def test_convertCelsiusToFahrenheit_minus99point37(self):
        value = convertCelsiusToFahrenheit(-99.37)
        expected = -146.866
        self.assertAlmostEqual(value, expected, places=2)
        print('testing -99.37')

    def test_convertCelsiusToFahrenheit_alpha(self):
        convertCelsiusToFahrenheit("zero")
        # expected = "Must use a numeric value"
        self.assertRaises(TypeError)
        # print('testing alphanumeric')

    def test_convertCelsiusToFahrenheit_minus17point79(self):
        value = convertCelsiusToFahrenheit(-17.79)
        # expected = "Must use a numeric value"
        self.assertAlmostEqual(value,-0.02, places=2)
        print('testing -17.79')







    '''
    def test_convertCelsiusToFahrenheit(self):
        value = convertCelsiusToFahrenheit(0)
        expected = 32
        self.assertAlmostEqual(value, expected, places=2)

    
    def test_convertCelsiusToFahrenheit_2(self):
        value = convertCelsiusToKelvin(300.)
        expected = 572.0
        self.assertAlmostEqual(value, expected, places=2)

    # TODO: Add tests for the new functions to convert F to C and F to K

    def test_convert_CelsiusToKelvin(self):
        value = convert("Celsius", "Kelvin", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2)

    # TODO: Add tests for the new functions to convert temperatures and distances

'''

if __name__ == '__main__':
    unittest.main(verbosity=2)
