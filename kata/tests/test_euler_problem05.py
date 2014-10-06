#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import assert_equal

from kata.kata.euler_problem_05 import least_common_multiple_from_1_to

class TestEulerProblem05:

    def test_euler05_returns_2520_for_least_common_multiple_from_1_to_10(self):
        assert_equal(2520, least_common_multiple_from_1_to(10))
