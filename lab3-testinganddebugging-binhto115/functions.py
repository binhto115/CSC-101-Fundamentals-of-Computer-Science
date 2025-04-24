# Name: Binh To
# Date: 10/10/2022
# Github: binhto115

def addValues(a: int, b: int) -> int:
    """Returns the sum of the given values"""
    return a + b

def getSquareRoot(x: float) -> float:
    """Returns the square root of the given value"""
    return x ** 0.5

def convertToCelsius(fahrenheit: float) -> float:
    """Converts the given Fahrenheit temperature value to Celsius"""
    return (fahrenheit - 32.0) / 1.8

def capitalizeCharacter(string: str, n: int) -> str:
    """Returns the string with the n'th character capitalized."""
    string = list(string)
    string[n - 1] = string[n - 1].upper()
    string = ''.join(string)
    return string
