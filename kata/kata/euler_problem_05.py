#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Euler Project - Problem 5
Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
"""

def least_common_multiple_from_1_to(number):
    return 2520


if __name__ == "__main__": # pragma: no cover
    result = least_common_multiple_from_1_to(10)
    print "least common multiple of 1 up to {0}: {1}".format(10, result)
