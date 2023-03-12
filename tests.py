import unittest

from conversions import convertCelsiusToKelvin
from conversions import convertCelsiusToFahrenheit
from conversions import convertFahrenheitToCelsius
from conversions import convertFahrenheitToKelvin
from conversions import convertKelvinToCelsius
from conversions import convertKelvinToFahrenheit
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
        print('testing -273.15')

    # Tests Celsius to Fahrenheit Conversions
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
        print('testing alphanumeric')

    def test_convertCelsiusToFahrenheit_minus17point79(self):
        value = convertCelsiusToFahrenheit(-17.79)
        # expected = "Must use a numeric value"
        self.assertAlmostEqual(value,-0.02, places=2)
        print('testing -17.79')


    # Tests Fahrenheit to Celsius Conversions
    def test_convertFahrenheitToCelsius_0(self):
        value = convertFahrenheitToCelsius(0)
        expected = -17.78
        self.assertAlmostEqual(value, expected, places=2, msg="tests 0")
        print('testing 0')

    def test_convertFahrenheitToCelsius_300(self):
        value = convertFahrenheitToCelsius(300.)
        expected = 148.89
        self.assertAlmostEqual(value, expected, places=2)
        print('testing 300')

    def test_convertFahrenheitToCelsius_minus99point37(self):
        value = convertFahrenheitToCelsius(-99.37)
        expected = -72.98
        self.assertAlmostEqual(value, expected, places=2)
        print('testing -99.37')

    def test_convertFahrenheitToCelsius_alpha(self):
        convertFahrenheitToCelsius("zero")
        # expected = "Must use a numeric value"
        self.assertRaises(TypeError)
        print('testing alphanumeric')

    def test_convertFahrenheitToCelsius_32(self):
        value = convertFahrenheitToCelsius(32)
        # expected = "Must use a numeric value"
        self.assertEqual(value,0)
        print('testing 32')


    # Tests Fahrenheit to Kelvin Conversions
    def test_convertFahrenheitToKelvin_0(self):
        value = convertFahrenheitToKelvin(0)
        expected = 255.372
        self.assertAlmostEqual(value, expected, places=2, msg="tests 0")
        print('testing 0')

    def test_convertFahrenheitToKelvin_300(self):
        value = convertFahrenheitToKelvin(300.)
        expected = 422.039
        self.assertAlmostEqual(value, expected, places=2)
        print('testing 300')

    def test_convertFahrenheitToKelvin_minus99point37(self):
        value = convertFahrenheitToKelvin(-99.37)
        expected = 200.167
        self.assertAlmostEqual(value, expected, places=2)
        print('testing -99.37')

    def test_convertFahrenheitToKelvin_alpha(self):
        convertFahrenheitToKelvin("zero")
        # expected = "Must use a numeric value"
        self.assertRaises(TypeError)
        print('testing alphanumeric')

    def test_convertFahrenheitToKelvin_minus459point67(self):
        value = convertFahrenheitToKelvin(-459.67)
        self.assertEqual(value,0)
        print('testing -459.67')



    # Tests Kelvin to Celsius Conversions
    def test_convertKelvinToCelsius_0(self):
        value = convertKelvinToCelsius(0)
        # expected = -273.15
        self.assertEqual(value,-273.15)
        print('testing 0')

    def test_convertKelvinToCelsius_300(self):
        value = convertKelvinToCelsius(300.)
        expected = 26.85
        self.assertAlmostEqual(value, expected, places=2)
        print('testing 300')

    def test_convertKelvinToCelsius_minus99point37(self):
        value = convertKelvinToCelsius(-99.37)
        expected = -372.52
        self.assertAlmostEqual(value, expected, places=2)
        print('testing -99.37')

    def test_convertKelvinToCelsius_alpha(self):
        convertKelvinToCelsius("zero")
        # expected = "Must use a numeric value"
        self.assertRaises(TypeError)
        print('testing alphanumeric')

    def test_convertKelvinToCelsius_273point15(self):
        value = convertKelvinToCelsius(273.15)
        self.assertEqual(value, 0)
        print('testing 273.15')


    # Tests Kelvin to Fahrenheit Conversions
    def test_convertKelvinToFahrenheit_0(self):
        value = convertKelvinToFahrenheit(0)
        expected = -459.67
        self.assertAlmostEqual(value, expected, places=2)
        print('testing 0')

    def test_convertKelvinToFahrenheit_300(self):
        value = convertKelvinToFahrenheit(300.)
        expected = 80.33
        self.assertAlmostEqual(value, expected, places=2)
        print('testing 300')

    def test_convertKelvinToFahrenheit_minus99point37(self):
        value = convertKelvinToFahrenheit(-99.37)
        expected = -638.54
        self.assertAlmostEqual(value, expected, places=2)
        print('testing -99.37')

    def test_convertKelvinToFahrenheit_alpha(self):
        convertKelvinToFahrenheit("zero")
        # expected = "Must use a numeric value"
        self.assertRaises(TypeError)
        print('testing alphanumeric')

    def test_convertKelvinToFahrenheit_minus459(self):
        value = convertKelvinToFahrenheit(-459)
        expected = -1285.87
        self.assertAlmostEqual(value, expected, places=2)
        print('testing ZeroK')
    '''

class RefactoredCheck(unittest.TestCase):
    def test_refactoredCelsiusToKelvin(self):
        assert convert("CELSIUS", "KELVIN", 0) == 273.15
        assert convert("CELSIUS", "FAHRENHEIT", 0) == 32
        assert convert('FAHRENHEIT', 'CELSIUS', 0) == -17.77777777777778
        assert convert('FAHRENHEIT', 'KELVIN', 0) == 255.3722222222222
        assert convert('KELVIN', 'CELSIUS', 0) == -273.15
        assert convert('KELVIN', 'FAHRENHEIT', 0) == -459.67



    '''
    def test_refactoredCelsiusToKelvin(self):
        value = convert("Celsius", "Kelvin", 0)
        expected = 273.15
        self.assertAlmostEqual(value, expected, places=2, msg="tests 0")
        print('refactored C to K testing 0')
    '''

if __name__ == '__main__':
    unittest.main(verbosity=2)
