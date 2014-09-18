"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the
number and for the multiples of five print "Buzz".
For numbers which are multiples of both print "FizzBuzz".
"""

def fizzbuzz(num):
    result = ""

    if (num % 15 == 0):
        result = "FizzBuzz"
    elif (num % 5 == 0):
        result = "Buzz"
    elif (num % 3 == 0):
        result = "Fizz"
    else:
        result = str(num)

    return result


if __name__ == "__main__": # pragma: no cover
    for i in range(1, 101):
        print fizzbuzz(i)
