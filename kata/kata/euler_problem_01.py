#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Euler Project - Problem 1
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_of_multiples_of_3_or_5_below(number):
    multiples = filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1, number))

    if not multiples:
        return 0

    return reduce(lambda x, y: x + y, multiples)


if __name__ == "__main__": # pragma: no cover
    result = sum_of_multiples_of_3_or_5_below(1000)
    print "sum of multiples of 3 or 5 below {0}: {1}".format(1000, result)
