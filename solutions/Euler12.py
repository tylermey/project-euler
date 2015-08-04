# this is definitely one of my slower/hacky answers
# I should come back and speed this up.
from supportFunctions import num_divisors
import time
def euler():
    iter = 1
    ans = 1
    mult = 1
    while ans<=500:
        mult+=1
        # you don't have to check every number
        iter+=mult
        ans = num_divisors(iter)
    print "Euler 11 Answer: %d" % iter