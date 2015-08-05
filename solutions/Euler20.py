from math import factorial
from supportFunctions import sum_digits

# support functions coming in handy!
def euler():
    ans = sum_digits(factorial(100))
    print ("Euler 20 answer: %d") % ans