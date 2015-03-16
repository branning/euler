#!/usr/bin/env python

from euler007 import eratosthenes

def factorize(n, primes=None):
    if primes is None:
        primes = eratosthenes(n)
    if n in primes:
        return [n]
    factors = []
    for p in primes:
        if p >= n:
            break
        multiplicity = 1
        while n % p**multiplicity == 0:
            factors.append(p)
            multiplicity += 1
        if len(factors) > 0 and n == reduce(lambda x,y: x*y, factors):
            break
    return factors

def factorize_range(limit, primes):
    factors = {}
    for n in range(2, limit + 1):
        factors[n] = factorize(n, primes)
    return factors

def LCM(numbers):
    primes = eratosthenes(max(numbers))
    factors = {}
    for n in numbers:
        factors[n] = factorize(n, primes)    
    common_factors = {}
    for n in factors.keys():
        for f in set(factors[n]):
            multiplicity = sum([f==i for i in factors[n]])
            if not common_factors.has_key(f):
                common_factors[f] = multiplicity
            elif multiplicity > common_factors[f]:
                common_factors[f] = multiplicity
    common_multiple = 1
    for f in common_factors:
        common_multiple *= f ** common_factors[f]
    return common_multiple

if __name__=="__main__":
    limit = 20
    print LCM(range(2,limit+1))