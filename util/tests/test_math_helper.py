#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import assert_equal

from util.math_helper import gcd
from util.math_helper import lcm

class TestMathHelperGCD:

    def test_gcd_returns_1_given_args_0_and_1(self):
        assert_equal(gcd(0, 1), 1)

    def test_gcd_returns_1_given_args_1_and_0(self):
        assert_equal(gcd(1, 0), 1)

    def test_gcd_returns_1_given_args_1_and_1(self):
        assert_equal(gcd(1, 1), 1)

    def test_gcd_returns_6_given_args_54_and_24(self):
        assert_equal(gcd(54, 24), 6)


class TestMathHelperLCM:

    def test_lcm_returns_6_given_args_3_and_6(self):
        assert_equal(lcm(3, 6), 6)

    def test_lcm_returns_6_given_args_6_and_3(self):
        assert_equal(lcm(6, 3), 6)

    def test_lcm_returns_15_given_args_3_and_5(self):
        assert_equal(lcm(3, 5), 15)
