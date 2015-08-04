from math import sqrt
from supportFunctions import primes_sieve
def euler():
    ans = primes_sieve(2000000)
    print("Euler 10 answer: %d") %sum(ans)