import unittest

from conversions import convertCelsiusToKelvin
from conversions import convertCelsiusToFahrenheit
from conversions import convertFahrenheitToCelsius
from conversions import convertFahrenheitToKelvin
from conversions import convertKelvinToCelsius
from conversions import convertKelvinToFahrenheit
from conversions_refactored import convert


class ConversionsCheck(unittest.TestCase):

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

    # Test refactored temp functions
    def test_refactored_CtoF(self):
        print("C to F")
        value = convert("CELSIUS", "FAHRENHEIT", 0)
        expected = 32
        self.assertEqual(value, expected)


    def test_refactored_CtoK(self):
        print("C to K")
        value = convert("CELSIUS", "KELVIN", 0)
        expected = 273.15
        self.assertEqual(value,expected)

    def test_refactored_FtoC(self):
        print("F to C")
        value = convert('FAHRENHEIT', 'CELSIUS', 0)
        expected = -17.77777777777778
        self.assertAlmostEqual(value, expected, places=2)

    def test_refactored_FtoK(self):
        print("F to K")
        value = convert('FAHRENHEIT', 'KELVIN', 0)
        expected = 255.3722222222222
        self.assertAlmostEqual(value, expected, places=2)

    def test_refactored_KtoC(self):
        print("K to C")
        value = convert('KELVIN', 'CELSIUS', 0)
        expected = -273.15
        self.assertEqual(value, expected)

    def test_refactored_KtoF(self):
        print("K to F")
        value = convert('KELVIN', 'FAHRENHEIT', 0)
        expected = -459.67
        self.assertAlmostEqual(value, expected, places=2)

    # Test refactored distance functions
    def test_refactored_MilestoYards(self):
        print("Miles to Yards")
        value = convert('MILES', 'YARDS', 1)
        expected = 1760
        self.assertAlmostEqual(value, expected, places=2)

    def test_refactored_MilestoMeters(self):
        print("Miles to Meters")
        value = convert('MILES', 'METERS', 1)
        expected = 1609.344
        self.assertAlmostEqual(value, expected, places=2)

    def test_refactored_YardstoMiles(self):
        print("Yards to Miles")
        value = convert('YARDS', 'MILES', 1760)
        expected = 1
        self.assertAlmostEqual(value, expected, places=2)

    def test_refactored_YardtoMeters(self):
        print("Yards to Meters")
        value = convert('YARDS', 'METERS', 1)
        expected = 0.9144
        self.assertAlmostEqual(value, expected, places=2)

    def test_refactored_MeterstoMiles(self):
        print("Meters to Miles")
        value = convert('METERS', 'MILES', 1609.344)
        expected = 1
        self.assertAlmostEqual(value, expected, places=2)

    def test_refactored_MeterstoYards(self):
        print("Meters to Yards")
        value = convert('METERS', 'YARDS', 1)
        expected = 1.0936
        self.assertAlmostEqual(value, expected, places=2)

    def test_refactored_same_units(self):
        print("test same units")
        assert convert('FAHRENHEIT', 'FAHRENHEIT', 32) == 32
        assert convert('CELSIUS', 'CELSIUS', 100) == 100
        assert convert('KELVIN', 'KELVIN', 273.15) == 273.15
        assert convert('MILES', 'MILES', 10) == 10
        assert convert('YARDS', 'YARDS', 100) == 100
        assert convert('METERS', 'METERS', 500) == 500

    def test_bad_request(self):
        print("Meters to Kelvin")
        value = convert('METERS', 'KELVIN', 1)
        expected = None
        self.assertEqual(value, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
