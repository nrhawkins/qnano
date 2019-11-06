"""Euler Problem #1: Sum the numbers which are divisible by x and y and less than z.
"""
import math
import numpy as np

def sum_factors_less_than_z(x, y, z):
    """
    """
    sum_factors = 0
    for i in range(1, z, 1):
    
        if i % x == 0 or i % y == 0:
            sum_factors += i

    return sum_factors

def sum_factors_less_than_z_verify(x, y, z):
    """
    """
    sum_factors = 0

    max_x = math.floor((z-1)/x)
    max_y = math.floor((z-1)/y)

    lx = x*np.array(range(1, max_x + 1))
    ly = y*np.array(range(1, max_y + 1))

    s = set(lx)
    s.update(ly)

    sum_factors += sum(s)

    return sum_factors

print("sum factors: ", sum_factors_less_than_z(3, 5, 10))
print("sum factors: ", sum_factors_less_than_z_verify(3, 5, 10))

print("sum factors: ", sum_factors_less_than_z(3, 5, 1000))
print("sum factors: ", sum_factors_less_than_z_verify(3, 5, 1000))

assert sum_factors_less_than_z(3, 5, 10) == 23
assert sum_factors_less_than_z(3, 5, 1000) == 233168

print("sum factors: ", sum_factors_less_than_z(3, 5, -1000))



