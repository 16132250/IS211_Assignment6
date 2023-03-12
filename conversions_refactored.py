class ConversionNotPossible(Exception):
    def __init__(self, fromUnit, toUnit):
        self.fromUnit = fromUnit
        self.toUnit = toUnit

    def __str__(self):
        return f"Can't compare {self.fromUnit} to {self.toUnit}"

def convert(fromUnit, toUnit, value):
    """
    Converts between Fahrenheit, Celsius and Kelvin, and
    Converts between Miles, Yards and Meters.
    :param fromUnit:
    :param toUnit:
    :param value:
    :return:
    """
    try:
        if fromUnit.upper() == toUnit.upper():
            return value
        elif fromUnit.upper() == 'CELSIUS' and toUnit.upper() == 'KELVIN':
            return float(value + 273.15)
        elif fromUnit.upper() == "CELSIUS" and toUnit.upper() == "FAHRENHEIT":
            return float(9 / 5 * value + 32)
        elif fromUnit.upper() == "FAHRENHEIT" and toUnit.upper() == "CELSIUS":
            return float((value - 32) * 5/9)
        elif fromUnit.upper() == "FAHRENHEIT" and toUnit.upper() == "KELVIN":
            return float((value + 459.67) * 5/9)
        elif fromUnit.upper() == "KELVIN" and toUnit.upper() == "CELSIUS":
            return float(value - 273.15)
        elif fromUnit.upper() == "KELVIN" and toUnit.upper() == "FAHRENHEIT":
            return float(1.8 * (value - 273.15) + 32)
        elif fromUnit.upper() == "MILES" and toUnit.upper() == "YARDS":
            return float(value * 1760)
        elif fromUnit.upper() == "MILES" and toUnit.upper() == "METERS":
            return float(value * 1609.344)
        elif fromUnit.upper() == "YARDS" and toUnit.upper() == "MILES":
            return float(value / 1760)
        elif fromUnit.upper() == "YARDS" and toUnit.upper() == "METERS":
            return float(value * 0.9144)
        elif fromUnit.upper() == "METERS" and toUnit.upper() == "MILES":
            return float(value / 1609.344)
        elif fromUnit.upper() == "METERS" and toUnit.upper() == "YARDS":
            return float(value / 0.9144)
    except TypeError:
        raise ConversionNotPossible(ValueError)
