"""
#
# This file holds support functions that will be used in more than one Euler solution
#
"""
import math
# Input: limit on how high the sieve should enumerate
# Output: list of primes up to limit
# This implementation of the sieve is not entirely my own, some help was needed from google for speedups
def primes_sieve(limit):
    n = limit+1
    removed = set()
    primes = []
    for i in range(2, n):
        if i in removed:
            continue
        for num in range(i*2, n, i):
            removed.add(num)
        primes.append(i)
    return primes

# Input: number of primes to find 
# Output: that numbered prime   
def find_Nth_prime(n):
    prime = 2
    count = 1
    iter = 3
    while count < n:
        if is_prime(iter):
            prime = iter
            count += 1
        iter += 2
    return prime
    
# Input: number
# Output: boolean if prime 
def is_prime(x):
    if x % 2==0: return False
    i=3
    #while i < int(sqrt(x)):
    while i < x**0.5+1:
        if x % i == 0:
            return False
        i+= 2
    return True

# Input: number
# Output: boolean of if int
# python lacks a good implementation of this function
def isInt(inNum):
    if (math.floor(inNum)==inNum):
        return True
    else: 
        return False
        
# Input: number
# Output: factors
# I got bored, so I tried to write it as a recursion 
def find_factors(inNum):
    # found this sweet function xrange I'd never seen before, and it's FAST
    for i in xrange(2,inNum):
        if inNum%i==0: return (i,) + find_factors(inNum/i)
    return (inNum,1)

# Input: number
# Output: number of divisors
def num_divisors(inNum):
    total = 0
    sq = int(math.ceil(math.sqrt(inNum)))
    if isInt(sq):
        total+=1
    for i in range(1, int(sq)):
        if inNum % i == 0:
            total +=2
        else:
            continue
    return total