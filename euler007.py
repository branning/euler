#!/usr/bin/env python

import math

def atkin(limit):
    '''
    from http://en.wikipedia.org/wiki/Sieve_of_Atkin
    '''
    # initialize the sieve
    is_prime = [False] * (limit + 1)
    is_prime[0:3] = [True] * 3

    # put in candidate primes:
    # integers which have an odd number of representations by certain quadratic forms

    for x in xrange(1, int(math.sqrt(limit))):
        for y in xrange(1, int(math.sqrt(limit))):
            n = 4*x*x + y*y
            if (n <= limit) and (n % 12 == 1 or n % 12 == 5):
                is_prime[n] = not is_prime[n]
            n = 3*x*x + y*y
            if (n <= limit) and (n % 25 == 7):
                is_prime[n] = not is_prime[n]
            n = 3*x*x - y*y
            if (x > y) and (n <= limit) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]

    # eliminate composites by sieving
    for n in xrange(5, int(math.sqrt(limit))):
        if is_prime[n]:
            # n is prime, omit multiples of its square; this is sufficient
            # because composites which managed to get on the list cannot
            # be square-free
            k = n*n
            while k <= limit:
                is_prime[k] = False
                k = k + n*n

    primes = [2, 3]
    for n in xrange(5, limit+1):
        if is_prime[n]:
            primes.append(n)

    return primes

def eratosthenes(limit):

    is_prime = [True] * (limit + 1)

    # seed the sieve by removing multiples of 2 and 3
    primes = [2,3]
    for x in primes:
        is_prime[x+x : limit + 1: x] = [False] * len(xrange(x+x, limit + 1, x))

    for i in xrange(5, limit + 1):
        if not is_prime[i]:
            continue
        is_prime[i + i: limit + 1: i] = [False] * len(xrange(i+i, limit + 1, i))
        if i**2 > limit:
            break

    for i in xrange(5, limit + 1):
        if is_prime[i]:
            primes.append(i)

    return primes