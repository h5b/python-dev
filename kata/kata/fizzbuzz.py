"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the
number and for the multiples of five print "Buzz".
For numbers which are multiples of both print "FizzBuzz".
"""

def fizzbuzz(num):
    return str(num)


if __name__ == "__main__": # pragma: no cover
    for i in range(1, 101):
        print fizzbuzz(i)
