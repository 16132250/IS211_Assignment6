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
        pass
        print("Must use a numeric value")

def convertFahrenheitToCelsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius

    :param fahrenheit:
    :return:
    """
    try:
        celsius = float((fahrenheit - 32) * 5 / 9)
        return celsius

    except TypeError:
        print("Must use a numeric value")

def convertFahrenheitToKelvin(fahrenheit):
    """
    Convert Fahrenheit to Kelvin

    :param fahrenheit:
    :return:
    """
    try:
        kelvin = float((fahrenheit + 459.67) * 5 / 9)
        return kelvin

    except TypeError:
        print("Must use a numeric value")

def convertKelvinToCelsius(kelvin):
    """
    Convert Kelvin to Celsius

    :param :
    :return:
    """
    try:
        celsius = kelvin - 273.15

        return celsius

    except TypeError:
        print("Must use a numeric value")

def convertKelvinToFahrenheit(kelvin):
    """
    Convert Kelvin to Fahrenheit

    :param :
    :return:
    """
    try:
        fahrenheit = 1.8 * (kelvin - 273.15) + 32

        return fahrenheit

    except TypeError:
        print("Must use a numeric value")



