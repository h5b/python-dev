#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import assert_equal

from util.gcd import gcd

def test_gcd_returns_1_given_args_0_and_1():
    assert_equal(gcd(0, 1), 1)

def test_gcd_returns_1_given_args_1_and_0():
    assert_equal(gcd(1, 0), 1)

def test_gcd_returns_1_given_args_1_and_1():
    assert_equal(gcd(1, 1), 1)

def test_gcd_returns_6_given_args_54_and_24():
    assert_equal(gcd(54, 24), 6)
