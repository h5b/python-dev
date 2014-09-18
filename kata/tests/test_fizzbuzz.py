from nose.tools import assert_equal
from nose.tools import assert_not_equal

from kata.kata.fizzbuzz import fizzbuzz

def test_fizz():
    assert_equal("Fizz", fizzbuzz(3))

def test_buzz():
    assert_equal("Buzz", fizzbuzz(5))

def test_fizzbuzz():
    assert_equal("FizzBuzz", fizzbuzz(15))

def test_returns_num():
    assert_equal(str(2), fizzbuzz(2))
