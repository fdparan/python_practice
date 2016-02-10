"""
@author: francisparan
"""


def exponent(base, power):
    result = 1

    if power < 0:
        return 1.0 / exponent(base, -1 * power)

    for y in range(power):
        result *= base

    return result

