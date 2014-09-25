#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import raises

from kata.kata.euler_problem_06 import difference_of_sum_and_square
from kata.kata.euler_problem_06 import square_of_sum
from kata.kata.euler_problem_06 import sum_of_squares

class TestEulerProblem06:

    def test_euler06_returns_sum_of_squares_from_1_to_10(self):
        result = sum_of_squares()
        assert_equal(385, result)

    def test_euler06_returns_square_of_sum_from_1_to_10(self):
        result = square_of_sum()
        assert_equal(3025, result)

    def test_euler06_returns_difference_between_sum_and_square(self):
        result = difference_of_sum_and_square()
        assert_equal(2640, result)
