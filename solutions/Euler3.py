from supportFunctions import primes_sieve, isInt
from math import sqrt

def euler():
    num=600851475143

    tl = primes_sieve(int(sqrt(num)))
    best=1
    for x in tl:
        if isInt(num/float(x)) and x>best:
            best=x
        
    print "Euler 3 answer: %d"  %best






