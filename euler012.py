#!/usr/bin/env python

from euler005 import factorize
from euler007 import eratosthenes

def triangle_numbers(limit):
    sum = 0
    for i in range(1,limit+1):
        sum += i
        yield sum

def prime_factorize(n, primes=None):
    if primes is None:
        primes = eratosthenes(n/2)
    factors = factorize(t, primes)
    prime_factors = {}
    for f in factors:
        if not prime_factors.has_key(f):
            prime_factors[f] = 1
        else:
            prime_factors[f] += 1
    return prime_factors

if __name__=="__main__":
    limit = 100000
    primes = eratosthenes(limit)
    for i,t in enumerate(triangle_numbers(limit)):
        factors = prime_factorize(t, primes)
        # with n prime factors, we can make 2**n divisors
        divisors = 1 # include 1 for the number 1
        for f in factors.keys():
            divisors *= factors[f] + 1
        if divisors > 500:
            print "Triangle number {} is {} and has factors {} and therefore {} divisors".format(i, t, factors, divisors)
            break
