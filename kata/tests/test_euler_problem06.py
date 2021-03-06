#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import assert_equal

from kata.kata.euler_problem_06 import difference_between_sum_and_square
from kata.kata.euler_problem_06 import square_of_sum
from kata.kata.euler_problem_06 import sum_of_squares

class TestEulerProblem06:

    def test_euler06_returns_385_for_sum_of_squares_from_1_to_10(self):
        result = sum_of_squares(10)
        assert_equal(385, result)

    def test_euler06_returns_3025_for_square_of_sum_from_1_to_10(self):
        result = square_of_sum(10)
        assert_equal(3025, result)

    def test_euler06_returns_2640_for_difference_between_sum_and_square_from_1_to_10(self):
        result = difference_between_sum_and_square(10)
        assert_equal(2640, result)
