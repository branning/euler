#!/usr/bin/env python

from euler007 import eratosthenes

def quadratic(n, a, b):
  return n**2 + a*n + b

limitN = 300
limitA = 1000
limitB = 1000
primes = set(eratosthenes(quadratic(limitN, limitA, limitB)))

max_consecutive_primes = 0
maxAB = (None,None)
consecutive_primes = [[None] * (2*limitA+1)] * (2*limitB+1)

debugging = False

for a in range(-1*limitA,limitA+1):
  for b in range(-1*limitB,limitB+1):
    n = 0
    while quadratic(n, a, b) in primes:
      n += 1
      if n == limitN:
        print "Warning: exceeded N limit of {} with a={} b={}".format(limitN, a, b)
    consecutive_primes[a][b] = n
    if n > max_consecutive_primes:
      max_consecutive_primes = n
      maxAB = (a,b)
if debugging:
  print "With a={} b={}, generated {} primes from n=(0,{})"\
        .format(maxAB[0],maxAB[1],max_consecutive_primes,max_consecutive_primes-1)
print maxAB[0]*maxAB[1]
