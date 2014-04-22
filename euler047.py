#!/usr/bin/env python

from euler007 import eratosthenes
from euler012 import prime_factorize

primes = eratosthenes(10**6)

import pdb; pdb.set_trace()

therun = []
limit = 10**6
start = 646 # the 3-run example ends here
for n in range(start+1, limit+1):
  factors = prime_factorize(n, primes)
  if len(factors.keys()) >= 4:
    therun.append(n)
  else:
    therun = []
  if len(therun) == 4:
    print therun[0]
    break
else:
  print "Failed to find a run of 4 consecutive integers with 4 prime factors less than {}".format(limit)
