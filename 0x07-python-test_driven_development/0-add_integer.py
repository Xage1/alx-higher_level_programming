#!/usr/bin/python3
"""
Function add two integers
Return: The sum of a and b.
"""


def add_integer(a, b=98):
    """Function that validate the add of two integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
