#!/usr/bin/env python

from euler007 import eratosthenes
import itertools

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

# check a bunch of low primes first
primes = eratosthenes(10**4)

digits = list('987654321')
while len(digits) > 2:
  for d in itertools.permutations(digits):
    n = int(''.join(d))
    prime = True
    for p in primes:
      if n % p == 0:
        prime = False
        break
    if not prime:
      #print "not {}".format(n)
      continue
    #print "trying Rabin Miller on {}".format(n)
    if rabinmiller(n):
      print n
      digits = []
      break
  digits = digits[1:]
