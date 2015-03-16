#!/usr/bin/env python

from euler007 import eratosthenes
import itertools
from math import sqrt, ceil

def millerrabin(n):
  return rabinmiller(n)

def rabinmiller(n):
  limit = 341550071728321
  a_s = [2,3,5,7,11]
  if n > 2152302898747:
    a_s.append(13)
  if n > 3474749660383:
    a_s.append(17)
  if n >= limit:
    print "Cannot do deterministic Rabin Miller for n > {}".format(limit)
    return None

  s = 0
  d = n-1
  while(d % 2 == 0):
    d = d/2
    s += 1
  # n-1 == d*s**2 now

  for a in a_s:
    if a**d % n != 1:
      for r in range(s):
        if a**(2**r*d) % n == n-1:
          break
      else:
        return False # the number is composite
  return True

def isPrime(n, lowprimes=None):
  prime_ceiling = 10**6
  limit = int(ceil(sqrt(n))) # the highest of the "low primes"
  if lowprimes is None:
    lowprimes = eratosthenes( min(prime_ceiling, limit) )
  # if the number is too large to check by generating primes,
  # use the Miller-Rabin primality test
  useRabinMiller = True if limit > prime_ceiling else False

  prime = True
  for p in primes: # check a bunch of low primes first
    if n % p == 0:
      prime = False
      break
  else: # none of the primes divided n
    if useRabinMiller: # and our number is large
      print "trying Rabin Miller on {}".format(n)
      prime = rabinmiller(n)
  return prime


if __name__=="__main__":
  limit = 7654321
  digits = list(str(limit))
  primes = eratosthenes(int(ceil(sqrt(limit))))
  while len(digits) > 2:
    for d in itertools.permutations(digits):
      n = int(''.join(d))
      if isPrime(n):
        print n
        digits = [] # stop while loop
        break
    digits = digits[1:]
