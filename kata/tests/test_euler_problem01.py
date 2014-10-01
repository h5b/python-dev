#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import assert_equal

from kata.kata.euler_problem_01 import sum_of_multiples_of_3_or_5_below

class TestEulerProblem01:

    def test_euler01_returns_sum_of_zero_for_multiples_of_3_or_5_below_3(self):
        result = sum_of_multiples_of_3_or_5_below(3)
        assert_equal(0, result)

    def test_euler01_returns_sum_of_3_for_multiples_of_3_or_5_below_4(self):
        result = sum_of_multiples_of_3_or_5_below(4)
        assert_equal(3, result)

    def test_euler01_returns_sum_of_23_for_multiples_of_3_or_5_below_10(self):
        result = sum_of_multiples_of_3_or_5_below(10)
        assert_equal(23, result)
