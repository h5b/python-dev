#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Euler Project - Problem 6
Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

def sum_of_squares(upper_limit):
    squares = map(lambda x: x**2, range(1, upper_limit + 1))
    return reduce(lambda x, y: x + y, squares)

def square_of_sum(upper_limit):
    sum = reduce(lambda x, y: x + y, range(1, upper_limit + 1))
    return sum**2

def difference_of_sum_and_square(upper_limit):
    return (square_of_sum(upper_limit) - sum_of_squares(upper_limit))


if __name__ == "__main__": # pragma: no cover
    result = difference_of_sum_and_square(100)
    print "difference(1 to 100): {0}".format(result)
