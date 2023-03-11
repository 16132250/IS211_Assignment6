def convertCelsiusToKelvin(celsius):
    """
    Convert Celsius to Kelvin

    :param celsius:
    :return:
    """

    try:
        kelvin = celsius + 273.15
        return kelvin

    except TypeError:
        pass
        # print("Must use a numeric value")

def convertCelsiusToFahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit

    9/5 * celsius + 32

    :param celsius:
    :return:
    """
    try:
        fahrenheit = float((9/5 * celsius) + 32)
        return fahrenheit

    except TypeError:
        print("Must use a numeric value")

def convertFahrenheitToCelsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius

    :param fahrenheit:
    :return:
    """

    celsius = 0

    return celsius

def convertFahrenheitToKelvin(fahrenheit):
    """
    Convert Fahrenheit to Kelvin

    :param fahrenheit:
    :return:
    """

    kelvin = 'k'

    return kelvin

def convertKelvinToCelsius(fahrenheit):
    """
    Convert Kelvin to Celsius

    :param :
    :return:
    """

    celsius = 0

    return celsius

def convertKelvinToFahrenheit(fahrenheit):
    """
    Convert Kelvin to Celsius

    :param :
    :return:
    """

    celsius = 0

    return celsius


'''
Celsius to Kelvin
Celsius to Fahrenheit

Fahrenheit to Celsius
Fahrenheit to Kelvin

Kelvin to Celsius
Kelvin to Fahrenheit
'''


