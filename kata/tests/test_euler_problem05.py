#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import assert_equal

from kata.kata.euler_problem_05 import least_common_multiple_from_1_to

class TestEulerProblem05:

    def test_euler05_returns_1_for_least_common_multiple_from_1_to_1(self):
        assert_equal(1, least_common_multiple_from_1_to(1))

    def test_euler05_returns_2_for_least_common_multiple_from_1_to_2(self):
        assert_equal(2, least_common_multiple_from_1_to(2))

    def test_euler05_returns_6_for_least_common_multiple_from_1_to_3(self):
        assert_equal(6, least_common_multiple_from_1_to(3))

    def test_euler05_returns_12_for_least_common_multiple_from_1_to_4(self):
        assert_equal(12, least_common_multiple_from_1_to(4))

    def test_euler05_returns_2520_for_least_common_multiple_from_1_to_10(self):
        assert_equal(2520, least_common_multiple_from_1_to(10))
