#!/usr/bin/env python

from euler007 import eratosthenes
from math import sqrt, ceil

def goldbach_decompose(n, primes):
  # can n be written as the sum of a prime and a power of 2?
  primes_set = set(primes)
  for s in range(1, int(ceil(sqrt(n/2)))):
    diff = n - 2*s**2
    if diff in primes:
      return diff, s
  else:
    return None

limit = 10**5
primes = eratosthenes(limit)

odd_composites = set(range(9,limit+1,2)) # start with 9
odd_composites -= set(primes) # remove primes
odd_composites = list(odd_composites) # listify
odd_composites.sort()

for n in odd_composites:
  decomposition = goldbach_decompose(n, primes)
  if decomposition:
    prime,square = decomposition
    #print "{} = {} - 2*{}^2".format(n, prime, square)
  else: # failed to decompose
    #print "Cannot decompose {}".format(n)
    print n
    break
