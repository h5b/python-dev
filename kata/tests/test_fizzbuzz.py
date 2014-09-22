#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import raises

from kata.kata.fizzbuzz import fizzbuzz


class TestFizzBuzz:

    def test_fizzbuzz_returns_string_fizz(self):
        assert_equal("Fizz", fizzbuzz(3))
        assert_equal("Fizz", fizzbuzz(6))

    def test_fizzbuzz_returns_string_buzz(self):
        assert_equal("Buzz", fizzbuzz(5))
        assert_equal("Buzz", fizzbuzz(10))

    def test_fizzbuzz_returns_string_fizzbuzz(self):
        assert_equal("FizzBuzz", fizzbuzz(15))
        assert_equal("FizzBuzz", fizzbuzz(30))

    def test_fizzbuzz_returns_number_if_not_divisible_by_3_and_5(self):
        assert_equal("1", fizzbuzz(1))
        assert_equal("97", fizzbuzz(97))

    @raises(TypeError)
    def test_fizzbuzz_raises_error_on_invalid_arg(self):
        fizzbuzz("python")
        fizzbuzz(3.14159265359)
