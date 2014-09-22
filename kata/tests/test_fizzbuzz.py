from nose.tools import assert_equal
from nose.tools import assert_not_equal

from kata.kata.fizzbuzz import fizzbuzz
from util.list_helper import intersect
from util.list_helper import exclusive


class TestFizzBuzz:

    def setup(self):
        self.numbers = range(1, 101)
        self.L_fizzes = filter(lambda x: (x % 3 == 0), self.numbers)
        self.L_buzzes = filter(lambda x: (x % 5 == 0), self.numbers)

        """ filter non-unique elements to match criterion """
        self.L_fizzbuzzes = intersect(self.L_buzzes, self.L_fizzes)
        self.L_fizzes = exclusive(self.L_fizzes, self.L_fizzbuzzes)
        self.L_buzzes = exclusive(self.L_buzzes, self.L_fizzbuzzes)
        self.L_integers = exclusive(self.numbers,
                self.L_fizzes + self.L_buzzes + self.L_fizzbuzzes)


    def test_fizz(self):
        [assert_equal("Fizz", fizzbuzz(n)) for n in self.L_fizzes]

    def test_buzz(self):
        [assert_equal("Buzz", fizzbuzz(n)) for n in self.L_buzzes]

    def test_fizzbuzz(self):
        [assert_equal("FizzBuzz", fizzbuzz(n)) for n in self.L_fizzbuzzes]

    def test_returns_num(self):
        [assert_equal(str(n), fizzbuzz(n)) for n in self.L_integers]
