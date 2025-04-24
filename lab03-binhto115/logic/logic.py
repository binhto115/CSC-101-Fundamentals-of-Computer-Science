# True if the reminder of n is 0. Otherwise, false
def is_even(n: int) -> bool:
    number = int(n)
    reminder = number % 2
    return reminder == 0


"""Tests to see if the inputted number is included 
    within the given interval."""


def in_an_interval(n: float) -> bool:
    num = float(n)
    return 2 <= num < 9 or 47 < num < 92 or 12 < num <= 19 or 101 <= num <= 103

